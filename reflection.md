# Lab 5 — Reflection

**Student:** Pranav Hemanth  
**Date:** 31/10/25

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

- **Easiest:** style issues (PEP8 line length, whitespace, using f-strings) — these required only small text edits and are low risk.
- **Hardest:** security/injection issues (e.g., `subprocess` with `shell=True` or input validation) — these required reasoning about correct APIs, validating inputs, and sometimes restructuring code to avoid insecure patterns.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

- Example: Pylint flagged a function as unused even though it was dynamically imported or called via `getattr` at runtime. Static tools sometimes cannot see dynamic calls — I reviewed the code manually and confirmed it was used.

### 3. How would you integrate static analysis tools into an actual development workflow?

- Add Pylint/Flake8/Bandit to CI (GitHub Actions) to fail PRs when high-severity issues are introduced.
- Add pre-commit hooks (pre-commit framework) so developers run linters locally before commit.
- Use staged fixes for style automatically (`black` for formatting) while leaving security checks to CI for human review.

### 4. What tangible improvements did you observe after fixes?

- Fewer runtime exceptions in manual testing; clearer logging; fewer vague `except:` blocks; safer subprocess calls; improved readability via f-strings and consistent formatting — overall maintainability improved.
