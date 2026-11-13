import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("normalize.py")
SPEC = importlib.util.spec_from_file_location("port_validation_normalize", MODULE_PATH)
normalize_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(normalize_module)


class NormalizePathTest(unittest.TestCase):
    def test_removes_trailing_slashes_from_non_root_paths(self):
        self.assertEqual("docs", normalize_module.normalize_path("Docs/"))
        self.assertEqual("docs", normalize_module.normalize_path(" docs/// "))

    def test_preserves_existing_normalization_behavior(self):
        cases = {
            "/": "/",
            "/Docs/": "/docs",
            "Docs": "docs",
            "  Docs  ": "docs",
        }

        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(expected, normalize_module.normalize_path(path))


if __name__ == "__main__":
    unittest.main()
