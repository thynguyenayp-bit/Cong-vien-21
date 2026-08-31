#!/usr/bin/env bash
# Chặn push thẳng main/master. (PreToolUse:Bash)
input=$(cat)
cmd=$(printf '%s' "$input" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('tool_input',{}).get('command',''))" 2>/dev/null)
if printf '%s' "$cmd" | grep -Eiq 'git[[:space:]]+(-C[[:space:]]+[^[:space:]]+[[:space:]]+)?push([[:space:]]|$)' \
   && printf '%s' "$cmd" | grep -Eiq '(^|[[:space:]/])(main|master)([[:space:]]|$|:)'; then
  echo "🚫 BỊ CHẶN: không push thẳng main/master. Tạo nhánh + PR." >&2
  exit 2
fi
exit 0
