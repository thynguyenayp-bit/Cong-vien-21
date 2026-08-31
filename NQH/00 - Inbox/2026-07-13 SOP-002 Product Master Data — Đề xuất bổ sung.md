---
tags: [SOP, master-data, product, amendment, review]
date: 2026-07-13
status: draft
ref-sop: NQDL-MDP-SOP-002_Product_Master_Data_Management v1.1
---

# Đề xuất bổ sung — NQDL-MDP-SOP-002 (Product Master Data)

> Review ngày 13/07/2026 — đối chiếu cấu trúc category/subcategory với mô hình thực tế các cơ sở NQH hiện tại và sắp mở.
> Tài liệu này là **đề xuất nội bộ**, chưa chỉnh SOP gốc. Cần phê duyệt CEO/CFO trước khi update chính thức.

---

## Tóm tắt vấn đề

| #   | Phần              | Vấn đề                                                  | Ưu tiên            |
| --- | ----------------- | ------------------------------------------------------- | ------------------ |
| 1   | §4.1 BU           | AIR gộp AD1 + AD2 — 2 địa điểm khác nhau                | 🔴 Cao             |
| 2   | §4.1 BU           | PZG (Pizza Gập) thiếu hoàn toàn                         | 🔴 Cao             |
| 3   | §4.2 Sub-brand    | MBC đang có ĐKĐKD riêng → cần nâng thành BU             | 🔴 Cao             |
| 4   | §4.4 Sub-category | SVC không có subcategory — không phân tích được         | 🟡 Trung bình      |
| 5   | §4.4 Sub-category | ROM không có subcategory — Kupid không tính được RevPAR | 🟡 Trung bình      |
| 6   | §4.4 FOD          | Sub-category generic, không fit menu Tây Nguyên BKL     | 🟡 Trung bình      |
| 7   | §7 KPIs           | Food Cost BKL mâu thuẫn: SOP-002 ghi 25–28%, FB-SOP-001 ghi 32–35% | 🟡 Trung bình |
| 8   | §4.1 BU           | REX Kingdom chưa có                                     | 🟢 Thấp (chuẩn bị) |
| 9   | §4.4 BEV          | ALC chỉ BKL+THOM — cần xem KUP mini-bar                 | 🟢 Thấp            |

---

## 1. Đề xuất — §4.1 Đơn vị Kinh doanh

> [!warning] Migration cần thiết
> Tách `AIR` → `AD1` + `AD2` là breaking change với CukCuk POS và field `primary_bu` trong toàn bộ database. Cần IT kiểm kê 35 SKU hiện có của AIR và phân bổ trước khi áp dụng.

**Bảng thay thế (§4.1):**

| Mã      | Tên đầy đủ                    | Loại hình                | Trạng thái                        |
| ------- | ----------------------------- | ------------------------ | --------------------------------- |
| ~~AIR~~ | ~~AirDream Cafe~~             | ~~Cà phê ngoài trời~~    | Deprecated — tách thành AD1 + AD2 |
| AD1     | AirDream 1 — Đống Đa          | Cà phê ngoài trời        | Tạm ngưng (thi công đường)        |
| AD2     | AirDream Forest Station (AFS) | Cà phê + không gian rừng | Hoạt động                         |
| KUP     | Kupid Homestay                | Lưu trú + F&B            | Hoạt động                         |
| THOM    | Nhà Hàng & Cà Phê Thơm        | Ẩm thực Việt + Cà phê    | Hoạt động                         |
| BKL     | Buôn Kơ Lang                  | BBQ + ẩm thực Tây Nguyên | Hoạt động                         |
| TMM     | Trại Mèo Mướp                 | Du lịch nông nghiệp      | Hoạt động                         |
| PZG     | Pizza Gập (tại AFS/AD2)       | Pizza F&B                | Hoạt động                         |
| COM     | Mâm Cơm                       | Cơm Việt, bữa trưa       | Pending ĐKĐKD                     |
| REX     | Rex Kingdom                   | Du lịch sinh thái + F&B  | Mở 15/08/2026 (có thể trễ)        |
|         |                               |                          |                                   |

---

## 2. Đề xuất — §4.2 Sub-brand

> [!info] MBC → COM
> Mâm Cơm đang tiến hành ĐKĐKD riêng (giao ban 13/07/2026). Khi hoàn thành → `MBC` nâng thành BU `COM`, tách khỏi pháp nhân THOM. Mã PRD-XXXX của sản phẩm giữ nguyên, chỉ update field `primary_bu`.

**Sub-brand THOM:**

| Mã  | Tên          | Food Cost mục tiêu | Menu                   | Trạng thái                          |
| --- | ------------ | ------------------ | ---------------------- | ----------------------------------- |
| CFT | Café Thơm    | 22%                | Cà phê, trà, đồ ăn nhẹ | Hoạt động                           |
| MBT | Một Bữa Thơm | 38%                | Fine Dining châu Âu    | Hoạt động                           |
| MBC | Một Bữa Cơm  | 32%                | Cơm Việt, bữa trưa     | → Pending reclassify thành BU `COM` |

**Sub-brand AD2 (mới):**

| Mã  | Tên       | Food Cost mục tiêu | Menu               | Trạng thái |
| --- | --------- | ------------------ | ------------------ | ---------- |
| PZG | Pizza Gập | 28–32%             | Pizza, đồ ăn nhanh | Hoạt động  |

---

## 3. Đề xuất — §4.4 Sub-category thiếu

### 3A. PHÒNG NGHỈ (ROM) — thêm mới

Hiện tại ROM không có subcategory nào → Kupid không thể tính RevPAR theo loại phòng.

| Mã | Tên | Áp dụng BU | Ghi chú |
|----|-----|------|--------|
| ROM-STD | Phòng tiêu chuẩn | KUP | Phòng đơn/đôi thông thường |
| ROM-FAM | Phòng gia đình | KUP | Phòng lớn / nhiều người |
| ROM-SPE | Phòng đặc biệt | KUP | View đặc biệt, thiết kế riêng |
| ROM-WHL | Thuê nguyên tầng / toà | KUP | Nhóm lớn, đoàn |
| ROM-REX | Phòng / Khu nghỉ (REX) | REX | Placeholder — xác định sau khảo sát |

### 3B. DỊCH VỤ (SVC) — thêm mới

Hiện tại SVC không có subcategory → không phân biệt được doanh thu từ tour TMM, đặt chỗ đoàn BKL, hay vận chuyển Sales.

| Mã | Tên | Áp dụng BU | Ghi chú |
|----|-----|------|--------|
| SVC-EVT | Sự kiện / Đặt chỗ đoàn | BKL, KUP, TMM | Private event, tiệc |
| SVC-TUR | Tour / Trải nghiệm | TMM, REX | Cho ăn thú, cắm trại, tham quan |
| SVC-TRN | Vận chuyển | Sales | Xe dịch vụ, đưa đón đoàn |
| SVC-ROM | Dịch vụ phòng | KUP | Room service, laundry |
| SVC-MKT | Dịch vụ phụ trợ bán hàng | Tất cả | Không phổ biến — dùng khi phát sinh |

### 3C. BEV — cập nhật scope ALC

| Mã | Tên | Áp dụng BU hiện tại | Đề xuất cập nhật |
|----|-----|------|--------|
| ALC | Có cồn | BKL, THOM | BKL, THOM, **KUP** (mini-bar) |

> [!question] Cần xác nhận
> TMM có bán rượu/bia không? Nếu có (đặt chỗ đoàn, BBQ ngoài trời) → thêm TMM vào ALC scope.

---

## 4. Đề xuất — §2.2 Phạm vi Dữ liệu (cập nhật bảng)

| BU                | Số SKU hiện tại | Sub-brand    | Food Cost mục tiêu | Ghi chú                    |
| ----------------- | --------------- | ------------ | ------------------ | -------------------------- |
| BKL               | 112             | —            | 25–28%             | Đang vận hành              |
| MBT               | 77              | Một Bữa Thơm | 38%                | Đang vận hành              |
| CFT               | 53              | Café Thơm    | 22%                | Đang vận hành              |
| MBC               | 47              | Một Bữa Cơm  | 32%                | → Pending reclassify COM   |
| AD1               | ~20             | —            | 20–25%             | Từ AIR — cần kiểm kê       |
| AD2               | ~15             | —            | 20–25%             | Từ AIR — cần kiểm kê       |
| PZG               | TBD             | —            | 28–32%             | Chưa có trong database     |
| KUP               | TBD             | —            | ROM + F&B          | ROM/SVC chưa mã hóa        |
| TMM               | TBD             | —            | 30–35%             | Chưa có trong database     |
| COM               | TBD             | —            | 30–35%             | Pending ĐKĐKD              |
| REX               | TBD             | —            | TBD                | Mở 08/2026                 |
| **Tổng hiện tại** | **326**         | —            | —                  | Chỉ tính F&B đang vận hành |

---

## 5. Đề xuất — §7 KPIs (bổ sung)

| Chỉ số | Mục tiêu | Công thức | Tần suất |
|-----|-------|--------|-------|
| Food Cost % — AD1/AD2 | 20–25% | Giá thành / Giá bán × 100 | Hàng tuần |
| Food Cost % — PZG | 28–32% | Giá thành / Giá bán × 100 | Hàng tuần |
| Food Cost % — TMM | 30–35% | Giá thành / Giá bán × 100 | Hàng tuần |
| Food Cost % — COM | ≤ 32% | Giá thành / Giá bán × 100 | Hàng tuần |
| RevPAR theo loại phòng — KUP | TBD | DT phòng / Số phòng available | Hàng tuần |
| % SKU có Recipe — PZG/TMM/COM | 100% | Món có Recipe / Tổng món | Hàng tháng |

---

## 6. Đề xuất — §4.4 Sub-category BKL (sau khi đối chiếu menu thực tế)

> Review từ `NQDL-BKL-FB-SOP-001` — menu Tây Nguyên BKL có đặc thù riêng, sub-category generic không đủ.

### 6A. Vấn đề phát hiện

| Sub-category | Vấn đề |
|---|---|
| `BBQ` | Quá rộng — thịt nướng + hải sản nướng + gia cầm nướng đều vào 1 bucket → mất food cost phân tích theo nguyên liệu |
| `MAI` | Lẩu (4 SKU, food cost 28%, giá TB 380k) bị gộp vào MAI — format sharing, logic cost khác hoàn toàn |
| `APP` | 6 món rau ăn kèm BBQ bị label khai vị — sai về mặt menu engineering |
| `SNA` | BKL không có snack — trường này sẽ luôn trống, noise trong báo cáo |
| `ALC` | Rượu cần (3 SKU, đặc sản Tây Nguyên, 150k) bị gộp với bia/rượu vang — mất bản sắc và food cost sai |
| Mẹt cơm | Chưa rõ là `SET` (1 SKU trên POS) hay `CMB` (bundle nhiều SKU) — cần IT xác nhận |

### 6B. Sub-category FOD đề xuất cho BKL

| Mã | Tên | Áp dụng | Thay thế |
|---|---|---|---|
| APP | Khai vị | BKL | Salad, khai vị nóng |
| SID | Món phụ / Side dish | BKL, THOM | Rau ăn kèm BBQ — **mới** |
| GRL | Đồ nướng | BKL | Thay `BBQ` — bao gồm thịt + hải sản + gia cầm nướng |
| HOT | Lẩu / Hot pot | BKL, THOM | Tách khỏi MAI — **mới** |
| MAI | Món chính | Tất cả | Cơm/Bún/Pasta — giữ cho non-grilled, non-hotpot |
| SET | Set menu / Mẹt cơm | BKL, THOM, PZG | Nếu CukCuk bán 1 SKU |
| DES | Tráng miệng | Tất cả | Giữ nguyên |

### 6C. Sub-category BEV đề xuất cho BKL

| Mã | Tên | Áp dụng | Thay thế |
|---|---|---|---|
| COF | Cà phê | AD1, AD2, CFT, BKL | Thêm BKL |
| TEA | Trà | AD1, AD2, CFT, BKL | Thêm BKL |
| JUI | Nước ép | Tất cả | Giữ nguyên |
| SMO | Sinh tố | Tất cả | Giữ nguyên |
| SOF | Nước ngọt / Nước đóng chai | Tất cả | **Mới** — margin + food cost khác đồ uống pha chế |
| ALC | Bia / Rượu vang | BKL, THOM, KUP | Bỏ rượu cần ra |
| TRD | Đặc sản uống (Rượu cần, rượu thảo mộc…) | BKL, TMM | **Mới** — đặc sản Tây Nguyên |

### 6D. Mâu thuẫn Food Cost BKL — cần xác nhận

> [!warning] Cần kế toán xác nhận
> - **SOP-002** §2.2 ghi mục tiêu Food Cost BKL: **25–28%**
> - **NQDL-BKL-FB-SOP-001** §1 ghi: **32–35%** (và từng món đặc trưng thực tế 28–35%)
> Hai con số mâu thuẫn. Nếu KPI dùng 25–28% mà thực tế target 32–35% thì báo cáo sẽ luôn "miss" mà không phải do vận hành kém.

---

## Việc cần làm để duyệt SOP

- [ ] IT kiểm kê 35 SKU AIR → phân bổ AD1 vs AD2 #task 📅 2026-07-20 🔺
- [ ] Xác nhận TMM bán cồn hay không #task 📅 2026-07-18 🔼
- [ ] IT tạo mã PZG, TMM, KUP trên CukCuk POS #task 📅 2026-07-20 🔼
- [ ] Kupid: tạo mã PRD phòng nghỉ (đang chờ danh sách room type) #task 📅 2026-07-18 🔺
- [ ] Kế toán xác nhận Food Cost BKL đúng là 25–28% hay 32–35% #task 📅 2026-07-18 🔺
- [ ] IT xác nhận mẹt cơm BKL trên CukCuk là 1 SKU hay bundle #task 📅 2026-07-18 🔼
- [ ] Trình CEO/CFO phê duyệt bản đề xuất này → update SOP-002 v1.2 #task 📅 2026-07-27 🔺

---

*Người soạn: Ngọc Thy · Tham chiếu: [[2026-07-13 Giao ban tuần]] · SOP gốc: NQDL-MDP-SOP-002 v1.1*
