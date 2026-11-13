import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_repo import validate_skills  # noqa: E402


class SkillTests(unittest.TestCase):
    def test_active_skills_validate(self):
        self.assertEqual(validate_skills(), [])

    def test_only_poteto_skill_is_installed(self):
        skills = ROOT / '.agents/skills'
        self.assertEqual(sorted(p.name for p in skills.iterdir() if (p / 'SKILL.md').is_file()), ['poteto-mode'])

    def test_poteto_is_general_purpose_with_conditional_databricks_references(self):
        mode = (ROOT / '.agents/skills/poteto-mode/SKILL.md').read_text()
        self.assertIn('general-purpose', mode.lower())
        self.assertIn('references/databricks.md', mode)
        self.assertIn('For unrelated tasks', mode)
        self.assertTrue((ROOT / '.agents/skills/poteto-mode/references/databricks-data-modeling.md').is_file())
        self.assertTrue((ROOT / '.agents/skills/poteto-mode/references/databricks-pipeline-quality.md').is_file())
        self.assertTrue((ROOT / '.agents/skills/poteto-mode/references/databricks-deployment-safety.md').is_file())
        self.assertFalse((ROOT / '.agents/skills/databricks-architect').exists())

    def test_readme_shows_one_mode(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('one entry point', readme.lower())
        self.assertNotIn('@databricks-architect', readme)

    def test_portability_does_not_assume_cursor_subagents(self):
        mode = (ROOT / '.agents/skills/poteto-mode/references/runtime.md').read_text()
        self.assertIn('not portable', mode)
        self.assertIn('Do not', mode)

    def test_tdd_workflow_requires_failing_before_passing_after(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/tdd.md').read_text()
        self.assertLess(workflow.index('before changing production code'), workflow.index('smallest production change'))
        self.assertIn('confirm it fails for the intended reason', workflow)
        self.assertIn('failing-before evidence, passing-after evidence', workflow)
        self.assertIn('do not add a bad test', workflow)

    def test_multi_phase_plan_is_plan_only_and_evidence_driven(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/multi-phase-plan.md').read_text()
        self.assertIn('The plan is the deliverable', workflow)
        self.assertIn("Do not implement it until the user explicitly asks execution to begin", workflow)
        for requirement in ('dependencies', 'behavioral verification', 'rollback path', 'completion evidence'):
            self.assertIn(requirement, workflow)
        self.assertIn("Execution begins only on the user's explicit go", workflow)

    def test_pause_safely_is_explicit_and_has_no_implicit_publication(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/pause-safely.md').read_text()
        self.assertIn('only when the user explicitly asks', workflow)
        self.assertIn('Do not commit, push, open a pull request, deploy, or publish', workflow)
        for checkpoint_field in ('original intent', 'verification evidence', 'remaining steps', 'first action on resume'):
            self.assertIn(checkpoint_field, workflow)

    def test_internal_workflows_are_routed_without_new_skills(self):
        routing = (ROOT / '.agents/skills/poteto-mode/references/routing.md').read_text()
        for reference in ('tdd.md', 'multi-phase-plan.md', 'pause-safely.md', 'runtime-forensics.md', 'trace-forensics.md', 'figure-it-out.md'):
            self.assertIn(reference, routing)
        skills = ROOT / '.agents/skills'
        self.assertEqual(sorted(p.name for p in skills.iterdir() if (p / 'SKILL.md').is_file()), ['poteto-mode'])

    def test_runtime_forensics_requires_live_evidence_and_safe_authorization(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/runtime-forensics.md').read_text()
        self.assertIn('currently running process', workflow)
        self.assertIn('Capture a real signal', workflow)
        self.assertIn('explicit approval', workflow)
        self.assertIn('Do not hot-patch', workflow)
        self.assertIn('diagnosis, not a fix', workflow)

    def test_trace_forensics_treats_capture_as_fixed_untrusted_data(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/trace-forensics.md').read_text()
        self.assertIn('fixed dataset', workflow)
        self.assertIn('untrusted input', workflow)
        self.assertIn('bounded, queryable representation', workflow)
        self.assertIn('without explicit authorization', workflow)
        self.assertIn('strongest hypothesis', workflow)

    def test_figure_it_out_is_auditable_without_implicit_publication(self):
        workflow = (ROOT / '.agents/skills/poteto-mode/references/figure-it-out.md').read_text()
        self.assertIn('falsifiable definition of done', workflow)
        self.assertIn('ordered phase list before code', workflow)
        for verdict in ('VERIFIED', 'NOT VERIFIED', 'INCONCLUSIVE'):
            self.assertIn(verdict, workflow)
        self.assertIn('local decision trail', workflow)
        self.assertIn('Do not commit, push, publish', workflow)

    def test_batch_3_orchestration_workflows_are_portable_and_routed(self):
        routing = (ROOT / '.agents/skills/poteto-mode/references/routing.md').read_text()
        expected = {
            'autonomous-run.md': ('checkable exit predicate', 'never pretend a background loop is armed'),
            'hillclimb.md': ('freeze the harness', 'Keep a candidate only when improvement clears observed noise'),
            'orchestrate.md': ('If no authorized worker mechanism exists', 'worker summary or green status alone is not a verdict'),
        }

        for filename, requirements in expected.items():
            self.assertIn(f']({filename})', routing)
            workflow = (ROOT / f'.agents/skills/poteto-mode/references/{filename}').read_text()
            for requirement in requirements:
                self.assertIn(requirement, workflow)

        autonomous = (ROOT / '.agents/skills/poteto-mode/references/autonomous-run.md').read_text()
        self.assertIn('Do not create commits unless the user explicitly requested them', autonomous)
        hillclimb = (ROOT / '.agents/skills/poteto-mode/references/hillclimb.md').read_text()
        self.assertIn('Do not commit, push, open a pull request, deploy, or publish', hillclimb)
        for workflow in (autonomous, hillclimb):
            self.assertIn('[Show me your work](show-me-your-work.md)', workflow)
            self.assertIn('canonical TSV columns', workflow)
        orchestrate = (ROOT / '.agents/skills/poteto-mode/references/orchestrate.md').read_text()
        self.assertIn('remain separately approval-gated', orchestrate)

    def test_batch_3_review_and_decision_trail_workflows_are_portable_and_routed(self):
        routing = (ROOT / '.agents/skills/poteto-mode/references/routing.md').read_text()
        for reference in ('interrogate.md', 'show-me-your-work.md', 'orchestrate.md'):
            self.assertIn(f']({reference})', routing)

        interrogate = (ROOT / '.agents/skills/poteto-mode/references/interrogate.md').read_text()
        self.assertIn('Findings survive only when reproduced', interrogate)
        self.assertIn('Otherwise run the adversarial lenses sequentially', interrogate)
        self.assertIn('do not apply fixes', interrogate)
        self.assertIn('No verified findings is a valid result', interrogate)

        trail = (ROOT / '.agents/skills/poteto-mode/references/show-me-your-work.md').read_text()
        self.assertIn('append-only TSV log', trail)
        self.assertIn('ts\\tphase\\tdecision\\twhy\\tevidence\\tresult', trail)
        self.assertIn('prevent spreadsheet formula execution', trail)
        self.assertIn('Do not commit, push, publish, or upload it', trail)
        self.assertIn('never invent a reviewer or model name', trail)


if __name__ == '__main__':
    unittest.main()
