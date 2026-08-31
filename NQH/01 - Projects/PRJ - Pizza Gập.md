---
tags: [project, pzg]
status: active
owner: "Ngọc Thy"
deadline: "2026-06-30"
---

# PRJ — Pizza Gập: Tái sản xuất & Đóng gói (Sprint 17–30/06)

> Dự án Stage-Gate. [[Working-Preferences|Tôi]] là **PJM**. Pizza Gập vận hành tại [[BU - AirDream 2|ADR2 — AirDream 2]] (vị trí chia sẻ với BKL). BU thương hiệu: [[BU - Pizza Gập]].

## 🎯 Mục tiêu & deadline
- **Sprint 10 ngày: 17/06 → 30/06/2026.** Khai trương chính thức: **đầu tháng 7**.
- 3 kết quả phải có:
  1. **Sản phẩm đạt chuẩn** (làm lại, nghiệm thu tại quầy + bán thành phẩm từ bếp tổng).
  2. **Bộ hồ sơ "đóng gói" dự án** để BGĐ quyết định **mở chuỗi** (Go/No-Go).
  3. **Kế hoạch phát triển cơ sở mới** (đang trễ — cấp trên hối).

## 📌 Bối cảnh quan trọng (từ hồ sơ NQH-SOP)
- Dự án đang ở **Gate 5 / Launch-Handover, trễ ~13 ngày** (hạn cũ 30/05). Hoàn thành thực tế **~50-55%** (QA 12/06).
- **Vấn đề chính = "systematization gap"**: ~8/9 SOP vận hành + dashboard hiệu suất + mô hình P&L + danh sách NVL-CCDC **đã có draft trên Google Drive**, chỉ **chưa migrate vào NQH-SOP + QA review**. KHÔNG phải "chưa làm".
- ⇒ Phần lớn công sức sprint này là **nghiệm thu lại sản phẩm** + **hệ thống hoá drafts** + **mở rộng**, không phải làm mới từ đầu.
- **Tài liệu nền tái dùng** (trong `../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/11_Working/BD_Projects/PizzaGap-Project/`):
  - `Gate-3_Launch_Handover/PZG-G3-CHECKLIST.md` — checklist bàn giao + KPI (DT ≥2M/ngày, food cost ≤32%, ≥40 phần/ngày)
  - `Gate-3_Launch_Handover/PZG-G5-ANALYSIS-TRE-TIEN-DO-11062026.md` — phân tích trễ + recovery plan + 11 tiêu chí Gate 5
  - `PZG-FIX-PLAN-GO-NOGO-TEMPLATE.md` — mẫu Sổ rủi ro + Kế hoạch khắc phục + **Biên bản Go/No-Go**
  - `PZG-IN-A-BOX-PACKAGING-CHECKLIST-12052026.md` — checklist bao bì
  - `PZG-BTP-RECIPES-THANG-02062026.md` + `PZG-PROCESS-RECIPE-HAO-ANALYSIS-19042026.md` — công thức/quy trình
  - Quy trình test món chuẩn: `02_Nhat_Quang_Da_Lat/Operations/NQH-RD-SOP-MENU-002_New_Dish_Test_Process.md` (thang **135 điểm**)

---

## 1. ✅ Việc A — Xin phê duyệt 10 ngày làm lại sản phẩm
**Hướng xử lý:** Soạn **tờ trình 1 trang** gửi [[Đặng Hoàng Anh]] (CEO NQDL) — cc [[Đặng Thế Tài]]: (1) lý do làm lại sản phẩm, (2) phạm vi, (3) nguồn lực cần, (4) timeline 17–30/6, (5) cam kết khai trương đầu T7, (6) rủi ro nếu không duyệt. Dùng khung quyết định trong `PZG-FIX-PLAN-GO-NOGO-TEMPLATE.md`.
- [ ] Soạn & gửi tờ trình xin phê duyệt 10 ngày làm lại sản phẩm #task 👤[[Đặng Hoàng Anh]] 📅 2026-06-17 🔺

## 2. 🔬 Đánh giá (7 hạng mục)
> Mỗi hạng mục: **tiêu chí đạt rõ ràng** + **nguồn tái dùng**. Sản phẩm dùng chuẩn nghiệm thu chính thức.

### 2.1 Sản phẩm — quầy + bán thành phẩm (BTP) từ bếp tổng
Màu sắc · vị · mùi · kết cấu · kích thước. So **sản phẩm tại quầy** vs **BTP bếp tổng gửi qua** → đánh giá lại menu + chất lượng thực tế.
💡 **Bổ sung:** chấm theo **Phiếu đánh giá testing 135 điểm** (NQH-RD-SOP-MENU-002), ngưỡng **PASS ≥80%**. Thêm: **food cost ≤32%** · thời gian ra món · độ ổn định khi làm số lượng lớn · **ảnh hưởng bao bì tới chất lượng khi giao** (giữ nóng/giòn) · shelf-life BTP · độ đồng nhất giữa các mẻ BTP.
- [ ] Nghiệm thu lại sản phẩm (quầy + BTP) theo phiếu 135đ #task 👤[[Bảo]] 📅 2026-06-21 ⏫

### 2.2 Quy trình sản xuất
Các bước · công thức định lượng · thời gian · kỹ thuật · công suất.
💡 **Bổ sung:** công suất giờ cao điểm (phần/giờ) · điểm nghẽn · phân định rõ phần làm ở **bếp tổng (BTP)** vs **ráp tại quầy** · recipe card chuẩn hoá.
- [ ] Chuẩn hoá quy trình sản xuất + recipe card #task 👤[[Bảo]] 📅 2026-06-22 ⏫

### 2.3 Quy trình HACCP / vệ sinh ATTP
💡 **Bổ sung (gate bắt buộc trước khai trương):** **giấy phép VSATTP** cho quầy tại ADR2 · rủi ro **nhiễm chéo** (tủ đông/kho dùng chung BKL — đã nêu trong Red-Team) · log nhiệt độ.
- [ ] Hoàn thiện HACCP/ATTP + xác nhận giấy phép VSATTP #task 📅 2026-06-23 ⏫

### 2.4 Quy trình kho
💡 **Bổ sung:** par level · FIFO · NCC + giá · lịch đặt hàng · quy trình **nhận BTP từ bếp tổng**. Nguồn: `NQDL-PZG-WI-003_Warehouse_Inventory_Daily`, `NQDL-AFS-BTP-SOP-001_BTP_Receiving`.
- [ ] Chốt quy trình kho + par level + nhận BTP #task 📅 2026-06-23 🔼

### 2.5 Luồng vận hành bếp — layout + luồng việc
💡 **Bổ sung:** layout quầy · luồng order → làm → pickup (POS) · tách luồng khách/nhân viên với BKL. Nguồn: `PZG-SOP-OPS-ORDER-PICKUP-Thy-23042026.md` + Open/Close shift checklist.
- [ ] Chốt layout + luồng vận hành bếp #task 👤[[Kiệt]] 📅 2026-06-22 🔼

### 2.6 Định biên
💡 **Bổ sung:** số nhân sự/ca · vai trò · chi phí lương · **kế hoạch tuyển + đào tạo trước khai trương** (Module 7 đang thiếu 4 items).
- [ ] Lập định biên + kế hoạch tuyển/đào tạo #task 👤[[Kiệt]] 📅 2026-06-24 ⏫

### 2.7 P&L
💡 **Bổ sung:** doanh thu dự báo (chuẩn KPI: ≥2M/ngày, ≥40 phần/ngày) · breakeven · CapEx vs OpEx · payback · **transfer price BTP từ bếp tổng**. Nguồn: P&L Model Google Sheet (đã có).
- [ ] Hoàn thiện mô hình P&L 30 ngày + breakeven #task 👤[[Bảo]] 📅 2026-06-25 ⏫

## 3. 🚧 Các công việc (workstreams)

### 3.1 Đặt bao bì — ⚠️ ĐƯỜNG GĂNG (lead time!)
💡 In bao bì thường mất **7–15 ngày** → **phải đặt 17–18/6**, nếu không lỡ khai trương đầu T7. Chốt: thiết kế (theo Brand Guidelines v1.0 của Hoàng Oanh) · SKU (hộp các size, túi, ly…) · số lượng · nhà in. Nguồn: `PZG-IN-A-BOX-PACKAGING-CHECKLIST-12052026.md`.
- [ ] Chốt thiết kế + số lượng + đặt bao bì với nhà in #task 📅 2026-06-18 🔺

### 3.2 Chiến dịch MKT khai trương → hè
💡 Brief + ngân sách + kênh (FB/Zalo/local/KOL) + lịch nội dung + ưu đãi khai trương. Phối hợp Thừa An + Đức Duy (Module 8 Marketing đang chậm — cần kick-off gấp).
- [ ] Brief & chốt chiến dịch MKT khai trương–hè #task 📅 2026-06-24 ⏫

### 3.3 Đóng gói dự án (closure package — để quyết mở chuỗi)
💡 = hoàn thiện **11 tiêu chí Gate 5 + ~50 items**: migrate 8 SOP drafts → NQH-SOP · Brand Guidelines v1.0 · P&L 30 ngày · NVL-CCDC · Sổ tay nhân sự · Lessons Learned · Sổ rủi ro. Đây là bộ hồ sơ BGĐ dùng để quyết **Go/No-Go mở chuỗi**.
- [ ] Hoàn thiện bộ đóng gói dự án (Gate 5 closure package) #task 📅 2026-06-29 ⏫

### 3.4 Kế hoạch phát triển cơ sở mới (SOS — đã trễ)
💡 Site selection #2 ĐL (đã dời 06→08/2026) · tiêu chí chọn site · **CapEx mô hình 1 cơ sở** · timeline nhân rộng. Phối hợp [[Bảo]] + Vy. **Báo cáo rõ lý do trễ + kế hoạch bắt kịp** cho cấp trên.
- [ ] Lập kế hoạch cơ sở mới + báo cáo lý do trễ #task 👤[[Bảo]] 📅 2026-06-26 🔺

### 3.5 Quyết định & khai trương
- [ ] Họp Go/No-Go mở chuỗi + trình BGĐ (Biên bản quyết định) #task 👤[[Đặng Hoàng Anh]] 📅 2026-06-30 🔺
- [ ] Chuẩn bị khai trương đầu T7 (training nhân sự, nghiệm thu cuối) #task 📅 2026-06-30 ⏫

---

## 4. 🗓️ Lịch 10 ngày (đường găng)
| Ngày | Trọng tâm |
|------|-----------|
| **17/6** | 🔺 Tờ trình xin phê duyệt · kick-off · chốt thiết kế bao bì |
| **18/6** | 🔺 **ĐẶT BAO BÌ** (lead time) · bắt đầu nghiệm thu sản phẩm |
| 19–21/6 | Nghiệm thu sản phẩm (quầy + BTP, 135đ) · quy trình sản xuất · layout bếp |
| 22–24/6 | HACCP/ATTP · kho · định biên · brief MKT |
| 25–26/6 | P&L · 🔺 kế hoạch cơ sở mới (SOS) |
| 27–29/6 | Đóng gói closure package (migrate drafts → hồ sơ) |
| **30/6** | 🔺 Go/No-Go mở chuỗi + trình BGĐ · chuẩn bị khai trương T7 |

## 5. ⚠️ Rủi ro & phụ thuộc
- **Bao bì lead time** → đặt ngay 18/6 (đường găng số 1).
- **Giấy phép VSATTP** chưa có → chặn khai trương. Xác nhận sớm.
- **Phụ thuộc người khác:** Hoàng Oanh (brand/bao bì design), Marketing team (đang chậm), Architect Module 4 (TBD).
- **Nhiễm chéo HACCP** do vị trí chia sẻ với BKL (tủ đông/kho chung).
- **Nhân sự chưa đủ** cho khai trương → tuyển/đào tạo kịp.

## 6. 👥 Phối hợp (ai làm gì)
| Người | Vai trò trong sprint |
|-------|----------------------|
| [[Working-Preferences\|Ngọc Thy]] | PJM — điều phối, đóng gói, trình BGĐ |
| [[Kiệt]] | QL ADR2 — vận hành, định biên, layout |
| Hào (Tổng Bếp trưởng) | Sản phẩm, công thức, BTP bếp tổng |
| [[Bảo]] | OaaS + QA — nghiệm thu, P&L, site selection |
| Hoàng Oanh | Brand guidelines, thiết kế bao bì |
| Thừa An + Đức Duy | Marketing khai trương |
| Quyên Võ | PMO BD — thẩm quyền quyết định |
| [[Đặng Hoàng Anh]] | CEO NQDL — phê duyệt, bảo trợ |
| [[Đặng Thế Tài]] | CEO NQH — quan sát/phê duyệt cấp tập đoàn |

## 7. ❓ Cần chị xác nhận (để em chỉnh kế hoạch chính xác)
1. **"Khai trương đầu T7"** = grand opening chính thức (relaunch 2.0) tại ADR2, hay là **mở cơ sở mới #2**?
2. **"Làm lại sản phẩm"** phạm vi: **toàn menu** hay một số món cụ thể?
3. Người **phê duyệt 10 ngày**: anh Hoàng Anh hay anh Tài?
4. **Bao bì**: đã có thiết kế (Brand Guidelines) chưa, hay cần thiết kế mới?

## 9. 🔁 Việc bàn giao & chi phí (cập nhật 24/6)
- [ ] Follow lộ trình training + nextsteps sau mỗi buổi #task 📅 2026-06-26 ⏫
- [ ] Tuyển đủ đội ngũ nhân sự cứng cho cơ sở #task ⏫
- [ ] Theo dõi đơn đặt bao bì → giao kịp khai trương #task 🔼
- [ ] Hoàn ứng tạm ứng **10tr** (Bflow — luồng Tạm ứng/Hoàn ứng) → [[Quy trình phê duyệt Bflow (DAG)]] #task 📅 2026-06-25 ⏫
- [ ] Báo cáo đóng gói **chi phí đầu tư ban đầu** (CAPEX) → [[Quy trình phê duyệt Bflow (DAG)]] #task 📅 2026-06-29 ⏫
- [ ] Điều chỉnh chất lượng sản phẩm — gồm khắc phục vụ **pizza mang về đợi 2h** tại [[BU - AirDream 2]] #task ⏫

## 8. 🔗 Liên kết
- BU: [[BU - Pizza Gập]] · [[BU - AirDream 2]] · Người: [[Đặng Hoàng Anh]] · [[Bảo]] · [[Kiệt]]
- Hồ sơ dự án (ngoài vault): `../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/11_Working/BD_Projects/PizzaGap-Project/`
