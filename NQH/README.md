# Starter Vault — Second Brain NQH

Vault mẫu để bắt đầu trong 10 phút. (Đọc cẩm nang đầy đủ: [../01_Playbook.md](../01_Playbook.md))

## Quick-start
1. **Copy** cả thư mục này ra máy bạn, vd `~/Documents/MySecondBrain` (đổi tên tùy ý).
2. Mở **Obsidian** → *Open folder as vault* → trỏ vào thư mục vừa copy.
3. Cài plugin: **Dataview**, **Tasks** (bắt buộc); **Periodic Notes**, **Templater** (khuyến nghị).
4. Mở `07 - Maps of Content/Home.md` để bắt đầu.

## Dùng AI agent (tùy chọn)
Trong thư mục vault, mở agent đã được IT cấp:
- **Claude Code**: chạy `claude` → đăng nhập OAuth (license công ty). Thử lệnh `/daily`.
- **Kimi**: đặt `ANTHROPIC_BASE_URL` + key Moonshot rồi chạy `claude`.
- **OpenAI Codex / Gemini CLI**: đọc `AGENTS.md` / `GEMINI.md` (cùng nội dung với `CLAUDE.md`).

## Có sẵn trong vault
- Khung PARA (00–07), templates (Daily, Weekly, Meeting, Person, Project Brief).
- `Home` + `Dashboard` (Dataview tự gom task).
- `Projects.base` (Obsidian Bases).
- `.claude/` — file quy ước + lệnh `/daily` `/weekly` `/inbox` + hook git-safety.
- File quy ước AI: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` (giống nhau — sửa thì đồng bộ cả 3).

## An toàn
Không đưa dữ liệu mật NQH vào vault/AI chia sẻ. AI chỉ soạn nháp — bạn duyệt trước khi gửi. Xem `CLAUDE.md` mục AN TOÀN.
