"""Offline smoke checks for copied runtime resources; no service calls or downloads."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SKILLS = Path(__file__).resolve().parents[1] / 'plugins/html-briefing/skills'


class BundledRuntimes(unittest.TestCase):
    def test_ui_reference_database_search(self):
        result = subprocess.run([sys.executable, str(SKILLS / 'ui-ux-pro-max/scripts/search.py'),
                                 'comparison', '--domain', 'chart', '--json'],
                                capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        self.assertGreater(data['count'], 0)
        self.assertEqual(data['domain'], 'chart')

    def test_browser_wrapper_preserves_arguments(self):
        with tempfile.TemporaryDirectory() as tmp:
            executable = Path(tmp) / 'npx'
            executable.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
            executable.chmod(0o755)
            env = dict(os.environ, PATH=tmp + os.pathsep + os.environ.get('PATH', ''),
                       PLAYWRIGHT_CLI_SESSION='package-check')
            result = subprocess.run(['/bin/bash', str(SKILLS / 'playwright/scripts/playwright_cli.sh'), '--help'],
                                    env=env, capture_output=True, text=True, check=True)
            self.assertEqual(result.stdout.splitlines(), ['--yes', '--package', '@playwright/cli',
                              'playwright-cli', '--session', 'package-check', '--help'])


if __name__ == '__main__':
    unittest.main()
