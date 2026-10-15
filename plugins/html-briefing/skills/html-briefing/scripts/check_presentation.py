#!/usr/bin/env python3
"""Check canvas structure and hash-bound browser evidence, not browser behavior itself."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

CHECKS = ('layout', 'navigation_zoom', 'focus', 'disclosure', 'reading')


class CanvasHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.scripts = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'script':
            self.in_script = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False

    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)


def check_html(html):
    """Detect missing starter infrastructure; not a JavaScript correctness proof."""
    doc = CanvasHTML()
    doc.feed(html)
    errors = []
    for name in ('stage', 'viewport', 'world', 'blocks', 'nav-shell'):
        if doc.ids.count(name) != 1:
            errors.append(f'Expected one canvas element #{name}')
    code = '\n'.join(doc.scripts)
    code = re.sub(r'/\*.*?\*/|//[^\n]*', '', code, flags=re.S)
    for name in ('focusNode', 'pan', 'setSize', 'toggleTree', 'toggleDetail',
                 'rememberReading', 'restoreReading', 'beginPinch'):
        if not re.search(r'function\s+' + name + r'\s*\(', code):
            errors.append(f'Missing canvas controller: {name}')
    for event in ('dblclick', 'keydown', 'wheel'):
        if not re.search(r"addEventListener\(\s*['\"]" + event + r"['\"]", code):
            errors.append(f'Missing canvas input: {event}')
    if '/* MODEL */' in html or 'CanvasModel.zoomView' not in code:
        errors.append('Canvas model is missing or not assembled')
    return errors


def check_report(report, digest, alternative_request=None):
    errors = []
    if report.get('artifact_sha256') != digest:
        errors.append('Browser evidence is stale or belongs to a different artifact')
    if not isinstance(report.get('environment'), str) or not report['environment'].strip():
        errors.append('Browser environment must be recorded')
    checks = report.get('checks')
    if not isinstance(checks, dict):
        return errors + ['Browser checks must be an object']
    required = ('alternative_behavior',) if alternative_request else CHECKS
    if alternative_request and report.get('user_request') != alternative_request:
        errors.append('Alternative evidence must quote the same explicit user request')
    for name in required:
        item = checks.get(name)
        if not isinstance(item, dict) or item.get('status') != 'PASS' or not isinstance(item.get('evidence'), str) or not item['evidence'].strip():
            errors.append(f'Browser check not verified: {name}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--structural-only', action='store_true')
    parser.add_argument('--browser-report', type=Path)
    parser.add_argument('--alternative-request', help='Exact explicit user request for another mode; never invent approval')
    args = parser.parse_args()
    try:
        if args.alternative_request is not None and not args.alternative_request.strip():
            raise ValueError('An alternative requires a non-empty explicit user request')
        if args.structural_only and args.browser_report:
            raise ValueError('Choose structural-only or final browser-evidence checking')
        data = args.artifact.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        errors = [] if args.alternative_request else check_html(data.decode('utf-8'))
        if errors:
            raise ValueError('; '.join(errors))
        print(f'artifact_sha256: {digest}')
        if args.structural_only:
            print('ALTERNATIVE EXEMPTION' if args.alternative_request else 'STRUCTURE PASS')
            print('Browser acceptance: UNVERIFIED')
            return
        if not args.browser_report:
            parser.exit(2, 'UNVERIFIED: supply --browser-report after inspecting this final artifact\n')
        report = json.loads(args.browser_report.read_text(encoding='utf-8'))
        if not isinstance(report, dict):
            raise ValueError('Browser report must be an object')
        errors = check_report(report, digest, args.alternative_request)
        if errors:
            raise ValueError('; '.join(errors))
        print('ACCEPTANCE RECORD PASS' + (' (explicit alternative)' if args.alternative_request else ' (flow canvas)'))
        print('Recorded browser evidence checked; this command did not run a browser.')
    except (OSError, ValueError) as error:
        parser.exit(1, f'FAIL: {error}\n')


if __name__ == '__main__':
    main()
