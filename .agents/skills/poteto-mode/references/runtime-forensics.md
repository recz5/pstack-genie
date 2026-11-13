# Runtime forensics

Use this playbook when a symptom must be observed in a currently running process, such as CPU spin, memory growth, blocking, or a visual glitch. The deliverable is a cited diagnosis, not a fix.

1. Define the symptom, affected process, observation window, and a falsifiable diagnosis criterion.
2. Inventory the runtime tools and permissions actually available. Prefer passive, read-only observation. Ask for explicit approval before attaching invasive tooling, changing runtime state, injecting code, restarting a process, or capturing sensitive data.
3. Capture a real signal on the matching surface: a CPU profile for spin, a heap snapshot or allocation profile for growth, thread or wait evidence for blocking, or an authorized trace for a visual glitch. Record the artifact path, capture conditions, and time window.
4. Reduce the artifact to the smallest relevant finding: a hot path, retainer chain to a root, blocked thread and wait reason, or loop firing without input. Use native parallel or delegated analysis only when the runtime exposes it; otherwise reduce large artifacts sequentially without flooding the working context.
5. Test the mechanism with the least invasive authorized observation that can distinguish the hypothesis from alternatives. Do not hot-patch or mutate a live process merely to prove a theory.
6. Map the finding to source file, symbol, and line when the evidence supports it. If symbols or source mappings are missing, state that attribution remains incomplete.
7. Report the signal, capture conditions, reduced finding, mechanism evidence, source attribution, artifact paths, and confidence. Do not implement a fix unless asked; hand a confirmed cause to Bug fix or Performance.

If no suitable capture tool or permission exists, report the exact evidence gap and the safest next capture rather than theorizing from source alone.
