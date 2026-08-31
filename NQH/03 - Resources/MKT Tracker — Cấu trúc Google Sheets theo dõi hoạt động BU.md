---
tags: [resource, mkt, tracker, template]
updated: "2026-07-04"
---

# 📊 MKT Tracker — Cấu trúc Google Sheets theo dõi hoạt động tất cả BU

> Template thiết kế cho NQH. Người xem: [[Working-Preferences|Thy]] (tổng hợp). Người nhập: Team MKT. Setup 1 lần, dùng hàng tuần.

---

## 🗂️ Cấu trúc file (6 tab)

| Tab | Ai nhập | Mục đích |
|-----|---------|----------|
| 📊 **Dashboard** | Auto | Thy xem tổng quan, không nhập tay |
| 📱 **Social** | Team MKT | Theo dõi bài đăng + hiệu quả hàng ngày |
| 💰 **Ads** | Team MKT | Chi tiêu + hiệu quả quảng cáo |
| ⭐ **KOL/KOC** | Team MKT | Quản lý booking + kết quả |
| 🌱 **Seeding** | Team MKT | Ghi nhận hoạt động seeding |
| 📍 **Google Review** | MKT + BU | Theo dõi đánh giá + chiến dịch đẩy review |

---

## Danh sách BU (dropdown dùng chung)
`BKL · TMM · AirDream 1 · AirDream 2 · Kupid · Pizza Gập · Thơm · Cafe Thơm · Rex · Cơm Mới`

---

## 📱 TAB 1 — Social

**Nhịp nhập:** Cuối mỗi ngày hoặc đầu giờ sáng hôm sau.

| Cột                  | Nội dung                          | Ghi chú                       |
| -------------------- | --------------------------------- | ----------------------------- |
| Ngày                 | DD/MM/YYYY                        |                               |
| Tuần                 | =WEEKNUM() hoặc nhập tay          | Dùng để pivot                 |
| BU                   | Dropdown                          |                               |
| Platform             | Facebook / Instagram / TikTok     |                               |
| Loại content         | Ảnh / Video / Reel / Story / Live |                               |
| Tóm tắt nội dung     | 1 dòng mô tả                      | Ví dụ: "Combo cuối tuần Thơm" |
| Link bài đăng        | URL                               |                               |
| **Số bài KH (tuần)** | Kế hoạch đầu tuần                 | Điền 1 lần đầu tuần           |
| **Số bài TH**        | Thực hiện                         | Cập nhật khi đăng             |
| **Reach KH**         | Mục tiêu reach                    |                               |
| **Reach TH**         | Số thực tế (lấy từ Insights)      |                               |
| **Tương tác KH**     | Mục tiêu                          | Like+Comment+Share            |
| **Tương tác TH**     | Thực tế                           |                               |
| Followers đầu tuần   | Snapshot T2                       |                               |
| Followers cuối tuần  | Snapshot CN                       |                               |
| Ghi chú              | Lý do chênh lệch, ý kiến          |                               |

> **Cột % đạt** (auto): =TH/KH — format màu: <70% đỏ · 70–90% vàng · >90% xanh

---

## 💰 TAB 2 — Ads

**Nhịp nhập:** Hàng ngày hoặc cuối tuần tổng hợp.

| Cột | Nội dung | Ghi chú |
|-----|----------|---------|
| Ngày / Tuần | | |
| BU | Dropdown | |
| Platform | Facebook Ads / Google Ads / TikTok Ads / Zalo Ads | |
| Tên chiến dịch | | |
| Mục tiêu | Awareness / Traffic / Reach / Conversion / Lead | |
| **Ngân sách KH (đ/ngày)** | | |
| **Chi tiêu TH** | Lấy từ Ads Manager | |
| Reach | | |
| Impressions | | |
| CPM (đ) | =Chi tiêu/Impressions×1000 | |
| Clicks | | |
| CPC (đ) | =Chi tiêu/Clicks | |
| Chuyển đổi | Đặt bàn / Gọi điện / Nhắn tin / Đặt phòng | Tùy BU |
| CPR — Chi phí/kết quả | =Chi tiêu/Chuyển đổi | |
| Trạng thái | Đang chạy / Tạm dừng / Kết thúc | |
| Ghi chú | | |

---

## ⭐ TAB 3 — KOL/KOC

**Nhịp nhập:** Mỗi khi có booking mới hoặc bài lên sóng.

| Cột | Nội dung | Ghi chú |
|-----|----------|---------|
| BU | Dropdown | |
| Tên KOL/KOC | | |
| Phân loại | KOL / KOC / Micro (<100k) / Nano (<10k) | |
| Platform | | |
| Số followers | | |
| Hình thức | Bài đăng / Story / Reel / Video dài / Combo | |
| Nội dung cam kết | Mô tả ngắn | |
| **Chi phí (đ)** | | |
| Ngày booking | | |
| Ngày đăng dự kiến | | |
| Ngày đăng thực tế | | |
| Link bài đăng | | |
| Reach thực tế | Lấy từ KOL báo cáo hoặc xem trực tiếp | |
| Tương tác thực tế | Like + Comment + Share | |
| Đã thanh toán? | Có / Chưa / Đặt cọc | |
| Hiệu quả | Tốt / Trung bình / Kém | Đánh giá sau 3 ngày |
| Có tái hợp tác? | Có / Không / Cân nhắc | |
| Ghi chú | | |

---

## 🌱 TAB 4 — Seeding

**Nhịp nhập:** Ngay sau khi seeding.

| Cột | Nội dung | Ghi chú |
|-----|----------|---------|
| Ngày | | |
| Tuần | | |
| BU | Dropdown | |
| Kênh / Nền tảng | Facebook Group / Zalo Group / TikTok / Forum / Reddit VN... | |
| Tên nhóm / diễn đàn | | |
| Quy mô nhóm | Số thành viên (nếu biết) | |
| **Số bài KH (tuần)** | | |
| **Số bài TH** | | |
| Tóm tắt nội dung | | |
| Phản hồi | Like / Comment / Share nhận được | |
| Có bị xóa/ban? | Có / Không | |
| Hiệu quả | Tốt / TB / Kém | |
| Ghi chú | | |

---

## 📍 TAB 5 — Google Review

**Nhịp nhập:** Cuối mỗi tuần.

| Cột | Nội dung | Ghi chú |
|-----|----------|---------|
| Tuần | | |
| BU | Dropdown | |
| Link Google Maps | | |
| **Rating đầu tuần** | Snapshot T2 | |
| **Rating cuối tuần** | Snapshot CN | |
| Tổng số review (hiện tại) | | |
| **Review mới trong tuần KH** | Mục tiêu | |
| **Review mới trong tuần TH** | Thực tế | |
| Review 4–5 sao (mới) | | |
| Review 1–3 sao (mới) | | |
| Đã phản hồi review xấu? | Có / Chưa / Không cần | |
| Phương pháp đẩy review tuần này | QR tại bàn / Nhắc trực tiếp / Zalo / Bao bì / Khác | |
| Ghi chú | Nội dung review xấu đáng chú ý | |

---

## 📊 TAB 6 — Dashboard (cấu trúc)

> Dùng QUERY hoặc PIVOT TABLE từ 5 tab trên. Thy xem, không cần nhập.

### Bảng 1 — Tổng hợp tuần hiện tại
| BU | Social (bài TH/KH) | Ads (chi tiêu TH/KH) | KOL (số) | Seeding (bài) | Rating Google |
|----|--------------------|----------------------|----------|---------------|---------------|
| BKL | | | | | |
| TMM | | | | | |
| ... | | | | | |

### Bảng 2 — Hiệu quả Social (reach & tương tác)
| BU | Platform | Reach TH | Reach KH | % đạt | Tương tác TH | Tương tác KH | % đạt |
|----|----------|----------|----------|-------|--------------|--------------|-------|

### Bảng 3 — Hiệu quả Ads
| BU | Chi tiêu TH | CPM | CPC | Chuyển đổi | CPR |
|----|-------------|-----|-----|------------|-----|

### Indicator màu (conditional formatting toàn Dashboard)
- 🟢 ≥ 90% kế hoạch
- 🟡 70–89%
- 🔴 < 70%

---

## 📌 Quy ước nhập liệu (gửi team MKT)

1. **Nhập số thực tế**, không làm tròn lên.
2. Nếu chưa có số → để trống, **không điền 0** (0 ≠ chưa có data).
3. **Deadline nhập:** Social + Seeding → trước 9h sáng hôm sau. Ads → cuối tuần (CN). KOL/KOC → ngay khi bài lên sóng.
4. Cột màu đỏ = bắt buộc nhập. Cột màu xám = optional.
5. **Ghi chú** khi TH < 70% KH — lý do ngắn gọn.

---

## 🔗 Liên kết vault
- Tổng việc MKT đang theo dõi: [[Bảng điều hành công việc]]
- BU cụ thể: [[BU - Cơm Mới]] · [[BU - Rex Kingdom]] · [[BU - Trại Mèo Mướp]] · [[BU - The Kupid]]
