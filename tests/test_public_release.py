import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_public_release import check_public_release  # noqa: E402


class PublicReleaseTests(unittest.TestCase):
    def test_starter_has_no_obvious_secrets(self):
        self.assertEqual(check_public_release(), [])

    def test_rejects_sensitive_file_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.env').write_text('SECRET=value')
            self.assertTrue(check_public_release(root))

    def test_detects_private_key_marker_without_leaking_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'bad.txt').write_text('-----BEGIN PRIVATE KEY-----\ncontent\n')
            problems = check_public_release(root)
            self.assertTrue(problems)
            self.assertNotIn('content', str(problems))


if __name__ == '__main__':
    unittest.main()
