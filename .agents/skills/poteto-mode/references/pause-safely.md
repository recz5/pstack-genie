# Pause-safely workflow

Use this workflow only when the user explicitly asks to pause, stop, or leave a resumable checkpoint. Requests to keep going are not pause requests.

1. Stop at a safe boundary. Finish or safely back out of the current atomic step, start nothing new, and stop any owned background work when the runtime supports it.
2. Take no irreversible or external action merely to create a checkpoint. Do not commit, push, open a pull request, deploy, or publish unless the user separately requested and authorized that action.
3. Preserve completed edits on disk and inspect the worktree state. Do not discard or overwrite pre-existing user changes.
4. Create a concise resume note when a durable checkpoint is useful. Put it at the user's requested path, otherwise use a clearly named workspace or temporary file permitted by the runtime.
5. Record the original intent, completed work, verification evidence, current state, remaining steps, key paths, blockers, risks, and the first action on resume. Distinguish facts saved on disk from context that exists only in the note.
6. Reply with the checkpoint path, worktree state, background-work state, what remains unverified, and the first resume action. Make clear that this is a pause, not a completion report.
