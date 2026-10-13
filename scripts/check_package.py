#!/usr/bin/env python3
"""Check local package structure/resources; not a browser or security audit."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


def check(root):
    root = Path(root).resolve()
    errors = []

    def fail(message):
        errors.append(message)

    def local(base, target):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//')):
            return None
        path = (base / unquote(parsed.path)).resolve()
        if not path.is_relative_to(root):
            fail(f'Path outside package: {target}')
            return None
        elif not path.exists():
            fail(f'Missing local resource: {path.relative_to(root)}')
            return None
        return path

    try:
        market = json.loads((root / '.agents/plugins/marketplace.json').read_text())
        assert market['name'] == 'html-briefing'
        entry, = market['plugins']
        assert entry['name'] == 'html-briefing'
        assert entry['source'] == {'source': 'local', 'path': './plugins/html-briefing'}
        plugin = local(root, entry['source']['path'])
        assert plugin is not None
        manifest = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
        portable = json.loads((plugin / 'plugin.json').read_text())
        for field in ('name', 'version', 'description', 'license', 'repository'):
            assert portable[field] == manifest[field], f'Portable/compatibility mismatch: {field}'
        assert portable['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
        assert manifest['name'] == 'html-briefing' and manifest['license'] == 'MIT AND Apache-2.0'
        assert re.fullmatch(r'\d+\.\d+\.\d+(?:\+[0-9A-Za-z.-]+)?', manifest['version'])
        assert manifest['skills'].startswith('./') and '..' not in Path(manifest['skills']).parts
        skills = local(plugin, manifest['skills'])
        assert skills and skills.is_relative_to(root)
        bundle = json.loads((plugin / 'bundle.json').read_text())
        assert bundle['version'] == manifest['version'], 'Bundle version mismatch'
        imported = {item['skill']: item for item in bundle['bundled']}
        expected = set(bundle['coordinationSkills']) | set(imported)
        assert bundle['coordinationSkills'] == ['html-briefing'], 'Use one briefing coordination entrypoint'
        assert expected == {'playwright', 'gsap-core', 'gsap-performance', 'gsap-plugins', 'ui-ux-pro-max', 'gsap-scrolltrigger', 'html-briefing', 'gsap-timeline', 'gsap-utils', 'impeccable', 'gsap-frameworks', 'gsap-react'} and len(imported) == 11, 'Incomplete declared bundle'
        actual = {p.parent.name for p in skills.glob('*/SKILL.md')}
        assert actual == expected, f'Skill inventory: expected {sorted(expected)}, got {sorted(actual)}'
        for name in expected:
            entry = skills / name / 'SKILL.md'
            match = re.search(r'^name:\s*["\']?([a-z0-9-]+)["\']?\s*$', entry.read_text().split('---', 2)[1], re.M)
            assert match and match.group(1) == name, f'Wrong skill name: {name}'
            assert (skills / name / 'agents/openai.yaml').is_file(), f'Missing UI metadata: {name}'
        for resource in ('references/flow-canvas.md', 'assets/flow-canvas/presentation.template.html', 'assets/flow-canvas/canvas-model.js', 'scripts/build_flow_canvas.py'):
            assert local(skills / 'html-briefing', resource), f'Missing canvas resource: {resource}'
        for name, record in imported.items():
            base = skills / name
            assert record['license'] in {'MIT', 'Apache-2.0'}, f'Unreviewed license: {name}'
            assert record['licenseFile'] in record['files'], f'Missing license record: {name}'
            for resource, digest in record['files'].items():
                path = local(base, resource)
                assert path and path.is_file(), f'Missing bundled resource: {name}/{resource}'
                assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Changed bundled resource without provenance update: {name}/{resource}'
    except (AssertionError, KeyError, ValueError, TypeError, OSError) as exc:
        fail(f'Invalid package/skill manifest: {exc}')

    for required in ['README.md', 'README.zh-CN.md', 'LICENSE', 'AGENTS.md', 'PROJECT_STATE.md']:
        if not (root / required).is_file():
            fail(f'Missing required file: {required}')
    for path in root.rglob('*'):
        if any(part in {'.git', '.venv', '__pycache__'} for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            fail(f'Symlink is not a portable package resource: {path.relative_to(root)}')
            continue
        if path.suffix == '.md':
            text = path.read_text()
            # Documentation examples are not package resources.
            text = re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', text, flags=re.M | re.S)
            text = re.sub(r'`+[^`\n]*`+', '', text)
            targets = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text)
            targets += re.findall(r'(?:href|src)=[\'"]([^\'"]+)[\'"]', text)
            for target in targets:
                local(path.parent, target)
        if path.suffix == '.svg':
            try:
                ElementTree.parse(path)
            except ElementTree.ParseError as exc:
                fail(f'Invalid SVG {path.relative_to(root)}: {exc}')
    return errors


if __name__ == '__main__':
    issues = check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    for issue in issues:
        print('FAIL:', issue)
    print('Package structure/resources:', 'FAIL' if issues else 'PASS')
    sys.exit(bool(issues))
