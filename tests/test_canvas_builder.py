"""Exercise the packaged builder, its portable output and overwrite boundary."""
import importlib.util
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'plugins/html-briefing/skills/html-briefing'
spec = importlib.util.spec_from_file_location('canvas_builder', SKILL / 'scripts/build_flow_canvas.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class CanvasBuilder(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / 'presentation.html'
        self.template = SKILL / 'assets/flow-canvas/presentation.template.html'
        self.model = SKILL / 'assets/flow-canvas/canvas-model.js'

    def test_real_starter_builds_portably(self):
        builder.build(self.template, self.model, self.output)
        html = self.output.read_text()
        self.assertNotIn('/* MODEL */', html)
        self.assertEqual(html, (ROOT / 'examples/flow-canvas.html').read_text())
        self.assertFalse(re.search(r'(?:src|href)=[\"\'](?:https?:|/)', html))
        self.assertNotIn('/Users/', html)
        script = self.output.with_suffix('.js')
        script.write_text('\n'.join(re.findall(r'<script>(.*?)</script>', html, re.S)))
        subprocess.run(['node', '--check', str(script)], check=True, capture_output=True)

    def test_double_click_focus(self):
        subprocess.run(['node', str(ROOT / 'tests/canvas-double-click.test.cjs')], check=True, capture_output=True)

    def test_existing_output_is_preserved(self):
        self.output.write_text('User work')
        with self.assertRaises(FileExistsError):
            builder.build(self.template, self.model, self.output)
        self.assertEqual(self.output.read_text(), 'User work')
        builder.build(self.template, self.model, self.output, force=True)
        self.assertTrue(self.output.read_text().startswith('<!doctype html>'))

    def test_sources_cannot_be_overwritten(self):
        with self.assertRaises(ValueError):
            builder.build(self.template, self.model, self.model, force=True)

    def test_invalid_template_and_script_are_rejected(self):
        template = Path(self.tmp.name) / 'template.html'
        template.write_text('/* MODEL */ /* MODEL */')
        with self.assertRaises(ValueError):
            builder.build(template, self.model, self.output)
        self.assertFalse(self.output.exists())
        template.write_text('<script>/* MODEL */</script>')
        model = Path(self.tmp.name) / 'model.js'
        model.write_text('</ScRiPt>')
        with self.assertRaises(ValueError):
            builder.build(template, model, self.output)
        self.assertFalse(self.output.exists())


if __name__ == '__main__':
    unittest.main()
