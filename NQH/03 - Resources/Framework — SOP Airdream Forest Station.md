---
tags: [resource, framework, sop, airdream, van-hanh]
status: draft
updated: "2026-07-12"
---

# Framework — Hệ thống SOP Airdream Forest Station

> Kiến trúc 3 tầng cho địa điểm co-location (Xe Cafe Airdream + Xe Pizza Gập), thiết kế để nhân rộng thành 2 chuỗi riêng lẻ. Ghi chú: [[Working-Preferences|Ngọc Thy]].

---

## Kiến trúc tổng quan

```
┌──────────────────────────────────────────────────────────┐
│  TẦNG 3 — SITE LAYER                                     │
│  Airdream Forest Station (rừng thông 4,500m², outdoor)   │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  TẦNG 2 — CO-LOCATION LAYER                       │   │
│  │  Quy trình phối hợp khi 2 brand cùng 1 địa điểm  │   │
│  │                                                   │   │
│  │  ┌──────────────────┐   ┌──────────────────┐      │   │
│  │  │  TẦNG 1A         │   │  TẦNG 1B         │      │   │
│  │  │  Brand SOP       │   │  Brand SOP       │      │   │
│  │  │  Xe Cafe         │   │  Xe Pizza Gập    │      │   │
│  │  │  Airdream        │   │  (chain-ready)   │      │   │
│  │  │  (chain-ready)   │   │                  │      │   │
│  │  └──────────────────┘   └──────────────────┘      │   │
│  └───────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

**Nguyên tắc sử dụng khi mở chuỗi:**
- Cafe Airdream #2 → Tầng 1A + Tầng 3 mới cho location đó
- Pizza Gập #2 → Tầng 1B + Tầng 3 mới cho location đó
- Co-location mới → Tầng 1A + 1B + Tầng 2 + Tầng 3 mới

---

## Tầng 1A — Brand SOP: Xe Cafe Airdream *(chain-ready)*

| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| CA-1 | Recipe & Quy trình pha chuẩn từng nhóm đồ uống | Barista | ⬜ Chưa viết |
| CA-2 | Tiêu chuẩn NVL đầu vào + bảo quản + tem nhãn | Barista / Site Manager | ⬜ |
| CA-3 | Tiêu chuẩn thành phẩm & presentation | Barista | ⬜ |
| CA-4 | Vệ sinh thiết bị cafe (trong ca + vệ sinh sâu định kỳ) | Barista | ⬜ |
| CA-5 | VSATTP: chống nhiễm chéo, vệ sinh cá nhân barista | Barista | ⬜ |
| CA-6 | Huỷ hàng — tiêu chí, ghi nhận, báo cáo | Barista / Site Manager | ⬜ |
| CA-7 | Training Kit barista (onboarding 3 ngày) | Site Manager | ⬜ |
| CA-8 | Brand Standards Cafe Airdream (áp dụng đồng nhất mọi location) | OM / BOD | ⬜ |

---

## Tầng 1B — Brand SOP: Xe Pizza Gập *(chain-ready)*

| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| PZ-1 | Recipe & Quy trình làm chuẩn (6 vị gập + mini + khoai tây chiên) | Pizza Staff | ⬜ |
| PZ-2 | Tiêu chuẩn NVL đầu vào + sơ chế + bảo quản + tem nhãn | Pizza Staff / Site Manager | ⬜ |
| PZ-3 | Tiêu chuẩn thành phẩm & presentation + SLA (order → giao) | Pizza Staff | ⬜ |
| PZ-4 | Vệ sinh lò + dụng cụ (trong ca + vệ sinh sâu định kỳ) | Pizza Staff | ⬜ |
| PZ-5 | VSATTP: chống nhiễm chéo, vệ sinh cá nhân nhân viên pizza | Pizza Staff | ⬜ |
| PZ-6 | Huỷ hàng — tiêu chí, ghi nhận, báo cáo | Pizza Staff / Site Manager | ⬜ |
| PZ-7 | Training Kit nhân viên pizza (onboarding 3 ngày) | Site Manager | ⬜ |
| PZ-8 | Brand Standards Pizza Gập (áp dụng đồng nhất mọi location) | OM / BOD | ⬜ |

---

## Tầng 2 — Co-location SOP: Phối hợp 2 Brand tại 1 Địa điểm

| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| CL-1 | Cơ cấu vận hành chung: site manager quản lý 2 xe | Site Manager | ⬜ |
| CL-2 | Phối hợp giờ cao điểm — peak protocol 2 brand | Site Manager + Tất cả | ⬜ |
| CL-3 | Token & Order flow chung (khách order cả 2 xe) | Tất cả tại quầy | ⬜ |
| CL-4 | Phân công nhân viên phục vụ ngoài trời | Site Manager | ⬜ |
| CL-5 | Kho & NVL: tách biệt 2 brand + điều chuyển nội bộ | Site Manager | ⬜ |
| CL-6 | Thanh toán & Đối soát: tách DT 2 brand + báo cáo tổng site | Site Manager | ⬜ |
| CL-7 | Audit co-location (đánh giá đồng thời 2 brand + vận hành chung) | OM / BOD | ⬜ |
| CL-8 | Xử lý tình huống chéo (1 xe hỏng / thiếu người) | Site Manager | ⬜ |

---

## Tầng 3 — Site SOP: Airdream Forest Station *(đặc thù địa điểm)*

### S — Site & Hạ tầng
| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| S1 | Sơ đồ địa điểm: vị trí 2 xe, zone bàn ghế, kho, luồng di chuyển | Tất cả | ⬜ |
| S2 | Biển báo & Chỉ dẫn (đặt ở đâu, nội dung gì) | Site Manager | ⬜ |
| S3 | Sắp xếp & Reset layout bàn ghế (thường / peak / mưa / sự kiện) | Server / Site Manager | ⬜ |
| S4 | Đặc thù rừng thông: xử lý lá thông · kiểm soát côn trùng · cành cây rơi | Tất cả | ⬜ |
| S5 | Bảo trì tài sản định kỳ: dù · bạt · bàn ghế ngoài trời · xe trang trí | Site Manager | ⬜ |

### O — Nhịp Vận hành
| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| O1 | Mở cửa site (checklist theo vai trò) | Tất cả | ⬜ |
| O2 | Bàn giao ca — form, checklist, ghi chú sự cố | Site Manager | ⬜ |
| O3 | Đóng cửa site (checklist theo vai trò) | Tất cả | ⬜ |

### F — Trải nghiệm Khách
| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| F1 | Tiêu chuẩn phục vụ khách tại khu ngoài trời | Server / Tất cả | ⬜ |
| F2 | Dọn dẹp bàn theo kịch bản (rời bàn · bàn lâu · peak · sau mưa) | Server | ⬜ |
| F3 | Chính sách đặc biệt: thú cưng · hút thuốc · trẻ nhỏ · chụp hình xe | Tất cả | ⬜ |
| F4 | Xử lý khiếu nại & Review tiêu cực | Site Manager | ⬜ |

### H — Tình huống Đặc biệt
| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| H1 | Thời tiết xấu: mưa · gió · sương dày · lạnh — quy trình theo cấp độ | Tất cả | ⬜ |
| H2 | Nguy hiểm từ rừng: cành cây rơi · cây nghiêng | Tất cả | ⬜ |
| H3 | Mất điện | Site Manager | ⬜ |
| H4 | Sự cố an toàn khách (té ngã, dị ứng, chấn thương) | Tất cả | ⬜ |
| H5 | Escalation matrix toàn site | Site Manager | ⬜ |

### A — Audit
| Mã | Tên SOP | Áp dụng cho | Trạng thái |
|---|---|---|---|
| A1 | Self-audit hàng ngày — site manager tự chấm điểm | Site Manager | ⬜ |
| A2 | Audit tuần — quản lý khu vực | OM | ⬜ |
| A3 | Audit OM / BOD (tiêu chí, scoring, hành động sau audit) | OM / BOD | ⬜ |
| A4 | KPI vận hành địa điểm | OM / BOD | ⬜ |

---

## RACI Tổng — Cấp Hệ thống

*R = Responsible (thực hiện) · A = Accountable (chịu trách nhiệm) · C = Consulted · I = Informed*

| Nhóm SOP | Site Manager | Barista | Pizza Staff | PT Server | OM / BOD |
|---|:---:|:---:|:---:|:---:|:---:|
| Tầng 1A — Cafe production | I | **R/A** | — | — | I |
| Tầng 1B — Pizza production | I | — | **R/A** | — | I |
| Tầng 2 — Co-location ops | **R/A** | C | C | C | I |
| S — Site & Hạ tầng | **R/A** | I | I | C | I |
| O — Nhịp vận hành | **A** | R | R | R | I |
| F — Trải nghiệm khách | **A** | R | R | **R** | I |
| H — Tình huống đặc biệt | **R/A** | R | R | R | I |
| A — Audit | R | C | C | — | **A** |

---

## Role Cards

### Site Manager
Nắm toàn bộ: CL-1→CL-8 · O1→O3 · S1→S5 · F4 · H1→H5 · A1→A4

### Barista — Xe Cafe Airdream
Nắm: CA-1→CA-7 · O1 · O3 · F1 · F2 · F3 · H1 (biết) · H4 (biết)

### Pizza Staff — Xe Pizza Gập
Nắm: PZ-1→PZ-7 · O1 · O3 · F1 · F2 · F3 · H1 (biết) · H4 (biết)

### PT Server (Ngoài trời)
Nắm: F1 · F2 · F3 · S3 · S4 · O1 · O3 · H1 (biết)

### OM / BOD
Nắm: CA-8 · PZ-8 · CL-7 · A2 · A3 · A4

---

## Trạng thái xây dựng

- [ ] Tầng 1A — Cafe Airdream (CA-1 → CA-8) #task ⏫
- [ ] Tầng 1B — Pizza Gập (PZ-1 → PZ-8) #task ⏫
- [ ] Tầng 2 — Co-location (CL-1 → CL-8) #task 🔼
- [ ] Tầng 3 — Site Layer (S · O · F · H · A) #task 🔼
- [ ] RACI tổng hoàn thiện sau khi viết xong từng SOP #task 🔽
- [ ] Role Cards hoàn thiện #task 🔽

---

## Liên kết
- BU tham chiếu: [[BU - AirDream 1]] · [[BU - Pizza Gập]]
- Bảng điều hành: [[Bảng điều hành công việc]]
