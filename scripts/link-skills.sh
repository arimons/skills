#!/usr/bin/env bash
# 이 저장소의 skills/<스킬명>을 Codex(~/.agents/skills)와 Claude Code(~/.claude/skills)에 상대경로 심볼릭 링크로 연결한다.
# 스킬 목록은 skills/*/SKILL.md 를 찾아 자동으로 정하므로 따로 관리하지 않는다.
# 사용: scripts/link-skills.sh [--dry-run]
set -euo pipefail

DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
REPO="$(cd "$(dirname "$0")/.." && pwd)"
TARGETS=("$HOME/.claude/skills" "$HOME/.agents/skills")
STAMP="$(date +%Y%m%d-%H%M%S)"

run() { if [ "$DRY" = 1 ]; then echo "  (dry-run) $*"; else "$@"; fi; }

for T in "${TARGETS[@]}"; do
  echo "== $T"
  run mkdir -p "$T"
  T_REAL="$(cd "$T" 2>/dev/null && pwd -P || echo "$T")"
  for dir in "$REPO"/skills/*/; do
    [ -f "$dir/SKILL.md" ] || continue
    name="$(basename "$dir")"
    dest="$T/$name"
    rel="$(python3 -c 'import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))' "$REPO/skills/$name" "$T_REAL")"
    if [ -L "$dest" ]; then
      if [ "$(readlink "$dest")" = "$rel" ] && [ -e "$dest" ]; then echo "  유지  $name"; continue; fi
      run rm "$dest"
    elif [ -e "$dest" ]; then
      run mv "$dest" "$dest.bak-$STAMP"; echo "  백업  $name -> $name.bak-$STAMP"
    fi
    run ln -s "$rel" "$dest"; echo "  연결  $name -> $rel"
  done
  # 저장소를 가리키다 끊어진 링크는 알려만 준다(지우지 않는다)
  for l in "$T"/*; do
    [ -L "$l" ] && [ ! -e "$l" ] && echo "  [끊어진 링크] $l -> $(readlink "$l")"
  done || true
done
echo "끝. Claude Code와 Codex를 다시 시작하면 적용됩니다."
