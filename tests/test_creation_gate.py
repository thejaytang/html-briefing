"""Exercise the default creation path and reject incomplete or stale delivery evidence."""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'plugins/html-briefing/skills/html-briefing/scripts'
CHECK = runpy.run_path(str(SCRIPTS / 'check_presentation.py'))


class CreationGate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name) / 'briefing'
        self.artifact = self.directory / 'presentation.html'

    def run_script(self, name, *args):
        return subprocess.run(['python3', str(SCRIPTS / name), *map(str, args)], capture_output=True, text=True)

    def create(self):
        result = self.run_script('new_briefing.py', '--directory', self.directory)
        self.assertEqual(result.returncode, 0, result.stderr)

    def report(self):
        # Synthetic evidence exercises the validator, not actual browser acceptance.
        return {'artifact_sha256': hashlib.sha256(self.artifact.read_bytes()).hexdigest(),
                'environment': 'synthetic test fixture',
                'checks': {name: {'status': 'PASS', 'evidence': 'synthetic fixture'} for name in CHECK['CHECKS']}}

    def test_default_creation_and_no_overwrite(self):
        self.create()
        self.assertEqual(self.artifact.read_bytes(), (ROOT / 'examples/flow-canvas.html').read_bytes())
        self.artifact.write_text('User material')
        result = self.run_script('new_briefing.py', '--directory', self.directory)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.artifact.read_text(), 'User material')

    def test_plain_page_is_rejected_even_with_canvas_words(self):
        html = '<html><body>flow canvas focusNode dblclick</body></html>'
        self.assertTrue(CHECK['check_html'](html))
        self.create()
        self.artifact.write_text(html)
        result = self.run_script('check_presentation.py', self.artifact, '--structural-only')
        self.assertEqual(result.returncode, 1)

    def test_builder_rejects_missing_interaction_before_overwriting(self):
        self.create()
        template = self.directory / 'presentation.template.html'
        template.write_text(template.read_text().replace("addEventListener('dblclick'", "addEventListener('unused'"))
        original = self.artifact.read_bytes()
        result = self.run_script('build_flow_canvas.py', '--template', template, '--model', self.directory / 'canvas-model.js', '--output', self.artifact, '--force')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.artifact.read_bytes(), original)

    def test_structure_does_not_imply_acceptance(self):
        self.create()
        result = self.run_script('check_presentation.py', self.artifact)
        self.assertEqual(result.returncode, 2)
        self.assertIn('UNVERIFIED', result.stderr)
        result = self.run_script('check_presentation.py', self.artifact, '--structural-only')
        self.assertEqual(result.returncode, 0)
        self.assertIn('Browser acceptance: UNVERIFIED', result.stdout)

    def test_evidence_must_be_complete_and_match_final_bytes(self):
        self.create()
        evidence = self.report()
        digest = evidence['artifact_sha256']
        self.assertEqual(CHECK['check_report'](evidence, digest), [])
        for state in ('FAIL', 'UNVERIFIED', 'SKIPPED'):
            evidence['checks']['focus']['status'] = state
            self.assertTrue(CHECK['check_report'](evidence, digest))
        evidence = self.report()
        evidence['checks']['focus']['evidence'] = ''
        self.assertTrue(CHECK['check_report'](evidence, digest))
        evidence = self.report()
        report = Path(self.tmp.name) / 'browser.json'
        report.write_text(json.dumps(evidence))
        self.assertEqual(self.run_script('check_presentation.py', self.artifact, '--browser-report', report).returncode, 0)
        self.artifact.write_text(self.artifact.read_text() + '\n')
        self.assertEqual(self.run_script('check_presentation.py', self.artifact, '--browser-report', report).returncode, 1)

    def test_explicit_alternative_is_distinguished_from_canvas(self):
        self.create()
        self.artifact.write_text('<html><body>Requested scroll report</body></html>')
        self.assertEqual(self.run_script('check_presentation.py', self.artifact, '--alternative-request', '').returncode, 1)
        self.assertEqual(self.run_script('check_presentation.py', self.artifact, '--alternative-request', 'Use a scroll report').returncode, 2)
        evidence = self.report()
        evidence.update(user_request='Use a scroll report', checks={'alternative_behavior': {'status': 'PASS', 'evidence': 'synthetic fixture'}})
        report = Path(self.tmp.name) / 'browser.json'
        report.write_text(json.dumps(evidence))
        result = self.run_script('check_presentation.py', self.artifact, '--alternative-request', 'Use a scroll report', '--browser-report', report)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('explicit alternative', result.stdout)
        self.assertEqual(self.run_script('check_presentation.py', self.artifact, '--alternative-request', 'Different request', '--browser-report', report).returncode, 1)
