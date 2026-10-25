# redrun-lab

A deliberately tiny Python package. Its only job is to produce **real** GitHub
Actions runs, green and then red, so that RedRun's evaluation set is built from
runs that actually happened instead of hand-written fixtures.

Each case is a branch with two commits: a green one, and then the breaking
commit. `main` is green and stays green.

| branch | what the breaking commit changes |
| --- | --- |
| `case/dep-bump-unpinned` | loosens a `packaging` pin, so a release that dropped `LegacyVersion` gets installed |
| `case/dep-bump-conflict` | pins `httpcore` to a version `httpx` cannot use: the resolver cannot build a set |
| `case/bad-commit-logic` | a shipping threshold comparison is inverted |
| `case/bad-commit-rename` | `format_total` is renamed where it is defined, not where it is imported |
| `case/flaky-coin` | an index build drops everything on a coin flip |
| `case/flaky-timing` | a cache warm gets a clock-dependent pause, and a test asserts on elapsed time |
| `case/secret-missing` | the workflow starts requiring a repository secret that was never set |
| `case/secret-invalid` | the workflow sends a token that is not valid, and the API answers 401 |
| `case/config-python` | the workflow drops the Python version below what the code needs |
| `case/config-env` | the workflow renames the env var a step reads |
| `case/bad-commit-syntax` | a loop header loses its colon |
| `case/config-working-directory` | the install step is pointed at a directory without the manifest |

No real credential is stored in this repository. The only value ever set as a
repository secret here is a deliberately invalid token.
