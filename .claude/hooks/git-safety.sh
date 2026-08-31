#!/usr/bin/env bash
# git-safety hook — chạy trước mỗi lệnh Bash của AI trong vault này.
# Nhiệm vụ: cảnh báo nếu đang ở nhánh main / có thay đổi chưa commit.

set -euo pipefail

# Chỉ chạy khi trong một git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    exit 0
fi

BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "unknown")

# Cảnh báo nếu đang ở nhánh main
if [[ "$BRANCH" == "main" || "$BRANCH" == "master" ]]; then
    echo "⚠️  CẢNH BÁO: Bạn đang ở nhánh '$BRANCH'."
    echo "    Quy tắc NQH: không push thẳng main. Hãy tạo nhánh + Pull Request."
    echo "    Gợi ý: git checkout -b feature/ten-nhanh"
    exit 1
fi

# Cảnh báo nếu có thay đổi chưa commit (uncommitted changes)
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "⚠️  CẢNH BÁO: Có thay đổi chưa commit trong working tree."
    echo "    Hãy xem lại bằng git diff và commit trước khi tiếp tục."
    exit 1
fi

exit 0
