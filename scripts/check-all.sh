#!/usr/bin/env bash
# Run what CI runs, in the same order. The one command before opening a PR.
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n== %s\n' "$1"; }

step "Hygiene"
bash scripts/check-hygiene.sh

step "DCO sign-off on commits not yet on main"
base=$(git merge-base HEAD origin/main 2>/dev/null || git rev-list --max-parents=0 HEAD 2>/dev/null | tail -1 || true)
missing=0
if [ -n "${base:-}" ]; then
  while IFS= read -r sha; do
    if ! git log -1 --format=%B "$sha" | grep -q '^Signed-off-by: .* <.*>'; then
      echo "missing Signed-off-by: $(git log -1 --format='%h %s' "$sha")"; missing=1
    fi
  done < <(git rev-list "$base"..HEAD 2>/dev/null)
fi
[ "$missing" -eq 0 ] && echo "DCO: all commits signed off" || exit 1

step "Case-set structure"
python3 scripts/check-cases.py

printf '\nAll gates green.\n'
