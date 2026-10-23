# GitHub publishing instructions

Recommend a **private** repository named `h100-jet-impingement-cfd`. Do not upload journal PDFs, university-confidential work, proprietary H100/OEM drawings, passwords, API keys, or patent-sensitive designs without permission.

Create an empty repository on GitHub (no starter README, no new .gitignore, no new license), then run from the extracted project root:

```bash
git init -b main
git add .
git commit -m "Add source-checked H100 jet cooling project scaffold"
git remote add origin https://github.com/YOUR_USERNAME/h100-jet-impingement-cfd.git
git push -u origin main
```

Authenticate using your normal approved GitHub workflow; never save passwords or access tokens in repository files. If using GitHub Desktop, use **File → Add local repository** and publish privately.

After upload:
1. Verify the **Actions** workflow (six Python unit tests) completes.
2. Select **Code → Codespaces → Create codespace on main**.
3. During initial launch, Codespaces attempts to build the experimental `.devcontainer/Dockerfile` with OpenFOAM Foundation 14; if installation fails, examine the build log and official documentation. Its build was not verified in the environment where this starter was authored.
4. In Codespaces terminal, run `bash scripts/check_openfoam_install.sh`.
5. Only after that follow `docs/OPENFOAM_SETUP.md` and `docs/CFD_VALIDATION_PLAN.md`.

GitHub does not automatically simulate CFD. Codespaces uses billed/limited cloud CPUs, and computationally demanding cases are usually better placed on a lab workstation or HPC cluster. Do **not** put full OpenFOAM solutions or large mesh binary files into ordinary Git commits.
