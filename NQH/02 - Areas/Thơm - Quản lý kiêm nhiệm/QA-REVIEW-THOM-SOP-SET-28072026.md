# QA REVIEW — Bộ SOP Nhà hàng Một Bữa Thơm (21 SOP)

> Reviewer: Ngọc Thy (QA / Quản lý kiêm nhiệm Thơm) | Ngày: 28/07/2026
> Phạm vi: Toàn bộ `03_Business_Units/Thom_Restaurant/` (21 SOP .md + README)
> Đối chiếu chuẩn: banner cập nhật 17/07/2026 (MBC đã tách · KHÔNG Fine Dining · GM = Duy · "Cà Phê Thơm" · giờ NH 10–22h / Café 7:30–18h)

> ✅ **ĐÃ ĐỐI CHIẾU BẢN ONLINE MỚI NHẤT (29/07/2026)** — remote `origin/main` commit `857219c6`, README "Cập nhật lần cuối 28/07/2026". Bản 28/07 chỉ đổi 6 file Thơm (README + 5 SOP), **KHÔNG sửa các defect dưới đây → toàn bộ review vẫn còn hiệu lực.**
> Đợt 28/07 làm 3 việc: (1) README liệt kê đủ **22 tài liệu** (trước 14) — nhưng dòng 76–77 vẫn liệt kê **cả 2 file FIN-SOP-003 trùng mã**; (2) gắn thẻ `serves_sla` + sync 2 số: FOH chào khách 30s→**≤10s**, QA-001 nhiệt độ nóng 60→**>65°C**; (3) thêm mục **Nội quy Lao động** (4 file working 25–26/07, *chưa review*).
> Xác nhận còn nguyên trên bản mới: trùng mã FIN-SOP-003 · **"Fine Dining" ngay trong README mới (dòng 111 + 160)** · SVC-001/002 còn 3 sub-brand+MBC · QA-002 cấu trúc MBC · BOH-004 trống Phần C+D · FOH còn 2 chỗ Fine Dining.
> Được sửa: tên OM đúng = **Trần Nguyên Bảo** (không phải "Bảo Trần"/"Nguyễn Bảo").
> 🆕 Cần review bổ sung: `NOI-QUY-BO-SUNG-25072026`, `NOI-QUY-NHAN-VIEN-3BIS-DONG-DA`, `NOI-QUY-QUAY-PHA-CHE`, `DE-XUAT-CEO-BO-SUNG-NOI-QUY-V2-26072026` (trong `11_Working/BU_Drafts/Thom_Restaurant/`).

## KẾT LUẬN CHUNG
Đợt cập nhật 17/07 **chưa hoàn tất**: sửa xong README + banner + vài file (HR, FIN-Costing, OPS-WI), nhưng **nhiều SOP vận hành nhân viên đang dùng vẫn còn nội dung lỗi thời "sống"** (không phải chú thích lịch sử mà là lệnh thực thi). Kèm theo **4 lỗi cấu trúc/hệ thống** cần xử lý trước. Rủi ro: nhân viên làm theo quy trình MBC/Fine-Dining đã bị bỏ; kiểm soát tiền lỏng; tài liệu ATTP thiếu mảng.

Thống kê: **9 file cần sửa nặng · 10 cần sửa nhẹ–vừa · 1 draft chưa đủ ban hành · 1 file OK**.

---

## A. 4 LỖI CẤU TRÚC / HỆ THỐNG (xử lý trước tiên)

| # | Lỗi | Chi tiết | Hướng xử lý |
|---|-----|---------|-------------|
| A1 | **Trùng mã FIN-SOP-003** | Hai file khác nội dung cùng mã: `Cash_Reconciliation` (Square POS, FIN, KTT+CTO duyệt) và `Multi_Register_Reconciliation` (CukCuk, dựng trên 3 thương hiệu MBC/CFT/MBT, phòng chủ quản ghi "IT", duyệt bởi "Quản lý Thơm") | **Thu hồi/archive Multi_Register** (dựng trên mô hình MBC đã chết). NHƯNG trước khi bỏ, **di dời các chốt kiểm soát chống thất thoát mạnh nhất của nó** (đếm mù 2 người, người chứng kiến bắt buộc, bỏ két mỗi 2h, phân tầng chênh lệch 10K/100K/500K) sang bản Cash_Recon giữ lại. Rồi đổi mã cho hết trùng. |
| A2 | **Sai hệ thống POS** | `Cash_Reconciliation` mô tả toàn bộ đối soát trên **Square POS** — Thơm thực tế chạy **CukCuk**. Quy trình trỏ vào hệ thống không tồn tại. | Viết lại theo CukCuk POS. |
| A3 | **Mâu thuẫn tên & định vị MBT** | Cùng mã MBT nhưng: FOH/HR gọi **"Một Bữa Thơm"**; SVC-001/002 gọi **"Món Bếp Thơm / Món Việt Cao cấp"**; BAR-001 gọi "Đồ Âu"; QA-002 "Món Việt Cao cấp". | Chốt 1 tên chuẩn: **Một Bữa Thơm (MBT) — Modern European Country Dining**. Sửa đồng loạt. |
| A4 | **Mâu thuẫn food cost chuẩn** | FIN dùng lẫn lộn **35%** (Handbook dòng 473/678/842, Costing §6) và **28–32%** (Handbook DAG dòng 117, Costing §5B mới). | CFO/kế toán chốt 1 con số target duy nhất, sửa đồng bộ. |

---

## B. SWEEP 17/07 CHƯA HOÀN TẤT — Lỗi thời còn "sống" trong tài liệu đang dùng
*(Rủi ro vận hành cao nhất — nhân viên làm theo)*

**MBC còn active (phải bỏ):**
- `BOH-SOP-001` §2.1 dòng 128: station "**MBC Cơm Việt** | Cơm trưa combo, canh, món mặn Việt Nam" — chưa đánh dấu retired; dòng 53–54 scope "MBT + MBC" + **giờ sai "10:00-21:00"**.
- `OPS-SOP-001` header dòng 20 scope "(MBC + MBT + Quầy nước)"; §3.1 dòng 160 lệnh active "**Setup bàn Việt**" trỏ §2.2 đã retired; dòng 143/232/443 "vá cơm, vá canh / cơm trưa / cơm".
- `SVC-SOP-001` dòng 75–78 & `SVC-SOP-002` dòng 77–80: **còn nguyên 3 sub-brand gồm MBC** — cả 2 file chưa qua sweep 17/07.
- `QA-SOP-002` (Allergen — rủi ro cao): toàn bộ logic dựng trên vòng "MBC→CFT→MBT", dòng 111 "14:00-14:30 MBC→CFT vệ sinh sâu", ma trận dị ứng MBC.
- `FIN Handbook` §2.5.1 dòng 984 "MBT món Âu fine dining + **MBC** cơm Việt"; `BAR-001` dòng 54 "bữa ăn MBC".

**"Fine Dining" còn sót (sai định vị):**
- `FOH-SOP-001` dòng 236 "Đặt khăn ăn lên lòng khách **(fine dining)**" + dòng 377 "vị trí **Fine Dining Âu**".
- `OPS-CHK-001` dòng N3 "sắp xếp dao muỗng nĩa đúng vị trí **Fine Dining**".
- `FIN Handbook` dòng 984 "fine dining"; `Multi_Register` "Nhà hàng Cao cấp".

**"Ther / Cafe Ther" (phải là "Cà Phê Thơm"):**
- `BAR-001` dòng 22/53/111–112/228/247; `BOH-002` dòng 36/64/152/214; `BOH-003` dòng 38–39/156–165.

**Giờ cũ còn sót:** `Cash_Recon` dòng 79 (6-14/14-22/22-6h); `Multi_Register` dòng 95 (06:00-23:00).

---

## C. GAP NỘI DUNG / AN TOÀN
- `BOH-SOP-004`: **Phần C (vệ sinh thiết bị) + Phần D (quản lý dầu chiên) bỏ trống** ("cần bổ sung") — thiếu kiểm soát ATTP/an toàn.
- `BOH-SOP-005` Recipe Cards: **thiếu định lượng gram + cost** → không dùng để tính giá thành; mới ~180/499 dòng, gần như trống Main Course/Pasta/Dessert.
- `FOH-SOP-001`: **thiếu quy trình an ninh/kiểm đếm tiền cuối ca thực tế + quy trình FOC/void + leo thang khiếu nại** (chỉ 1 dòng "Quản lý xử lý").
- `SVC-SOP-001`: **không tích hợp CukCuk POS / Haravan** (chỉ ghi chung chung); thiếu SLA phản hồi yêu cầu đặt bàn.
- `SVC-SOP-002`: **thiếu chính sách hủy & lịch hoàn cọc**.
- `QA-SOP-002`: 3 bảng KPI cuối file mâu thuẫn nhau + khối template rỗng dán thêm (dòng 462–521).
- `QA-SOP-001`: mâu thuẫn nội bộ — ra món ≤12 phút (dòng 43) vs <15 phút (dòng 191); audit 80+ vs ≥85.
- `BAR-SOP-002`: vẫn **DRAFT** (khung rỗng) — thiếu QC 10 tiêu chí, công thức/định lượng, bài kiểm; **chưa đủ điều kiện ban hành**.

---

## D. QUẢN TRỊ PHIÊN BẢN & THẨM QUYỀN
- **Ô ký sai thẩm quyền:** `FOH-001` (dòng 561), `QA-002` (dòng 450), `Multi_Register` ghi người phê duyệt = **"Quản lý Thơm"**. ⚠️ Vi phạm quy tắc NQH: **GM BU không có thẩm quyền ban hành SOP** — phải COO NQDL duyệt + CEO ban hành.
- **Version header ≠ changelog:** OPS-001 (2.0 vs 2.1), OPS-CHK-001 (1.1 vs 1.2), FOH-001 (2.0 vs 2.1), HR-001 (2.0 vs 2.1).
- **Ngày review quá hạn:** OPS-002 (02/03), QA-001 (02/03), QA-002 (01/04), SVC (20/03), HR (01/04), FOH (01/07) — đều đã qua so với 28/07/2026.

---

## BẢNG TÌNH TRẠNG 21 FILE

| File | Tình trạng |
|---|---|
| BOH-SOP-001 Kitchen Open/Close | 🔴 Sửa nặng (station MBC còn active, giờ sai) |
| BOH-SOP-002 Commissary | 🟡 Sửa nhẹ (deprecated, còn "Ther") |
| BOH-SOP-003 BTP Transfer | 🟡 Sửa nhẹ (deprecated, còn "Ther") |
| BOH-SOP-004 Cooking/Cold Chain | 🔴 Sửa nặng (Phần C+D trống) |
| BOH-SOP-005 Recipe Cards | 🔴 Sửa nặng (thiếu định lượng/cost) |
| OPS-SOP-001 Zone Setup | 🔴 Sửa nặng (lệnh "Setup bàn Việt" active) |
| OPS-SOP-002 Inventory | 🟡 Sửa nhẹ (review quá hạn) |
| OPS-CHK-001 Daily Checklist | 🟡 Sửa nhẹ ("Fine Dining", lệch version) |
| OPS-WI-001 Scheduling | 🟢 OK (draft, đã cờ chờ Duy) |
| FIN-SOP-001 Accounting Handbook | 🟡 Sửa vừa (fine dining+MBC §2.5.1, food cost lệch) |
| FIN-SOP-002 Menu Costing | 🟡 Sửa nhẹ (KPI §6 lệch 35% vs 28-32%) |
| FIN-SOP-003 Cash_Reconciliation | 🟡 Sửa vừa (Square POS, trùng mã) |
| FIN-SOP-003 Multi_Register | 🔴 THU HỒI (dựng trên MBC) |
| FOH-SOP-001 Guest Welcome | 🟡 Sửa vừa (2 chỗ Fine Dining, thiếu FOC/an ninh ca) |
| SVC-SOP-001 Reservation | 🔴 Sửa nặng (3 sub-brand + MBC, chưa sweep) |
| SVC-SOP-002 Event Catering | 🔴 Sửa nặng (MBC, thiếu chính sách hủy cọc) |
| HR-SOP-001 Recruitment | 🟢 OK / sửa nhẹ (đã update 29 NV, GM Duy) |
| QA-SOP-001 Chất lượng | 🟡 Sửa nhẹ (mâu thuẫn số phút/audit) |
| QA-SOP-002 Allergen | 🔴 Sửa nặng (cấu trúc MBC, 3 KPI mâu thuẫn) |
| BAR-SOP-001 Beverage Counter | 🔴 Sửa nặng (Cafe Ther, MBC, xung đột BAR-002) |
| BAR-SOP-002 Barista DRAFT | ⚪ Draft — chưa đủ ban hành |

---

## ĐỀ XUẤT HÀNH ĐỘNG (ưu tiên)
1. **Đợt 1 (gấp — an toàn & tiền):** A1 (trùng mã + di dời chốt kiểm soát tiền), A2 (POS CukCuk), BOH-004 (vệ sinh/dầu), QA-002 (re-scope allergen). → giảm rủi ro thất thoát & ATTP ngay.
2. **Đợt 2 (định vị & vận hành):** dọn sạch MBC/Fine Dining/Ther còn sót ở BOH-001, OPS-001, SVC-001/002, FOH-001, BAR-001, CHK-001; chốt tên MBT (A3) + food cost (A4).
3. **Đợt 3 (chất lượng & quản trị):** điền BOH-005 định lượng/cost; hoàn thiện BAR-002; sửa ô ký sai thẩm quyền (D); đồng bộ version header + gia hạn ngày review.

> ⚠️ Lưu ý thẩm quyền: Thy sửa ở dạng **QA draft / đề xuất cập nhật**; ban hành chính thức cần COO NQDL duyệt + CEO ban hành (GM không tự ban hành SOP).
