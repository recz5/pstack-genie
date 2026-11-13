import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from import_upstream import vendor_from_checkout  # noqa: E402


class ImportTests(unittest.TestCase):
    def test_vendoring_preserves_upstream_and_requires_license(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            original = p / 'checkout/pstack'
            (original / 'skills/poteto-mode').mkdir(parents=True)
            (original / 'skills/poteto-mode/SKILL.md').write_text('upstream skill', encoding='utf-8')
            (original / 'LICENSE').write_text('MIT License', encoding='utf-8')
            dest = p / 'vendor/pstack'
            vendor_from_checkout(p / 'checkout', dest, revision='fixture-sha')
            self.assertEqual((dest / 'skills/poteto-mode/SKILL.md').read_text(), 'upstream skill')
            self.assertIn('fixture-sha', (p / 'vendor/UPSTREAM.txt').read_text())
            with self.assertRaises(RuntimeError):
                vendor_from_checkout(p / 'checkout', dest, revision='fixture-sha')

    def test_rejects_unlicensed_checkout(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            file = p / 'checkout/pstack/skills/poteto-mode/SKILL.md'
            file.parent.mkdir(parents=True)
            file.write_text('upstream skill', encoding='utf-8')
            with self.assertRaisesRegex(RuntimeError, 'LICENSE missing'):
                vendor_from_checkout(p / 'checkout', p / 'dest/pstack')


if __name__ == '__main__':
    unittest.main()
