#!/usr/bin/env bash
set -euo pipefail
# This runs a DISTRIBUTED OFFICIAL FOUNDATION v14 TUTORIAL unchanged.
# It checks the installation, NOT jet heat transfer or H100 compatibility.
if [[ ! -f /opt/openfoam14/etc/bashrc ]]; then
  echo 'BLOCKED: OpenFOAM Foundation v14 not installed at /opt/openfoam14' >&2;exit 2
fi
set +u
source /opt/openfoam14/etc/bashrc
set -u
: "${FOAM_TUTORIALS:?OpenFOAM environment lacks FOAM_TUTORIALS}"
for exe in foamRun blockMesh checkMesh foamVersion;do
 command -v "$exe" >/dev/null || { echo "BLOCKED: missing $exe" >&2;exit 2; }
done
SRC="$FOAM_TUTORIALS/incompressibleFluid/pitzDailySteady"
[[ -d "$SRC" ]] || { echo "BLOCKED: official v14 tutorial not found: $SRC" >&2;exit 2; }
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
DEST="$HERE/cfd/runs/tutorial_pitzDailySteady"
[[ ! -e "$DEST" ]] || { echo "Run output exists at $DEST; remove it manually before rerunning" >&2;exit 2; }
mkdir -p "$(dirname "$DEST")"
cp -a "$SRC" "$DEST"
cd "$DEST"
foamVersion > log.foamVersion 2>&1
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
foamRun > log.foamRun 2>&1
if ! grep -q '^End' log.foamRun;then echo 'Solver output did not record normal End; inspect log.foamRun' >&2;exit 2;fi
printf '%s\n' 'COMPLETED: official OpenFOAM v14 backward-facing-step tutorial.'
printf '%s\n' 'NOT A JET COOLING CASE. Inspect mesh, residuals and continuity in logs.'
printf '%s\n' "Files: $DEST"
