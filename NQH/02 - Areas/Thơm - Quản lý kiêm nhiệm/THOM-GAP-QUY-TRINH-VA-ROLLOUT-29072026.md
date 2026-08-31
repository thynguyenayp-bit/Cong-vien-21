# THƠM — Bản đồ phủ Quy trình + Kế hoạch Đưa xuống Cơ sở

> Lập: Ngọc Thy (QL kiêm nhiệm) · 29/07/2026 · Đối chiếu bản SOP mới nhất (origin/main 28/07)
> Mục đích: (1) xác định quy trình đang THIẾU gì để chạy cơ sở; (2) cách đưa SOP xuống cơ sở chạy đúng.

## 1. TRẢ LỜI: KHO & ĐẶT HÀNG

| Mảng | Có tài liệu? | Ở đâu | Kết luận |
|------|-------------|-------|----------|
| **Kho / tồn** | ✅ CÓ | NQDL-OPS-SOP-004 Thủ kho (cấp NQDL) + THOM-OPS-SOP-002 Kiểm kê + FM-005B/C/D | Không thiếu — nhưng ở cấp NQDL, cần **đưa xuống + gán cho thủ kho Thơm** |
| **Nhận hàng** | ✅ CÓ | NQDL-FB-SOP-002 Receiving + FM-005A Receiving Checklist | Không thiếu — cần đưa xuống |
| **Đặt hàng (vận hành BU)** | 🔴 **THIẾU** | Chỉ mảnh vụn: PROCURE-001 (leadtime, DRAFT + hết hạn 20/06) · P2P master (Holding, quá cao) · PRO-SOP-001…005 (sourcing chiến lược) · form Purchase Request rời | **Thiếu quy trình đặt hàng chạy được cho cơ sở** |
| **Par level / điểm đặt lại** | 🔴 **THIẾU** | Không có ở bất kỳ SOP Thơm nào | Cơ sở đang đặt hàng cảm tính → rủi ro dư/hao/thất thoát |

**→ Việc cần làm:** soạn 1 **Quy trình Đặt hàng Thơm (Work Instruction)** ngắn, gắn với par level, để chạy ngay; song song trình COO ratify thành SOP.

## 2. BẢN ĐỒ PHỦ TOÀN BỘ VÒNG VẬN HÀNH

Ký hiệu: ✅ đủ chạy · 🟡 có nhưng lỗi/khuyết · 🔴 thiếu hoặc không dùng được

| # | Giai đoạn | Tài liệu | Cấp | Tình trạng |
|---|-----------|----------|-----|-----------|
| 1 | **Đặt hàng + par level** | (mảnh vụn) | Holding/NQDL | 🔴 thiếu quy trình BU + chưa có par level |
| 2 | Nhận hàng | NQDL-FB-SOP-002 + FM-005A | NQDL | ✅ (cần đưa xuống) |
| 3 | Kho / tồn / xuất nhập | NQDL-OPS-SOP-004 + THOM-OPS-SOP-002 + FM-005B/C/D | NQDL+BU | ✅ (cần đưa xuống + đặt par) |
| 4 | Sơ chế / mise en place / nấu | THOM-BOH-SOP-001/004/005 | BU | 🟡 BOH-001 còn station MBC + giờ sai; BOH-004 trống vệ sinh TB+dầu; BOH-005 thiếu định lượng |
| 5 | Chuỗi lạnh / bảo quản | THOM-BOH-SOP-004 + FM-006A Temp Log | BU | 🟡 khuyết Phần C/D |
| 6 | ATTP / HACCP / dị ứng | NQDL-FB-SOP-001 HACCP + THOM-QA-SOP-002 + FM-006C | NQDL+BU | 🟡 QA-002 còn cấu trúc MBC |
| 7 | Setup khu vực / vận hành sàn | THOM-OPS-SOP-001 | BU | 🟡 còn lệnh "Setup bàn Việt" |
| 8 | Phục vụ FOH | THOM-FOH-SOP-001 | BU | 🟡 còn 2 chỗ Fine Dining; thiếu FOC + an ninh cuối ca |
| 9 | Đặt bàn / sự kiện | THOM-SVC-001/002 | BU | 🟡 SVC-001 còn 3 sub-brand+MBC; SVC-002 thiếu hủy/hoàn cọc |
| 10 | Quầy nước / bar | THOM-BAR-001/002 | BU | 🟡 BAR-001 còn "Ther"; BAR-002 draft chưa ban hành |
| 11 | **Thu ngân / đối soát tiền** | THOM-FIN-SOP-003 (×2) + FM-002/009 | BU | 🔴 trùng mã + POS sai (Square) |
| 12 | Bàn giao ca | NQDL-OPS-SOP-001 Shift Handover (33 mã ca) | NQDL | ✅ (cần đưa xuống) |
| 13 | Vệ sinh / sanitation | NQDL-OPS-CHK-001 + FM-006B | NQDL | ✅ (cần đưa xuống) |
| 14 | Xếp lịch / phân ca | THOM-OPS-WI-001 + HR-SOP-006 | BU | 🟡 draft, chờ Duy chốt mã ca |
| 15 | Kế toán / chi phí / định giá | THOM-FIN-001/002 | BU | 🟡 food cost lệch 35% vs 28-32% |
| 16 | Nhân sự / tuyển / onboard | THOM-HR-SOP-001 (định biên 29) | BU | ✅ tốt |
| 17 | Nội quy lao động | 4 file 25-26/07 (working) | Working | ⚪ mới, chưa review |
| 18 | Checklist hàng ngày | THOM-OPS-CHK-001 (30 items) | BU | 🟡 còn "Fine Dining" 1 dòng |
| 19 | Đào tạo | BU_Training_Guide_Thom | Training | ✅ |
| 20 | Menu R&D / món mới | NQH-RD-SOP-MENU-001/002 | NQDL | ✅ |

**Kết luận thiếu THẬT (không phải chỉ lỗi biên tập):**
1. 🔴 Quy trình **Đặt hàng BU + par level** (#1) — thiếu hẳn.
2. 🔴 **Đối soát tiền** (#11) — có tài liệu nhưng trùng mã + POS sai ⇒ coi như chưa chạy được.
3. 🟡 Khuyết: vệ sinh thiết bị + dầu chiên (#4/5); FOC + an ninh cuối ca (#8).

## 3. ĐƯA XUỐNG CƠ SỞ — CÁCH LÀM ĐÚNG

> ⚠️ **Nguyên tắc số 1:** KHÔNG phát bản SOP thô hiện tại xuống cơ sở — nhiều file còn MBC / Fine Dining / POS sai. Phát bản còn lỗi = nhân viên chạy sai quy trình. Phải **chốt bản sạch cho các file đưa xuống trước**, rồi mới phát.

**Nguyên tắc số 2 — không phát 22 SOP cho tất cả mọi người.** Đóng gói **theo TRẠM**, mỗi trạm chỉ nhận phần của mình:

| Trạm | Bộ tài liệu đưa xuống |
|------|----------------------|
| **Bếp (BOH)** | BOH-001 (mở/đóng bếp) + BOH-004 (nấu/chuỗi lạnh) + BOH-005 (recipe) + HACCP FB-SOP-001 + Temp Log FM-006A |
| **Sàn/Phục vụ (FOH)** | FOH-001 (đón-phục vụ-thanh toán) + OPS-001 (setup khu) + Daily Checklist |
| **Quầy nước** | BAR-001 + nội quy quầy pha chế |
| **Thu ngân** | FIN-003 đối soát tiền + FM-002 + FM-009 |
| **Kho/Đặt hàng** | OPS-SOP-004 Thủ kho + FB-SOP-002 Nhận hàng + **[MỚI] Quy trình đặt hàng** + FM-005A/B/C/D |
| **Toàn bộ NV** | Nội quy lao động (4 file) + Daily Checklist + Bàn giao ca OPS-SOP-001 |

**Trình tự triển khai (5 bước):**
1. **Chốt bản sạch** các file đưa xuống (ưu tiên bếp, thu ngân, kho/đặt hàng, FOH).
2. **Đóng gói theo trạm** — in sổ tay trạm + dán checklist tại chỗ + in sẵn form.
3. **Train** theo BU_Training_Guide_Thom; mỗi trạm 1 buổi ngắn.
4. **Giao owner từng trạm ký nhận** đã hiểu quy trình (gắn trách nhiệm).
5. **Tuần đầu audit bằng checklist** — ghi sai lệch, chỉnh, chuẩn hóa.

> **Thẩm quyền:** đưa SOP đã ratify xuống cơ sở = *triển khai* (Thy làm được). Tạo quy trình đặt hàng mới = Thy soạn **Work Instruction tạm** để chạy ngay + trình COO NQDL ratify thành SOP chính thức.

## 4. VIỆC TIẾP THEO (đề xuất thứ tự)
1. Soạn **Quy trình Đặt hàng Thơm (WI) + bảng par level** — vá lỗ hổng thật + chống thất thoát.
2. Chốt bản sạch bộ **Kho/Đặt hàng/Nhận hàng** → đưa xuống trạm kho trước (dễ, tác động chi phí ngay).
3. Xử lý **đối soát tiền** (trùng mã + POS) → đưa xuống thu ngân.
4. Dọn lỗi thời + đóng gói các trạm còn lại.
