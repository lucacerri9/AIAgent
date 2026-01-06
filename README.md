# Agentic Code Debugger

An “agentic” code debugger using an LLM to analyze a codebase, run commands, and iteratively fix bugs or implement small changes.

*** This project is for learning and experimentation only. Do not point it at sensitive codebases or production environments.
---

# Features
- Analyzes Python codebases with an LLM
- Proposes and applies fixes to failing tests or obvious bugs
- Can run commands (e.g. 'pytest', 'python main.py`, etc.)
- Iterative “plan -> act -> observe -> refine” loop
- Configurable model, prompts, and tools

---

# How It Works

At a high level:

1. **Context building**
   - Collects information about the codebase (e.g. files, errors, test output).
2. **Planning**
   - Asks the LLM to decide what to do next (inspect a file, run tests, edit a file, etc.).
3. **Tool use**
   - The agent can call tools you define, such as:
     - 'run_command' – runs shell commands
     - 'read_file' / 'write_file' – inspects or edits code
4. **Iteration**
   - Repeats the loop until tests pass, a goal is reached, or a max-steps limit is hit.

---
