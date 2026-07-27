---
name: Python dependency installs
description: Environment-specific caution when installing Python packages in imported projects
---

When installing Python dependencies with the managed package installer, verify the tracked requirements file immediately afterward; the installer may run an automatic freeze step that duplicates or rewrites the file unexpectedly.

**Why:** A package install can succeed while the post-install freeze leaves the project with an invalid or duplicated requirements file.

**How to apply:** Restore the intended pinned requirements content before running migrations or committing setup changes, then verify with a clean package-file diff.