---
tags: [SLA, NQDL, Cafe-Thom, AirDream-Cafe, Nha-Hang-Thom, KPI, Compliance]
status: DRAFT
date: 2026-08-15
author: Nguyễn Tuấn Kiệt — OM NQDL
base_reference:
  Cafe-Thom: NQDL-AFS (Airdream Forest Station) — QA-SOP-001/004, FOH-SOP-001, FNB-SOP-007/009/010
  Nha-Hang-Thom: NQDL-BKL (Buôn Kơ Lang) — QA-SOP-001, CS-SOP-001, FB-SOP-001, SEC-SOP-001
purpose: Tách 3 brand Nhà hàng Thơm — xây dựng SLA riêng cho Cafe Thơm & AirDream Cafe và Nhà hàng Thơm
---

# Bộ tiêu chí SLA — Cafe Thơm & AirDream Cafe / Nhà hàng Thơm

> **Nguồn tham chiếu:**
> - **Cafe Thơm & AirDream Cafe** → dựa trên khung SLA của **BU Airdream Forest Station (AFS/AD2)**
> - **Nhà hàng Thơm** → dựa trên khung SLA của **BU Buôn Kơ Lang (BKL)**
>
> **Mục đích:** Tách biệt 3 brand Nhà hàng Thơm theo yêu cầu COO — mỗi brand có bộ SLA/KPI riêng, không gộp.
>
> **Cách chấm:** Tick ☑ trực tiếp trên Obsidian khi đạt.

---

## PHẦN I — SLA BU CAFE THƠM & AIRDREAM CAFE

> *Tham chiếu khung: NQDL-AFS-QA-SOP-001 (Self-audit), NQDL-AFS-QA-SOP-004 (Site KPI), NQDL-AFS-FOH-SOP-001 (Guest Service), NQDL-AFS-FNB-SOP-007/009/010 (Cafe Airdream SOPs)*

### 1. SLA Tốc độ phục vụ (Service Speed)

- [ ] **SLA-CAFE-SPD-01** | Thời gian từ order → giao đồ uống (cafe/pha chế) | **≤ 5 phút** | POS CUKCUK + sổ ca | Hàng ngày
- [ ] **SLA-CAFE-SPD-02** | Thời gian khách đứng chờ tại quầy chưa được chào | **≤ 3 phút** | Self-audit D3 | Hàng ngày
- [ ] **SLA-CAFE-SPD-03** | Thời gian từ order → giao món phụ (bánh, snack) | **≤ 7 phút** | POS + sổ ca | Hàng ngày
- [ ] **SLA-CAFE-SPD-04** | SLA tổng hợp (% order đúng giờ) | **≥ 90%** | CUKCUK + sổ ca | Hàng tuần

### 2. SLA Kiểm soát nhiệt độ (Temperature Control)

- [ ] **SLA-CAFE-TMP-01** | Nhiệt độ cafe nóng khi phục vụ | **≥ 65°C** | Nhiệt kế đầu dò | 2 lần/ca
- [ ] **SLA-CAFE-TMP-02** | Nhiệt độ đồ uống lạnh / đá | **≤ 5°C** (không tính đá) | Nhiệt kế | 2 lần/ca
- [ ] **SLA-CAFE-TMP-03** | Nhiệt độ tủ mát bảo quản NVL | **0–5°C** | Log nhiệt độ | 4 lần/ngày
- [ ] **SLA-CAFE-TMP-04** | Nhiệt độ tủ đông bảo quản NVL | **≤ -18°C** | Log nhiệt độ | 4 lần/ngày
- [ ] **SLA-CAFE-TMP-05** | Chuỗi lạnh (cold chain) — NVL từ kho → quầy | Không đứt gãy, ≤ 30 phút ngoài vùng lạnh | Self-audit + log | Hàng ngày

### 3. SLA Trình bày & Thành phẩm (Presentation Standard)

- [ ] **SLA-CAFE-PRS-01** | Ly/cốc đúng loại theo menu, không sứt mẻ | 100% | Self-audit B | Hàng ngày
- [ ] **SLA-CAFE-PRS-02** | Latte art / lớp foam đúng chuẩn recipe | Đạt theo Recipe Card | Kiểm tra SM | Hàng ngày
- [ ] **SLA-CAFE-PRS-03** | Đồ uống đúng định lượng, đúng màu sắc | 100% đúng recipe | Audit tuần | Hàng tuần
- [ ] **SLA-CAFE-PRS-04** | Nhãn dán ngày pha trên mọi thành phẩm bán thành phẩm | 100% | Self-audit C2 | Hàng ngày

### 4. SLA Vệ sinh & ATTP (Food Safety & Hygiene)

- [ ] **SLA-CAFE-ATTP-01** | NVL hết HSD trong khu làm việc | **0 lần/tháng** | Self-audit C3 + audit tuần | Hàng ngày
- [ ] **SLA-CAFE-ATTP-02** | Sự cố VSATTP (ngộ độc, dị ứng phải xử lý y tế) | **0 lần/tháng** | Sổ sự cố | Hàng tháng
- [ ] **SLA-CAFE-ATTP-03** | Vệ sinh máy pha cafe, dụng cụ barista | Đạt chuẩn (CA-4) | Self-audit B3-B4 | Hàng ngày
- [ ] **SLA-CAFE-ATTP-04** | Vệ sinh cá nhân barista (móng, tóc, tạp dề) | 100% đạt | Kiểm tra đầu ca | Hàng ngày
- [ ] **SLA-CAFE-ATTP-05** | Log nhiệt độ ATTP — ghi chép đầy đủ | 100% sổ được ghi | Audit tuần | Hàng tuần

### 5. SLA Trải nghiệm khách (Guest Experience)

- [ ] **SLA-CAFE-GX-01** | Chào khách khi đến quầy | **Trong 15 giây** | Self-audit D | Hàng ngày
- [ ] **SLA-CAFE-GX-02** | Chào tạm biệt khách ra về | 100% bàn gần quầy | Self-audit D | Hàng ngày
- [ ] **SLA-CAFE-GX-03** | Không bàn bẩn bị bỏ qua > 5 phút | 0 bàn | Self-audit D2 | Hàng ngày
- [ ] **SLA-CAFE-GX-04** | Số khiếu nại trực tiếp / tuần | **≤ 2 lần** | Sổ sự cố | Hàng tuần
- [ ] **SLA-CAFE-GX-05** | Số review 1–3 sao / tháng | **≤ 3 review** | Google Maps / FB | Hàng tháng
- [ ] **SLA-CAFE-GX-06** | Xử lý khiếu nại lần đầu | **≤ 5 phút** | Sổ sự cố | Theo sự việc

### 6. SLA Đồng phục & Ngoại hình (Uniform & Appearance)

- [ ] **SLA-CAFE-UNF-01** | Đồng phục barista sạch, đúng quy định | 100% | Self-audit B7 | Hàng ngày
- [ ] **SLA-CAFE-UNF-02** | Bảng tên đeo đúng vị trí | 100% | Kiểm tra đầu ca | Hàng ngày
- [ ] **SLA-CAFE-UNF-03** | Vệ sinh cá nhân (tóc, móng, trang sức) | 100% đạt | Kiểm tra đầu ca | Hàng ngày

### 7. SLA Hao hụt & Kho (Waste & Inventory)

- [ ] **SLA-CAFE-WST-01** | Tỉ lệ hao hụt NVL Cafe (hủy / tổng nhập) | **≤ 3%** | Sổ hủy + nhập kho | Hàng tháng
- [ ] **SLA-CAFE-WST-02** | Tỉ lệ thẻ rung mất / tổng số | **≤ 5%/tháng** | Kiểm kê hàng tháng | Hàng tháng
- [ ] **SLA-CAFE-WST-03** | Kiểm kê cuối ca — NVL khớp sổ | Chênh ≤ 2% | Sổ kiểm kê | Mỗi ca

### 8. Bộ Self-audit hàng ngày (tham chiếu AFS-QA-SOP-001, điều chỉnh cho Cafe)

> Thang điểm: **2** = Đạt | **1** = Chưa đạt | **0** = Không đạt

#### Nhóm A — Hạ tầng & An toàn (tối đa 10 điểm)

- [ ] **A1** | Khu vực quầy pha chế sạch, không bừa bộn | /2
- [ ] **A2** | Sàn khu khách không trơn trượt, không vật cản | /2
- [ ] **A3** | Bàn ghế chắc chắn, sạch sẽ | /2
- [ ] **A4** | Nhà vệ sinh sạch (kiểm tra qua) | /2
- [ ] **A5** | Không có cành cây / vật nguy hiểm trên khu ngồi | /2
- **Tổng A: ___/10**

#### Nhóm B — Vệ sinh & Hình thức (tối đa 12 điểm)

- [ ] **B1** | Mặt bàn sạch, không rác | /2
- [ ] **B2** | Ghế xếp gọn, đúng layout | /2
- [ ] **B3** | Máy pha cafe + dụng cụ barista vệ sinh | /2
- [ ] **B4** | Khu vực kho NVL ngăn nắp | /2
- [ ] **B5** | Thùng rác không đầy | /2
- [ ] **B6** | Đồng phục nhân viên sạch, đúng quy định | /2
- **Tổng B: ___/12**

#### Nhóm C — Sản phẩm & Vận hành (tối đa 12 điểm)

- [ ] **C1** | NVL đầu ca đủ theo par level | /2
- [ ] **C2** | Tem nhãn đầy đủ trên BTP trong tủ mát | /2
- [ ] **C3** | Không NVL quá HSD trong khu làm việc | /2
- [ ] **C4** | Thẻ rung đủ, sạc đầy | /2
- [ ] **C5** | POS hoạt động bình thường | /2
- [ ] **C6** | Nhiệt độ tủ mát/tủ đông đạt chuẩn | /2
- **Tổng C: ___/12**

#### Nhóm D — Trải nghiệm khách (tối đa 8 điểm)

- [ ] **D1** | Khách được chào trong 15 giây | /2
- [ ] **D2** | Không bàn bẩn > 5 phút | /2
- [ ] **D3** | Không khách chờ > 3 phút chưa phục vụ | /2
- [ ] **D4** | Không sự cố chưa ghi nhận | /2
- **Tổng D: ___/8**

> **Tổng tối đa: 42 điểm**
> - 38–42: ✅ Xuất sắc
> - 33–37: 🟡 Đạt
> - 27–32: 🟠 Cần cải thiện — báo OM cuối ngày
> - < 27: 🔴 Không đạt — báo OM ngay

### 9. KPI tổng hợp BU Cafe Thơm & AirDream Cafe

- [ ] **Dịch vụ** | SLA tổng hợp (% order đúng giờ) | ≥ 90% | Tuần
- [ ] **Dịch vụ** | Điểm self-audit TB | ≥ 35/42 | Tuần
- [ ] **Dịch vụ** | Khiếu nại trực tiếp / tuần | ≤ 2 lần | Tuần
- [ ] **Dịch vụ** | Review 1–3 sao / tháng | ≤ 3 | Tháng
- [ ] **ATTP** | Sự cố VSATTP | 0 | Tháng
- [ ] **ATTP** | NVL hết HSD trong khu làm việc | 0 | Tháng
- [ ] **Nhân sự** | Tỉ lệ đến đúng giờ | ≥ 95% | Tuần
- [ ] **Nhân sự** | Báo cáo Zalo đúng & đủ | 100% | Tuần
- [ ] **Hao hụt** | Tỉ lệ hao hụt NVL | ≤ 3% | Tháng

---

## PHẦN II — SLA BU NHÀ HÀNG THƠM

> *Tham chiếu khung: NQDL-BKL-QA-SOP-001 (QA tổng thể), NQDL-BKL-CS-SOP-001 (Phục vụ khách), NQDL-BKL-FB-SOP-001 (F&B Standards), NQDL-BKL-SEC-SOP-001 (An toàn vệ sinh)*

### 1. SLA Đón tiếp & Xếp chỗ (Greeting & Seating)

- [ ] **SLA-NHT-GRT-01** | Thời gian chào đón khách từ khi vào | **≤ 15 giây** | Camera + giám sát ca | Hàng ngày
- [ ] **SLA-NHT-GRT-02** | Thời gian xếp chỗ từ khi khách đến | **≤ 3 phút** | Sổ ca | Hàng ngày
- [ ] **SLA-NHT-GRT-03** | Cập nhật tình trạng chờ cho khách | Mỗi **10 phút** | Lễ tân | Theo sự việc
- [ ] **SLA-NHT-GRT-04** | Mẫu câu chào khách đến (chuẩn) | 100% nhân viên thuộc | Kiểm tra SM | Hàng tuần
- [ ] **SLA-NHT-GRT-05** | Mẫu câu chào tiễn khách ra về | 100% nhân viên thuộc | Kiểm tra SM | Hàng tuần

### 2. SLA Tốc độ phục vụ món ăn (Food Service Speed)

- [ ] **SLA-NHT-SPD-01** | Thức uống chào mừng / đồ uống gọi riêng | **≤ 3 phút** | POS + sổ ca | Hàng ngày
- [ ] **SLA-NHT-SPD-02** | Món khai vị | **≤ 8–12 phút** | POS + sổ ca | Hàng ngày
- [ ] **SLA-NHT-SPD-03** | Món chính | **≤ 18–25 phút** | POS + sổ ca | Hàng ngày
- [ ] **SLA-NHT-SPD-04** | Tráng miệng | **≤ 10 phút** | POS + sổ ca | Hàng ngày
- [ ] **SLA-NHT-SPD-05** | Món > 25 phút — phải giải thích trước cho khách | 100% | Sổ order | Hàng ngày
- [ ] **SLA-NHT-SPD-06** | SLA tổng hợp (% order đúng giờ) | **≥ 90%** | POS CUKCUK | Hàng tuần
- [ ] **SLA-NHT-SPD-07** | Thời gian ghi order từ khi khách ngồi | **≤ 3–8 phút** | Sổ ca | Hàng ngày

### 3. SLA Kiểm soát nhiệt độ (Temperature Control)

- [ ] **SLA-NHT-TMP-01** | Nhiệt độ món nóng khi phục vụ | **≥ 65°C** | Nhiệt kế đầu dò | Mỗi mẻ / ngẫu nhiên
- [ ] **SLA-NHT-TMP-02** | Nhiệt độ món lạnh / gỏi / salad | **≤ 5°C** (trước khi ra món) | Nhiệt kế | Mỗi mẻ
- [ ] **SLA-NHT-TMP-03** | Nhiệt độ tủ mát bảo quản NVL | **0–5°C** | Log nhiệt độ | 4 lần/ngày
- [ ] **SLA-NHT-TMP-04** | Nhiệt độ tủ đông | **≤ -18°C** | Log nhiệt độ | 4 lần/ngày
- [ ] **SLA-NHT-TMP-05** | Nhiệt độ chế biến: thịt | Tâm ≥ **75°C** | Nhiệt kế đầu dò | Mỗi mẻ
- [ ] **SLA-NHT-TMP-06** | Nhiệt độ chế biến: hải sản | Tâm ≥ **65°C** | Nhiệt kế đầu dò | Mỗi mẻ
- [ ] **SLA-NHT-TMP-07** | Chuỗi lạnh (cold chain) — NVL từ kho → bếp | Không đứt gãy | Log + self-audit | Hàng ngày

### 4. SLA Trình bày & Chất lượng món (Presentation & Quality)

- [ ] **SLA-NHT-PRS-01** | Món đúng Recipe Card (định lượng, trang trí) | 100% | Kiểm tra Chef + SM | Hàng ngày
- [ ] **SLA-NHT-PRS-02** | Bát/đĩa không sứt mẻ, sạch | 100% | Self-audit | Hàng ngày
- [ ] **SLA-NHT-PRS-03** | Giới thiệu tên món khi phục vụ | 100% | Giám sát ca | Hàng ngày
- [ ] **SLA-NHT-PRS-04** | Món ra đúng thứ tự (khai vị → chính → tráng miệng) | 100% | Sổ order | Hàng ngày

### 5. SLA Vệ sinh & ATTP (Food Safety & Hygiene)

- [ ] **SLA-NHT-ATTP-01** | Sự cố VSATTP (ngộ độc, dị ứng y tế) | **0 lần/tháng** | Sổ sự cố | Tháng
- [ ] **SLA-NHT-ATTP-02** | NVL hết HSD trong khu bếp | **0 lần** | Tự kiểm + audit | Hàng ngày
- [ ] **SLA-NHT-ATTP-03** | Thớt/dao theo màu (HACCP) | 100% tuân thủ | Audit tuần | Hàng tuần
- [ ] **SLA-NHT-ATTP-04** | Log nhiệt độ ATTP — ghi chép đầy đủ | 100% | Audit tuần | Hàng tuần
- [ ] **SLA-NHT-ATTP-05** | Vệ sinh bếp cuối ca | Đạt checklist HACCP | Checklist A7 | Hàng ngày
- [ ] **SLA-NHT-ATTP-06** | Vệ sinh cá nhân NV (móng, tóc, đồng phục) | 100% | Kiểm tra đầu ca | Hàng ngày

### 6. SLA Xử lý khiếu nại (Complaint Handling)

- [ ] **SLA-NHT-CMP-01** | Phản hồi khiếu nại tại chỗ | **≤ 5 phút** | Sổ sự cố | Theo sự việc
- [ ] **SLA-NHT-CMP-02** | Phản hồi review tiêu cực online | **≤ 24 giờ** | Google / FB | Theo sự việc
- [ ] **SLA-NHT-CMP-03** | Phản hồi email khiếu nại | **≤ 48 giờ** | Email | Theo sự việc
- [ ] **SLA-NHT-CMP-04** | Quy trình LEARN được áp dụng | 100% | Sổ sự cố + giám sát | Theo sự việc
- [ ] **SLA-NHT-CMP-05** | Tổng khiếu nại trực tiếp / tuần | **≤ 3 lần** | Sổ sự cố | Hàng tuần

### 7. SLA Đồng phục & Ngoại hình (Uniform & Appearance)

- [ ] **SLA-NHT-UNF-01** | Đồng phục FOH sạch, đúng quy định | 100% | Kiểm tra đầu ca | Hàng ngày
- [ ] **SLA-NHT-UNF-02** | Đồng phục BOH sạch, đúng quy định | 100% | Kiểm tra Chef | Hàng ngày
- [ ] **SLA-NHT-UNF-03** | Bảng tên đeo đúng vị trí (tim trái) | 100% | Kiểm tra đầu ca | Hàng ngày

### 8. SLA Thanh toán & Tiễn khách (Payment & Farewell)

- [ ] **SLA-NHT-PAY-01** | Thời gian thanh toán từ khi khách yêu cầu | **≤ 3 phút** | POS | Hàng ngày
- [ ] **SLA-NHT-PAY-02** | Chào tiễn khách — mẫu câu chuẩn | 100% | Giám sát ca | Hàng ngày
- [ ] **SLA-NHT-PAY-03** | Trả lại tiền thừa/thẻ bằng 2 tay | 100% | Giám sát | Hàng ngày

### 9. SLA Kiểm soát lãng phí (Waste Control)

- [ ] **SLA-NHT-WST-01** | Tỉ lệ lãng phí thực phẩm / doanh thu | **≤ 3%** | Nhật ký Waste | Tháng
- [ ] **SLA-NHT-WST-02** | Hư hỏng NVL / tồn kho | **≤ 1%** | Kiểm kê | Tuần
- [ ] **SLA-NHT-WST-03** | FIFO đúng quy trình | 100% | Audit tuần | Hàng tuần

### 10. Kiểm toán chất lượng tuần (tham chiếu BKL-QA-SOP-001, điều chỉnh cho NHT)

#### Bếp (30 điểm)

- [ ] Nhiệt độ tủ lạnh/đông | 5
- [ ] Vệ sinh bề mặt/thiết bị | 5
- [ ] FIFO đúng quy trình | 5
- [ ] Thớt/dao theo màu | 5
- [ ] Đồng phục/vệ sinh cá nhân | 5
- [ ] Ghi chép log đầy đủ | 5

#### Phục vụ (30 điểm)

- [ ] Bàn ghế sạch sẽ | 5
- [ ] Dụng cụ ăn uống vệ sinh | 5
- [ ] Đồng phục nhân viên | 5
- [ ] Thái độ phục vụ | 10
- [ ] Thời gian phục vụ (SLA) | 5

#### Bar/Thu ngân (20 điểm)

- [ ] Vệ sinh khu vực | 5
- [ ] Đồ uống trong hạn | 5
- [ ] POS hoạt động | 5
- [ ] Xử lý thanh toán | 5

#### Kho/Nhận hàng (20 điểm)

- [ ] Sắp xếp FIFO | 5
- [ ] Nhiệt độ bảo quản | 5
- [ ] Nhãn mác/ngày tháng | 5
- [ ] Vệ sinh kho | 5

**Tổng: ___/100**

> **Thang đánh giá:**
> - 90–100: ✅ Xuất sắc — Tuân thủ thương hiệu ≥ 95%
> - 80–89: 🟢 Tốt — Tuân thủ thương hiệu ≥ 85%
> - 70–79: 🟡 Đạt — Tuân thủ thương hiệu ≥ 75%
> - < 70: 🔴 Không đạt — Cần cải tiến ngay

### 11. KPI tổng hợp BU Nhà hàng Thơm

- [ ] **Dịch vụ** | SLA tổng hợp (% order đúng giờ) | ≥ 90% | Tuần
- [ ] **Dịch vụ** | CSAT (Hài lòng khách hàng) | ≥ 4.5/5.0 | Tháng
- [ ] **Dịch vụ** | NPS | ≥ 35 (Q1) → ≥ 50 (Q4) | Quý
- [ ] **Dịch vụ** | Khiếu nại tại chỗ phản hồi ≤ 5 phút | 100% | Theo sự việc
- [ ] **Dịch vụ** | Review tiêu cực phản hồi ≤ 24h | 100% | Theo sự việc
- [ ] **ATTP** | Sự cố VSATTP | 0 | Tháng
- [ ] **ATTP** | NVL hết HSD trong bếp | 0 | Tháng
- [ ] **ATTP** | Tuân thủ HACCP (thớt/dao/log) | ≥ 95% | Tuần
- [ ] **Tài chính** | Food Cost | 32–35% | Tháng
- [ ] **Tài chính** | Tỉ lệ lãng phí | ≤ 3% DT | Tháng
- [ ] **Nhân sự** | Tỉ lệ đến đúng giờ | ≥ 95% | Tuần
- [ ] **Nhân sự** | Kiến thức sản phẩm (test hàng tháng) | ≥ 90% | Tháng
- [ ] **Thương hiệu** | Tuân thủ Brand Guidelines | ≥ 95% | Quý

### 12. Quy trình NPS & Quản lý phản hồi (tham chiếu BKL)

- [ ] QR code tại bàn | Sau mỗi bữa ăn | Tự động
- [ ] Khảo sát trực tiếp (VIP) | Khách đoàn / tiệc | Trong bữa
- [ ] Google Maps / FB | Theo dõi hàng ngày | Review xấu: ≤ 24h
- [ ] Đường dây nóng / email | Khi khách chủ động | ≤ 48h

**Quy trình HEART xử lý khiếu nại:**
1. **H**ear — Lắng nghe, không ngắt lời
2. **E**mpathize — Đồng cảm
3. **A**pologize — Xin lỗi chân thành
4. **R**esolve — Giải quyết ngay
5. **T**hank — Cảm ơn phản hồi

**Thẩm quyền bồi thường:**

- [ ] Nhẹ (món sai, chậm) | Giảm 10–20% hóa đơn | Trưởng ca
- [ ] Trung bình (ATTP nhẹ) | Miễn phí bữa ăn | Quản lý NHT
- [ ] Nghiêm trọng (ATTP nặng) | Hoàn tiền + chứng từ | CEO NQDL

---

## PHẦN III — BẢNG SO SÁNH KHUNG SLA GIỮA CÁC BU

| Tiêu chí | AFS (gốc) | Cafe Thơm & AirDream Cafe | BKL (gốc) | Nhà hàng Thơm |
|----------|-----------|--------------------------|-----------|---------------|
| **Mô hình** | Co-location 2 brand, outdoor, self-service | Cafe + đồ uống nhẹ, có thể indoor/outdoor | Nhà hàng full-service, 1000–1500 khách/ngày | Nhà hàng full-service, ẩm thực |
| **SLA tốc độ món chính** | ≤ 7 phút (Pizza) | ≤ 5 phút (pha chế) | ≤ 25 phút (món chính) | ≤ 25 phút (món chính) |
| **SLA nhiệt nóng** | ≥ 65°C | ≥ 65°C | ≥ 65°C | ≥ 65°C |
| **SLA nhiệt lạnh** | ≤ 5°C | ≤ 5°C | ≤ 5°C | ≤ 5°C |
| **Chào khách** | ≤ 15 giây (quầy) | ≤ 15 giây (quầy) | ≤ 15 giây (lễ tân) | ≤ 15 giây (lễ tân) |
| **Xử lý khiếu nại** | ≤ 5 phút | ≤ 5 phút | ≤ 5 phút (tại chỗ) | ≤ 5 phút (tại chỗ) |
| **Self-audit/ngày** | 52 điểm | 42 điểm | — (audit tuần 100 điểm) | 100 điểm (audit tuần) |
| **Food Cost target** | 35% | 28–35% (cafe) | 32–35% | 32–35% |
| **NPS mục tiêu** | — (chưa có baseline) | — (chưa có baseline) | ≥ 35 → ≥ 50 | ≥ 35 → ≥ 50 |
| **Hao hụt target** | ≤ 3% (cafe) | ≤ 3% | ≤ 3% DT | ≤ 3% DT |

---

## PHẦN IV — GHI CHÚ ÁP DỤNG

### 1. Baseline & Điều chỉnh mục tiêu
- Các mục tiêu `[x]` cần điền sau **1–3 tháng vận hành thực tế** để có baseline.
- Không đặt mục tiêu cứng khi chưa có dữ liệu — đặc biệt với Cafe Thơm & AirDream Cafe (brand mới tách).

### 2. Phân biệt Compliance vs Service Commitment
Theo guardrail G2 (INV-C — Service Governance):
- **Compliance** (bắt buộc theo luật/HACCP): Nhiệt độ ATTP, VSATTP, thớt/dao theo màu → **không thoả hiệp**.
- **Service Commitment** (cam kết trải nghiệm): Thời gian chào, tốc độ ra món, NPS → **có thể điều chỉnh** theo baseline.

### 3. Traceability (INV-C — G4)
Mỗi SLA-ID trong bảng trên có thể trace về SOP gốc:
- `SLA-CAFE-*` → NQDL-AFS-FNB-SOP-007/009/010, AFS-FOH-SOP-001, AFS-QA-SOP-001/004
- `SLA-NHT-*` → NQDL-BKL-CS-SOP-001, BKL-FB-SOP-001, BKL-QA-SOP-001, BKL-SEC-SOP-001

### 4. Chu kỳ đánh giá

| Chu kỳ | Nội dung | Người đánh giá |
|--------|----------|---------------|
| Hàng ngày | Self-audit + log nhiệt độ + sự cố | SM / Trưởng ca |
| Hàng tuần | Điểm audit + SLA + khiếu nại | OM |
| Hàng tháng | Tổng hợp tất cả KPI + Guardrails | OM → BOD |
| Hàng quý | Review KPI vs mục tiêu + điều chỉnh | BOD |

### 5. Kết nối KPI với đánh giá nhân sự

| Tổng KPI | Đánh giá | Hành động |
|----------|----------|-----------|
| Đạt ≥ 80% chỉ tiêu | Hoàn thành xuất sắc | Ghi nhận, thưởng |
| Đạt 60–79% chỉ tiêu | Hoàn thành | Nhắc nhở điểm yếu |
| Đạt < 60% chỉ tiêu | Chưa hoàn thành | Coaching với OM; cảnh báo nếu tái lặp |

---

*Người lập: Nguyễn Tuấn Kiệt — OM NQDL*
*Ngày lập: 15/08/2026*
*Trạng thái: DRAFT — trình OM Trần Nguyên Bảo rà soát trước khi trình CEO/COO*
