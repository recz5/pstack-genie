from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GitHubRepositoryTests(unittest.TestCase):
    def test_github_actions_workflow_exists(self):
        workflow = ROOT / '.github/workflows/validate.yml'
        self.assertTrue(workflow.is_file())
        self.assertIn('permissions:', workflow.read_text())
        self.assertIn('contents: read', workflow.read_text())

    def test_no_gitlab_ci_configuration(self):
        self.assertFalse((ROOT / '.gitlab-ci.yml').exists())

    def test_documentation_references_github(self):
        self.assertIn('GitHub', (ROOT / 'README.md').read_text())
        self.assertIn('GitHub', (ROOT / 'PUBLIC_RELEASE_CHECKLIST.md').read_text())
        self.assertNotIn('GitLab', (ROOT / 'README.md').read_text())
        self.assertNotIn('GitLab', (ROOT / 'PUBLIC_RELEASE_CHECKLIST.md').read_text())


if __name__ == '__main__':
    unittest.main()
