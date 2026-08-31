---
tags: [master-data, kupid, product, room, PRD]
date: 2026-07-13
status: draft
ref-sop: NQDL-MDP-SOP-002 v1.1
---

# Kupid — Đề xuất tên phòng & mã PRD

> Nguồn: "Phòng Kupid - Google Tài liệu.pdf" — đã xác nhận lại với GM Kupid (13/07/2026).
> Xem thêm: [[2026-07-13 SOP-002 Product Master Data — Đề xuất bổ sung]]

---

## Logic đặt tên

**Nguyên tắc: `[View] + [Tier]`** — khách nhìn tên biết ngay view và đẳng cấp.

### Tier progression

| Nhóm                          | Tier (tăng dần)                        | Dấu hiệu phân biệt           |
| ----------------------------- | -------------------------------------- | ---------------------------- |
| **Sân Vườn** (600k–1,200k)    | Standard → Classic → Superior → Deluxe | AC / số mặt kính / tiện nghi |
| **Đồi Thông** (1,500k–1,800k) | Standard → Deluxe → Premium → Grand    | Vị trí / số mặt kính / tầng  |
| **Gia Đình** (1,000k–1,200k)  | Standard → Sân Vườn                    | 2 giường 4 người             |

**Chi tiết Sân Vườn:**
- **Standard** (600k) — không AC, 1 mặt kính, tầng trệt / hầm
- **Classic** (800k) — không AC, 2 mặt kính, view thoáng hơn
- **Superior** (1,000k) — có máy lạnh
- **Deluxe** (1,200k) — có máy lạnh, đa số bồn tắm

**Chi tiết Đồi Thông:**
- **Standard** (1,500k) — view đồi thông/thung lũng, AC
- **Deluxe** (1,600k) — vị trí đặc biệt: góc, áp mái
- **Premium** (1,700k) — 2 mặt kính rõ ràng, view đồi thông
- **Grand** (1,800k) — top tier, view cao nhất

> [!warning] Bồn tắm KHÔNG phải tier indicator
> DH4 (600k) có bồn tắm; C302 (1,600k) chỉ vòi tắm đứng. Đây là đặc điểm room-level, ghi trong EzCloudHotel — KHÔNG đưa vào tên PRD.

> [!note] Tại sao bỏ tên cũ
> • "Sân Vườn" vs "Vườn" (2 tên gần giống nhau cho 2 tier khác nhau) → thay bằng "Sân Vườn" nhất quán cho toàn nhóm  
> • "Vườn Bồn Tắm" — đặt tên theo toilet, mâu thuẫn với callout trên  
> • "Đặc Biệt" vs "Cao Cấp" — không rõ tier nào cao hơn → thay bằng Deluxe/Premium  
> • "Grand Đồi Thông" — tiếng Anh chen giữa tên Việt → đổi thành "Đồi Thông Grand"

---

## Bảng đề xuất — 10 Room Type / 10 PRD

| PRD      | Tên tiếng Việt          | Tên OTA (EN)           | Giá/đêm   | SL  | Sub-cat |
| -------- | ----------------------- | ---------------------- | --------- | --- | ------- |
| PRD-0327 | Phòng Sân Vườn          | Garden Room            | 600.000   | 4   | ROM-ECO |
| PRD-0328 | Phòng Sân Vườn Classic  | Garden Classic Room    | 800.000   | 2   | ROM-ECO |
| PRD-0329 | Phòng Sân Vườn Superior | Garden Superior Room   | 1.000.000 | 3   | ROM-GDN |
| PRD-0330 | Phòng Sân Vườn Deluxe   | Garden Deluxe Room     | 1.200.000 | 5   | ROM-GDN |
| PRD-0331 | Phòng Đồi Thông         | Pine Hill Room         | 1.500.000 | 10  | ROM-HIL |
| PRD-0332 | Phòng Đồi Thông Deluxe  | Pine Hill Deluxe Room  | 1.600.000 | 5   | ROM-HIL |
| PRD-0333 | Phòng Đồi Thông Premium | Pine Hill Premium Room | 1.700.000 | 3   | ROM-HIL |
| PRD-0334 | Phòng Đồi Thông Grand   | Grand Pine Hill Room   | 1.800.000 | 6   | ROM-HIL |
| PRD-0335 | Phòng Gia Đình          | Family Room            | 1.000.000 | 1   | ROM-FAM |
| PRD-0336 | Phòng Gia Đình Sân Vườn | Family Garden Room     | 1.200.000 | 6   | ROM-FAM |
|          |                         |                        |           |     |         |

**Tổng: 45** ✓

---

## Mapping phòng vật lý → Room Type

| PRD      | Phòng thuộc nhóm                                                                                              | Đặc điểm chung                            | Toilet                                                |     |
| -------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------- | --- |
| PRD-0327 | A103, B103, DH4 (tầng trệt) · CH2 (tầng hầm)                                                                  | Không AC, 1 mặt kính, view sân vườn       | A103/B103/CH2: vòi tắm đứng · **DH4: bồn tắm**        |     |
| PRD-0328 | D204, D304                                                                                                    | Không AC, 2 mặt kính, view sân vườn       | Bồn tắm                                               |     |
| PRD-0329 | C203 (2mk) · C303 (1mk) · D303 (2mk, AC?)                                                                     | AC¹, view sân vườn                        | C203/C303: vòi tắm đứng · **D303: bồn tắm**           |     |
| PRD-0330 | A101, A102, B101, B102, C102                                                                                  | AC, **1 mặt kính**, view sân vườn         | A101/A102/B101/B102: bồn tắm · **C102: vòi tắm đứng** |     |
| PRD-0331 | A201, A202, A301, A302, B201, B202, B301, B302 (thung lũng, 2mk) · C103, C204 (đồi thông, 1mk)²               | AC, bồn tắm, view đồi thông/thung lũng    | Bồn tắm                                               |     |
| PRD-0332 | DH1, DH2 (góc đồi thông, 2mk) · C304 (áp mái đồi thông, 1mk) · C302 (thung lũng, 2mk) · C202 (sân vườn, 1mk)³ | AC, vị trí đặc biệt                       | C202/C302: vòi tắm đứng · C304/DH1/DH2: bồn tắm       |     |
| PRD-0333 | C101, D101, D102                                                                                              | AC, 2 mặt kính, view đồi thông            | Bồn tắm                                               |     |
| PRD-0334 | C201, C301, D201, D202, D301, D302                                                                            | AC, 2 mặt kính, view đồi thông/thung lũng | Bồn tắm                                               |     |
| PRD-0335 | DH3                                                                                                           | Tầng hầm, 2 giường 4 người, 1 mặt kính    | Bồn tắm                                               |     |
| PRD-0336 | A203, A303, B203, B303 (tầng 2, sân vườn) · D103, D203 (sân trước/vườn, 2mk)                                  | 2 giường 4 người, view sân vườn           | A/B: vòi tắm đứng · **D103/D203: bồn tắm**            |     |

> ¹ **D303 — chưa rõ AC:** PDF không ghi máy lạnh (C203/C303 có). Tạm nhóm vào PRD-0329, cần xác nhận.

> ² **PRD-0331 không đồng nhất hoàn toàn:** C103/C204 có 1 mặt kính cửa sổ lớn + view đồi thông; A/B201–302 có 2 mặt kính + view thung lũng — nhưng cùng giá 1,500k và cùng AC + bồn tắm, giữ 1 PRD.

> ³ **C202 — anomaly:** View sân vườn nhưng giá 1,600k (bằng nhóm đồi thông đặc biệt). Nhóm theo giá vào PRD-0332, nhưng trên OTA nên ghi rõ view thực tế.

> **PRD-0336:** D103/D203 có bồn tắm + 2 mặt kính (tốt hơn A/B). Cùng giá — giữ 1 PRD. Nếu muốn tách: PRD-0337 "Phòng Gia Đình Sân Vườn Superior" cho D103, D203.

---

## Sub-category ROM

| Mã | Tên | Nhóm giá | Số phòng |
|---|---|---|---|
| ROM-ECO | Sân Vườn Budget | 600k–800k | 6 |
| ROM-GDN | Sân Vườn Superior–Deluxe | 1.000k–1.200k đơn | 8 |
| ROM-HIL | Đồi Thông (tất cả tier) | 1.500k–1.800k đơn | 24 |
| ROM-FAM | Gia Đình | 1.000k–1.200k đôi | 7 |

---

## Việc cần làm

- [ ] Xác nhận tên mới (scheme Sân Vườn/Đồi Thông + Classic→Grand) với GM + Sales trước khi nhập OTA #task 📅 2026-07-18 🔺
- [ ] Đối chiếu mapping phòng vật lý → PRD với GM Kupid để xác nhận #task 📅 2026-07-18 🔺
- [ ] Xác nhận D303 có máy lạnh không (PDF không ghi rõ) #task 📅 2026-07-18 🔼
- [ ] Xác nhận C202 (sân vườn, 1,600k) giữ trong PRD-0332 hay tách riêng #task 📅 2026-07-18 🔼
- [ ] Quyết định tách PRD-0336 → PRD-0336 + PRD-0337 (D103/D203 bồn tắm + 2mk, A/B không) #task 📅 2026-07-18 🔼
- [ ] IT nhập 10 room type vào EzCloudHotel + CukCuk POS #task 📅 2026-07-20 🔺
- [ ] Tạo PRD-0327 → PRD-0336 trong Excel Master Data #task 📅 2026-07-20 🔺

---

*Người soạn: Ngọc Thy · 13/07/2026 · Cập nhật: 13/07/2026*
