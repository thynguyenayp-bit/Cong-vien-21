---
tags: [issue-report, sop, procurement]
date: 2026-08-19
status: open
type: issue-report
impact: Cao — ảnh hưởng khả năng cung ứng hàng thực phẩm hàng ngày cho 5 profit centers
---

# BC — Gap SOP P2P: Quy trình mua hàng thực phẩm không khả thi cho next-day delivery

> Báo cáo ngày 2026-08-19 — [[Dashboard]] · [[Home]] · [[Đặng Thế Tài]]

## Vấn đề

SOP P2P Master Process ([[NQH-HO-CGF-MP-001]] v1.1, hiệu lực 01/01/2026) thiết kế SLA cho mua hàng tổng quát (vật tư, dịch vụ, CapEx) với tổng thời gian **1–4 ngày**. Tuy nhiên, quy trình này đang được áp dụng cho **hàng thực phẩm tươi sống** — loại cần giao trong **≤ 8 tiếng** (tạo PR trước 5h chiều → hàng về sáng hôm sau).

Khoảng cách: SOP cần tối thiểu **16h+** (theo SLA thấp nhất), thực tế yêu cầu **≤ 8h**. Không có fast-track lane riêng cho perishable goods.

## Case minh hoạ (18/08/2026)

| Thời điểm | Sự kiện | Khoảng cách |
|-----------|---------|-------------|
| 16:25 | Bếp tạo PR | — |
| 18:16 | PR duyệt xong (bước cuối) | +1h51p ✅ đúng SLA |
| 19:20 | Chị Hồng tạo PO | +1h04p ✅ nhanh hơn SOP |
| 23:00 | KTT duyệt PO | **+3h40p** ⚠️ không có SLA |
| 23:00+ | Chị Hồng liên hệ NCC đặt hàng | — |

**Tổng: 6h35p.** Các bước có SLA chạy đúng hoặc nhanh hơn SOP. Bước KTT duyệt PO chiếm hơn 1/2 tổng thời gian nhưng **không có SLA** trong SOP → không có gì để breach → không auto-escalate. Phải có người can thiệp thủ công (gọi điện) mới xử lý được.

## Nguyên nhân gốc

1. **SOP "mù" với bước KTT duyệt PO** — không ghi SLA cho bước quyết định cuối cùng trước khi đặt hàng NCC. Tạo "black hole" không ai kiểm soát.
2. **Chuỗi duyệt PR phân tầng cộng dồn** — GM → OM → CEO theo hạn mức, SLA 4h–72h. Quá chậm cho hàng tươi sống cần đặt trong đêm giao ngay sáng hôm sau.
3. **Escalation thủ công, không phải system control** — chỉ hoạt động khi có người tự phát hiện và gọi điện. Ngày mai không có người đó → cùng kịch bản trễ hàng.

## Kiến nghị điều chỉnh

| # | Điều chỉnh | Mức ưu tiên |
|---|-----------|-------------|
| 1 | **Standing Approval / Blanket PO cho thực phẩm:** GM duyệt kế hoạch mua thực phẩm đầu tuần (danh mục + số lượng ước tính + NCC pre-approved + giá thoả thuận). Bếp order hàng ngày theo kế hoạch → không cần duyệt PR lại. Order vượt định mức hoặc ngoài kế hoạch → chạy quy trình duyệt bình thường. | 🔺 Cao |
| 2 | **Thêm SLA cho bước KTT duyệt PO:** tối đa **1h** cho thực phẩm, quá 1h → auto-escalate CEO | 🔺 Cao |
| 3 | **Auto-notification cho KTT** khi PO tạo + reminder mỗi 30 phút nếu chưa duyệt | ⏫ Trung bình |

> **Lưu ý:** Không áp dụng cơ chế "đặt trước duyệt sau" vì rủi ro tạo tiền lệ xấu (chi trước duyệt sau, khó kiểm soát gian lận). Kiểm soát nên tập trung ở **kế hoạch tuần** (duyệt 1 lần, giá trị lớn) thay vì **từng đơn nhỏ** (duyệt nhiều lần, giá trị nhỏ).

## Liên kết

- SOP tham chiếu: [[NQH-HO-CGF-MP-001_Purchase_to_Pay_Master_Process]]
- Người liên quan: [[Đặng Thế Tài]] · chị Hồng (mua hàng) · chị Vân (KTT)
- Báo cáo BGĐ: [[Báo cáo BGĐ]]
