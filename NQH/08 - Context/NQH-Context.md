---
tags: [context, nqh, reference]
updated: "2026-06-15"
---

# 🏢 NQH-Context — Bối cảnh tổ chức & quy ước nghiệp vụ

> AI đọc note này để hiểu môi trường làm việc của tôi và **tránh sai số khi làm báo cáo BGĐ**.

## NQ Holding (NQH)
Chuỗi F&B + hospitality tại Đà Lạt và Đắk Lắk. Tôi ([[Working-Preferences|Ngọc Thy]]) là trợ lý Ban Giám Đốc.

### Ban Giám Đốc tôi hỗ trợ trực tiếp
- [[Đặng Thế Tài]] — **Tổng Giám đốc Tập đoàn NQH**.
- [[Đặng Hoàng Anh]] — **Giám đốc Nhật Quang Đà Lạt (NQDL)**; đang lead dự án [[BU - Rex Kingdom]].
- Cả hai muốn báo cáo: **chi tiết · nêu rõ vấn đề · kèm phương án đề xuất**.

### Chi nhánh (dùng TÊN NỘI BỘ khi báo cáo)
| Tên nội bộ | Tên đầy đủ trong hệ thống | Ghi chú |
|------------|---------------------------|---------|
| **Buôn Kơ Lang (BKL)** | Buôn Kơ Lang | Chi nhánh chính |
| **Một Bữa Thơm (THƠM)** | Một Bữa Thơm | |
| **Trại Mèo Mướp (TMM)** | Ngôi Nhà Nhỏ Trên Thảo Nguyên | Đã đổi tên |
| **AirDream 1 (ADR1)** | AIR DREAM 3 BIS ĐỐNG ĐA | 3 bis Đống Đa, Đà Lạt |
| **AirDream 2 (ADR2)** | AIR DREAM 16HV | Forest Station |
| **Ther Cafe** | Ther Cafe | |
| **The Kupid** | The Kupid | Hotel + F&B |

## 📊 Nhịp báo cáo của tôi
- **Hằng ngày**: báo cáo công việc các Phòng ban/cơ sở.
- **Hằng tuần / hằng tháng**: báo cáo tổng hợp.
- **Theo mốc**: báo cáo dự án — [[BU - Pizza Gập]], [[BU - Cơm Mới]], [[BU - Rex Kingdom]], [[BU - Một Bữa Thơm]].
- **Khi cần**: báo cáo vấn đề phát sinh.
- Chi tiết & checklist: [[Báo cáo BGĐ]].

## 🔴 Quy ước nghiệp vụ — TUYỆT ĐỐI tuân thủ

### 1. Tuần làm việc NQH = Thứ 7 → Thứ 6 (Sat→Fri)
"Tuần này / tuần trước" mặc định tính theo **Thứ 7 đến Thứ Sáu tuần kế tiếp**, KHÔNG phải Mon–Sun. Khi tôi chỉ định ngày cụ thể ("từ 25/4 đến 1/5") thì dùng đúng ngày đó.

### 2. Đơn vị tiền — KHÔNG nhầm tỷ vs triệu
- `1.161.289.199đ` = **1,16 tỷ** (KHÔNG phải "1.161 tỷ").
- `344.313.998đ` = **344 triệu**.
- Số 7–9 chữ số → đọc bằng **triệu**; ≥10 chữ số → đọc bằng **tỷ**.
- Dấu `.` là phân cách hàng nghìn. Format tiền: `42.858.632đ`.
- Cross-check: tổng hệ thống NQH 1 tuần thường **1–5 tỷ**. Nếu báo cáo ra ">10 tỷ/tuần" → gần như chắc sai đơn vị, sửa lại.

### 3. Không tự cộng tay tổng số nhiều chữ số
LLM hay cộng sai. Dòng "TỔNG CỘNG" phải lấy từ một query tổng riêng, không cộng tay các dòng trên bảng.

## 🔴 Nguồn dữ liệu (quan trọng cho an toàn)
- Số liệu doanh thu **không lưu trong vault này** (dữ liệu mật + thay đổi realtime). Vault chỉ chứa báo cáo đã chốt / ghi chú, KHÔNG chứa dump dữ liệu thô.
- Nguồn chính thức: dashboard **baocao.nhatquangholding.com** và trợ lý dữ liệu **@bod** trên hệ thống MTClaw (qua Telegram). SSOT doanh thu = view `NQH.v_revenue_ssot`, cột `doanh_thu_official`.
- Khi cần số liệu: **luôn tra nguồn mới**, ghi rõ thời điểm tra. Không lấy lại số cũ trong hội thoại / note cũ rồi coi là hiện tại.

## Kho tri thức NQH (tham khảo, ngoài vault)
- **Hệ thống SOP NQH** đã clone ở thư mục anh em `../NQH-GROUP-SOP-SYSTEM/` (SOPs, training, BSC, JD…). Tra cứu khi cần quy trình/biểu mẫu chuẩn.
- **MTClaw** (`../MTClaw/`) — gateway AI đa kênh của NQH, chứa các SOUL agent (gồm @bod).
