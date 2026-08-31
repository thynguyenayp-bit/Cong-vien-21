---
tags: [resource, checklist, airdream, afs, ad2, van-hanh, sop]
status: active
owner: "Nguyễn Tuấn Kiệt"
updated: "2026-07-23"
---

# AFS — Bộ Checklist Vận hành Thực địa

> Áp dụng cho **AirDream Forest Station (AD2 / AFS)**. Mục tiêu: biến SOP từ "có trên giấy" thành "chạy ổn định mỗi ngày". Mỗi checklist có mã, tần suất, người làm, chuẩn đầu ra và link SOP gốc.

## Liên kết hệ thống

- BU theo dõi: [[BU - AirDream 2]]
- Kiến trúc 3 tầng SOP: [[Framework — SOP Airdream Forest Station]]
- SOP gốc:
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-OPS-SOP-001_Core_Operations.md|NQDL-AFS-OPS-SOP-001 Vận hành hàng ngày]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-OPS-SOP-003_Forest_Safety_Maintenance.md|NQDL-AFS-OPS-SOP-003 An toàn rừng thông]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-OPS-CHK-001_Opening_Checklist.md|NQDL-AFS-OPS-CHK-001 Checklist khai trương]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-OPS-CHK-002_Closing_Checklist.md|NQDL-AFS-OPS-CHK-002 Checklist kết ca]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-FNB-SOP-001_Food_Service_Operations.md|NQDL-AFS-FNB-SOP-001 Phục vụ đồ ăn]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-HR-SOP-001_Staff_Recruitment_Onboarding.md|NQDL-AFS-HR-SOP-001 Tuyển dụng & tiếp nhận]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/NQDL-AFS-BTP-SOP-001_BTP_Receiving_Operations.md|NQDL-AFS-BTP-SOP-001 Nhận hàng chuyển kho]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/AirDream_Cafe/NQDL-AIR-BAR-SOP-001_Beverage_Recipe_Cards.md|NQDL-AIR-BAR-SOP-001 Công thức pha chế AirDream]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/02_Nhat_Quang_Da_Lat/Operations/NQDL-OPS-SOP-001_Shift_Handover_Process.md|NQDL-OPS-SOP-001 Bàn giao ca NQDL]]
  - [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/02_Nhat_Quang_Da_Lat/Operations/NQDL-OPS-SOP-005_Bar_Beverage_Counter_Operations.md|NQDL-OPS-SOP-005 Quầy bar / quầy nước]]

## 1. Logic tổ chức trong SecondBrain + SOP

### 1.1 Vị trí file này
- Đây là **Resource** — kho mẫu checklist để tra cứu và copy.
- BU cụ thể được theo dõi trong **Area** `[[BU - AirDream 2]]`.
- Các báo cáo hàng ngày ghi vào **Daily Note** (`NQH/05 - Daily Notes/YYYY-MM-DD.md`).

### 1.2 Cách dùng mỗi ngày
1. Site Manager hoặc Trưởng ca copy phần checklist tương ứng vào Daily Note (hoặc in ra giấy A5 mang theo ca).
2. Mỗi mục là task `-[ ]` trong Obsidian, có thể gán `👤[[Tên]]` và `📅 YYYY-MM-DD`.
3. Foto chứng từ gửi group Zalo theo SOP; link/text báo cáo paste ngắn vào Daily Note.
4. Cuối tuần, dùng `[[Template - Weekly Review]]` để rà lại task chưa xong.

### 1.3 Nguyên tắc checklist có hiệu lực
- **Một mục = một hành động cụ thể** (không viết chung chung như "vệ sinh sạch").
- **Có chuẩn pass/fail rõ ràng** (ví dụ: "không còn vết bẩn nhìn bằng mắt thường").
- **Có ảnh / chữ ký / số liệu** chứng minh khi cần audit.
- **Ai làm (R), ai ký xác nhận (A)** phải ghi rõ.

### 1.4 Trạng thái SOP hiện tại (lưu ý)
- PR #33 đang chờ đóng blocker F1 (xoá SĐT cá nhân trong escalation matrix) trước khi ban hành chính thức.
- Một số SOP còn **PLANNED**: OPS-SOP-002 Vệ sinh & ATTP, OPS-SOP-004 POS, OPS-SOP-005 Kiểm soát tiền mặt, FIN-SOP-001 Sổ tay kế toán. Các checklist bên dưới đã tạo mục tạm dựa trên nội dung trong Core Operations và Closing Checklist; khi SOP chính thức ban hành sẽ cập nhật lại.

## 2. Tổng hợp checklist theo tần suất

| Mã              | Tên checklist                                  | Tần suất                      | Người làm (R)                     | Giám sát / Ký (A)        | Thời gian         | Ref SOP chính                             |
| --------------- | ---------------------------------------------- | ----------------------------- | --------------------------------- | ------------------------ | ----------------- | ----------------------------------------- |
| **AFS-CHK-D01** | Mở ca — kiểm tra an toàn + setup 2 xe buýt     | Mỗi ca mở cửa                 | NV ca M1 + Site Manager           | Site Manager             | 6:30–7:30         | OPS-SOP-001, OPS-SOP-003                  |
| **AFS-CHK-D02** | Kiểm tra an toàn rừng thông                    | Hàng ngày (sáng + tối)        | 2 NV được đào tạo                 | Site Manager             | 6:00 & 19:00      | OPS-SOP-003                               |
| **AFS-CHK-D03** | Vận hành trong ca — F&B, phục vụ, vệ sinh rừng | Liên tục / theo ca            | Barista + NV đồ ăn + FOH          | Site Manager / Trưởng ca | 7:30–19:30        | OPS-SOP-001, FNB-SOP-001, AIR-BAR-SOP-001 |
| **AFS-CHK-D04** | Giữa ca — kiểm kê nhanh & reset                | 13:00 hàng ngày               | NV ca M1 hoặc M2                  | Site Manager             | 13:00–13:20       | OPS-SOP-001                               |
| **AFS-CHK-D05** | Kết ca — POS, tiền mặt, vệ sinh, báo cáo       | Mỗi ca đóng cửa               | NV ca M3                          | Site Manager             | 18:30–19:30       | OPS-CHK-002, OPS-SOP-001                  |
| **AFS-CHK-D06** | Kiểm kê hàng ngày — NVL + vật tư + tiền mặt   | Cuối mỗi ca / giao ca         | Thu ngân + NV ca đóng             | Site Manager             | 10–15 phút        | OPS-SOP-004 (PLANNED), OPS-SOP-005 (PLANNED) |
| **AFS-CHK-W01** | Vệ sinh sâu & bảo trì tuần                     | Thứ 6 hàng tuần               | Cả team AFS                       | Site Manager             | 1.5–2 giờ         | OPS-SOP-001 (§5.1)                        |
| **AFS-CHK-W02** | Review vận hành tuần                           | Thứ 2 hàng tuần               | Site Manager + OM / BOD           | OM / BOD                 | 30–45 phút        | OPS-SOP-001, HR-SOP-001                   |
| **AFS-CHK-M01** | Kiểm tra PCCC & thiết bị an toàn               | Ngày 5 hàng tháng             | Site Manager + kỹ thuật           | OM / BOD                 | 1 giờ             | OPS-SOP-003                               |
| **AFS-CHK-M02** | Kiểm kê & đối soát tháng                       | Ngày cuối tháng               | Site Manager + Thu ngân + Kế toán | CFO / Kế toán trưởng     | Theo kế hoạch T+7 | FIN-SOP-001 (PLANNED), OPS-CHK-002        |
| **AFS-CHK-Q01** | Audit tuân thủ quý                             | Quý 1 lần                     | QA Team + OM / BOD                | COO NQDL                 | 1 buổi            | QA-SOP-005 Framework Implementation Audit |
| **AFS-CHK-E01** | Sơ tán khẩn cấp / sự kiện đặc biệt             | Theo cảnh báo / trước sự kiện | Tất cả NV tại ca                  | Site Manager             | Ngay lập tức      | OPS-SOP-003, NQDL-OPS-SOP-001             |

## 3. Chi tiết từng checklist

### AFS-CHK-D01 — Mở ca (6:30–7:30)
**Người làm:** NV ca M1 (2 người phân công song song).  
**Giám sát / Ký xác nhận:** Site Manager.  
**Mục tiêu:** Sẵn sàng đón khách đúng 7:30; 0 lỗi an toàn trước mở cửa.

#### 3.1 An toàn rừng — BẮT BUỘC trước mọi việc
- [ ] Kiểm tra toàn bộ khu rừng 4,000m² (lộ trình: cổng → đường chính → 4 trailer → khu bàn ghê → rừng sâu → cổng).
- [ ] Ghi nhận cành khô, cành nứt, cành thấp <5m gần chỗ ngồi.
- [ ] Kiểm tra thời tiết trên app (gió, mưa, giông bão).
- [ ] Nếu phát hiện nguy hiểm → khoanh vùng 5m, cắm biển cảnh báo, báo Site Manager trước 7:30.
- [ ] Chụp ảnh toàn cảnh khu rừng, lưu vào nhóm chat / Daily Note.

#### 3.2 Thiết bị & hệ thống
- [ ] Bật máy POS 2 quầy, đăng nhập CUKCUK, test in bill.
- [ ] Bật 2 máy xay cà phê (Robusta + Arabica), máy pha cà phê warm-up 10 phút.
- [ ] Bật máy pha nước sôi, 2 máy đánh, cân tiểu ly (reset về 0).
- [ ] Kiểm tra WiFi/LAN hoạt động; báo IT nếu lỗi.
- [ ] Kiểm tra điện xe buýt, cửa/khóa trailer.

#### 3.3 Setup trạm pha chế
- [ ] **Trạm Matcha:** chasen, chawan, cân tiểu ly, bột matcha/cacao, syrup đường, sữa đặc đủ vị trí.
- [ ] **Trạm Trà:** 4 bình trà (Oolong, Lài, Đen, Atiso) ở nhiệt độ phòng; trà sữa + chân trâu trong tủ mát.
- [ ] **Trạm Cà phê:** portafilter, tamper, beaker 75ml, khăn lau sạch.
- [ ] **Tủ mát:** kem matcha, kem muối, cam, chanh, xoài, xí muội, mứt các loại còn đủ dùng và đúng HSD.

#### 3.4 Vật tư tiêu hao & khu khách ngồi
- [ ] Ly nhựa, ly giấy, nắp ly, ống hút, quai nilong đủ cho ca.
- [ ] Khăn giấy, gạt tàn thuốc đặt đúng vị trí khu ngoài trời.
- [ ] Bàn ghế khu rừng xếp ngay ngắn: 1 bàn / 2 ghế; 2 bàn / 3–4 ghế (tùy khu).
- [ ] 4 trailer sạch, cửa mở, đèn fairy light tắt (chờ 17:00 bật).

#### 3.5 Xác nhận
- [ ] Site Manager ký xác nhận vào Daily Note / form mở ca.
- [ ] Ghi thời gian mở ca thực tế và số NV có mặt.

---

### AFS-CHK-D02 — Kiểm tra an toàn rừng thông (2 lần/ngày)
**Người làm:** 2 NV được đào tạo (không đi một mình).  
**Giám sát / Ký:** Site Manager.  
**Thời gian:** 6:00 sáng (trước mở cửa) + 19:00 tối (trước khi rời đi).  
**Mục tiêu:** 0 sự cố an toàn; mọi nguy hiểm được khoanh vùng trước khi khách vào.

- [ ] Đi theo lộ trình cố định (cổng → đường chính → 4 trailer → khu bàn ghế → rừng sâu → cổng).
- [ ] Nhìn từ dưới lên: cành lá vàng/khô, cành nứt, cành gãy lơ lửng.
- [ ] Chú ý cành thấp <5m gần đường đi / chỗ ngồi khách.
- [ ] Sau mưa / gió mạnh: kiểm tra thêm lần nữa ngay khi đến ca.
- [ ] Phân loại và xử lý:
  - Cành chết nhỏ (<5cm): thu dọn trong ngày.
  - Cành chết lớn (≥5cm) thấp <5m: khoanh vùng 5m, gọi cắt tỉa trong 4 giờ.
  - Cành gãy lơ lửng: khoanh vùng rộng, cấm khách vào, gọi cắt tỉa ngay.
- [ ] Chụp ảnh bất kỳ cành đáng ngờ; ghi vào nhật ký an toàn.
- [ ] Kiểm tra thời tiết, cập nhật cảnh báo giông bão.
- [ ] Site Manager xác nhận đã đọc báo cáo và ký.

---

### AFS-CHK-D03 — Vận hành trong ca (7:30–19:30)
**Người làm:** Barista, NV quầy đồ ăn, FOH lưu động.  
**Giám sát:** Site Manager / Trưởng ca.  
**Mục tiêu:** Doanh thu ≥15 triệu/ngày (2 quầy); thời gian phục vụ ≤3 phút/đồ uống, ≤5 phút/burrito; NPS ≥8.5.

#### 3.1 F&B — Quầy nước & Camper Grub
- [ ] Pha chế đúng công thức [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/AirDream_Cafe/NQDL-AIR-BAR-SOP-001_Beverage_Recipe_Cards.md|AIR-BAR-SOP-001]].
- [ ] Burrito / snacks ra món ≤5 phút, nhân nóng ≥65°C.
- [ ] Dùng FIFO cho NVL; không dùng NVL quá hạn.
- [ ] Vệ sinh lò nướng sau mỗi 2 pizza; thay giấy bạc khi đen/bẩn.
- [ ] Lau sàn xe buýt 2 mỗi 3 giờ.

#### 3.2 Phục vụ khách
- [ ] Chủ động chào khách, tư vấn đúng bảng kiến thức sản phẩm (Arabica/Robusta/Matcha/Trà).
- [ ] Khi đông: phát thẻ rung (01–15), hướng dẫn khách tự lấy hàng.
- [ ] Thu dọn bàn theo tần suất: vắng khách 60–90 phút/lần; đông khách 30–45 phút/lần.
- [ ] Vệ sinh khu rừng bằng phương pháp "quét lưới" (hàng ngang, lối đi 50cm).
- [ ] Nhắc nhở khách: cấm lửa, không hút thuốc trong rừng, thú cưng/chụp ảnh theo quy định.

#### 3.3 Kiểm soát chất lượng & ATTP
- [ ] Rửa tay trước khi pha chế / chế biến; sau khi chạm tiền/rác.
- [ ] Nhiệt độ đồ nóng 65–75°C; đồ lạnh 4–8°C.
- [ ] Trái cây hư → lập biên bản hủy NVL, có Site Manager ký.
- [ ] Không để đồ ăn >8 giờ ở nhiệt độ phòng.

#### 3.4 POS & thu ngân
- [ ] Mọi order phải có bill trên CUKCUK (không order miệng không ghi).
- [ ] Cuối mỗi giao dịch: đối chiếu tiền mặt vs POS.
- [ ] Khi POS lỗi → chuyển ngay sổ tay dự phòng, nhập bù trong 24 giờ.

---

### AFS-CHK-D04 — Giữa ca (13:00)
**Người làm:** NV ca M1 hoặc M2.  
**Giám sát:** Site Manager.  
**Thời gian:** 13:00–13:20.  
**Mục tiêu:** Không đứt gãy dịch vụ giữa 2 ca; NVL không thiếu giữa ca.

- [ ] Kiểm tra nhanh khu rừng sau giờ cao điểm trưa.
- [ ] Kiểm kê tồn kho 2 xe buýt (ly, vật tư, NVL chính).
- [ ] Rửa dụng cụ tích tụ tại xe buýt.
- [ ] Lau dọn trailer và khu bàn ghế ngoài trời.
- [ ] Cập nhật nhật ký ca: số khách, vấn đề gặp phải, NVL cần đặt.
- [ ] Đặt hàng trái cây / NVL giao trong 1 ngày nếu sắp hết.

---

### AFS-CHK-D05 — Kết ca (18:30–19:30)
**Người làm:** NV ca M3 (phân công: 1 người POS/tiền, 1 người vệ sinh, 1 người ngoài).  
**Giám sát / Ký:** Site Manager.  
**Mục tiêu:** Kết ca đúng 19:30; tiền mặt khớp POS; khu vực sạch sẽ, an toàn.

#### 5.1 Thông báo khách
- [ ] 18:00 thông báo quán đóng 19:30.
- [ ] 18:30 thông báo last order; ngừng nhận order mới.

#### 5.2 Vệ sinh khu pha chế (30 phút)
**Khu cà phê:**
- [ ] Mở máy pha chế độ nước nóng, chà sạch nơi ra cà phê.
- [ ] Xịt 2 vòi hơi nước cho hết sữa/cặn; để vòi tự ngắt.
- [ ] Quét cặn cà phê trên tamper, ống máy xay.
- [ ] Rửa các CCDC: tấm cao su, khay inox, ly thủy tinh, tay pha.
- [ ] Tắt máy pha, máy xay.

**Khu trà:**
- [ ] Tháo nắp bình syrup đường, sữa đặc để rửa.
- [ ] Bọc miệng bình squeeze, hũ xí muội, bát chanh, hộp xoài.
- [ ] Đậy nắp kem muối, kem matcha, các loại mứt; hộp chân trâu đậy kín.
- [ ] Chai mứt lựu, chai syrup lựu về đúng vị trí / tủ mát.
- [ ] Lau máy đánh cầm tay bằng khăn ẩm.
- [ ] Kiểm tra tồn trái cây tươi (xoài, cam, dừa, chanh) → đặt hàng nếu hết.

**Khu matcha:**
- [ ] Rửa thìa cacao/matcha; đậy nắp kín 2 hũ bột, bảo quản nhiệt độ phòng.
- [ ] Lau cân tiểu ly.
- [ ] Rửa bát pha matcha, chasen, giá đựng, bình nhựa.

**Vệ sinh tổng:**
- [ ] Rửa sạch CCDC, để ráo, cất lên nóc máy pha (nhỏ trước, lớn sau).
- [ ] Xịt nước xịt kính lau bề mặt đá, kính máy pha, bàn inox.
- [ ] Lau bàn gỗ, xung quanh bồn rửa bằng khăn đã giặt.
- [ ] Khăn lau ngâm nước sôi 5 phút → giặt lại → phơi khô.
- [ ] Đảm bảo không còn vết bẩn nhìn bằng mắt thường.

#### 5.3 POS & tiền mặt (5 phút)
- [ ] Xem báo cáo tổng hợp ca, chụp màn hình + in hóa đơn.
- [ ] In báo cáo kết ca; khoanh tròn số ly các sản phẩm nóng (ly giấy).
- [ ] Đếm tiền mặt trong két; để lại 1.000.000đ tiền nhỏ lẻ.
- [ ] Ghi tay: giờ ca, ngày, tổng tiền, tiền chuyển khoản, tiền mặt, tiền mặt thực nhận, số tờ tiền.
- [ ] Nộp tiền mặt cho thu ngân BKL.
- [ ] Tắt nguồn POS, tắt bóng đèn tủ lạnh.

#### 5.4 Kiểm kê số lượng (5 phút)
- [ ] Đếm ly giấy, ly nhựa còn lại → ghi số → báo thủ kho.
- [ ] Kiểm tra sữa, kem béo, bột béo, các loại trà → báo mua nếu gần hết.

#### 5.5 Vệ sinh khu bên ngoài & khóa cửa (10 phút)
- [ ] Dọn ly dơ, ống hút, vỏ giấy trong toàn bộ khu khách ngồi.
- [ ] Xếp lại bàn ghế ngay ngắn đúng layout.
- [ ] Tắt điện khu khách, tắt máy xông hơi nước và đậy nắp.
- [ ] Rút điện cabin bán đồ ăn + cabin pha nước.
- [ ] Cho loa, ghế nhân viên vào cabin pha nước.
- [ ] Đóng cửa sổ, khóa cửa cabin pha nước.
- [ ] Xách bao rác đi đổ đúng nơi tập kết.
- [ ] Kéo và khóa cửa sắt ra vào.

#### 5.6 Báo cáo Zalo
**Group Báo cáo Doanh thu:**
- [ ] Chụp màn hình kết ca POS.
- [ ] Chụp tờ báo cáo kết ca.
- [ ] Chụp tờ báo cáo doanh thu.
- [ ] Chụp tờ doanh thu theo mặt hàng.
- [ ] Chụp tất cả ảnh chuyển khoản của ca (nội dung CK + hóa đơn).

**Group Nhân viên:**
- [ ] Chụp hiện trạng cabin sau khi dọn.
- [ ] Chụp hiện trạng chỗ ngồi khách sau khi dọn.

#### 5.7 Xác nhận cuối
- [ ] Site Manager ký xác nhận kết ca.
- [ ] Ghi nhận sự cố / vấn đề cần ca sau xử lý.

---

### AFS-CHK-D06 — Kiểm kê hàng ngày (cuối ca / giao ca)
**Người làm:** Thu ngân + NV ca đang đóng (M3) hoặc NV ca M1/M2 khi giao ca.  
**Giám sát / Ký:** Site Manager.  
**Thời gian:** 10–15 phút (có thể gộp với AFS-CHK-D04 lúc 13:00 hoặc AFS-CHK-D05 lúc 19:00).  
**Mục tiêu:** Số liệu thực tế khớp với POS; không thiếu NVL giữa ca; phát hiện hao hụt / hủy hàng kịp thời.

> **Lưu ý:** Đây là kiểm kê **nhanh theo ca**, khác với kiểm kê chi tiết cuối tháng (AFS-CHK-M02).

#### 6.1 Kiểm kê tiền mặt
- [ ] Đếm tiền mặt trong két trước khi mở ca / sau khi đóng ca.
- [ ] Đối chiếu tiền mặt với báo cáo POS của ca.
- [ ] Ghi rõ: tiền đầu ca, tiền cuối ca, tiền mặt thực nhận, chênh lệch (nếu có).
- [ ] Nếu lệch >100đ → báo Site Manager ngay, ghi lý do ≥20 ký tự (theo DNA 0).
- [ ] Để lại quỹ tiền lẻ đầu ca: **1.000.000đ** (theo OPS-CHK-002); nộp phần dư cho thu ngân BKL.

#### 6.2 Kiểm kê vật tư tiêu hao (ly, nắp, ống hút, túi)
- [ ] Đếm số lượng thực tế: ly giấy, ly nhựa, nắp ly giấy, nắp ly nhựa, ống hút các loại.
- [ ] Đối chiếu số lượng bán trên POS với số lượng xuất thực tế (tính theo định mức mỗi món).
- [ ] Ghi chênh lệch nếu có (vỡ, rơi, tặng khách không ghi bill).
- [ ] Báo thủ kho / Site Manager nếu tồn dưới mức par (dự trữ 1–2 ngày).

#### 6.3 Kiểm kê NVL chính quầy nước
- [ ] **Trà:** 4 bình trà (Oolong, Lài, Đen, Atiso) + trà sữa — ghi số lít còn lại.
- [ ] **Cà phê:** số gram bột Robusta / Arabica còn trong máy xay / hộp.
- [ ] **Matcha / Cacao:** số gram bột còn lại.
- [ ] **Sữa & Kem:** sữa tươi, kem béo, kem muối, kem matcha — ghi số lượng / dung tích.
- [ ] **Mứt & Syrup:** mứt lựu, syrup lựu, mứt chanh dây, mứt tắc, mứt dâu tằm — ghi mức còn.
- [ ] **Trái cây tươi:** xoài, cam, chanh, dừa — ghi số lượng và chất lượng.
- [ ] **Topping:** chân trâu trắng, xí muội.

#### 6.4 Kiểm kê NVL Camper Grub (xe buýt 2)
- [ ] **Burrito:** thịt nướng, bò phô mai, gà sốt chanh dây, xúc xích trứng, nấm bắp, gà lá é, thịt kho mắm ruốc — ghi số phần còn.
- [ ] **Snacks:** khoai tây, gà viên — ghi số phần còn.
- [ ] **Tortilla / bánh mì:** số lượng còn.
- [ ] **Sốt:** truffle, BBQ, chanh dây, mắm ruốc — ghi mức còn.
- [ ] **Dầu chiên:** ghi số lần sử dụng / thay dầu (thay nếu >8 giờ sử dụng).

#### 6.5 Ghi nhận hao hụt & hủy hàng
- [ ] Ghi rõ các mục bị hủy: trái cây hư, NVL quá hạn, đồ chế biến hỏng.
- [ ] Ghi số lượng, lý do, người xác nhận.
- [ ] Lập **biên bản hủy NVL** nếu Site Manager yêu cầu ký.
- [ ] Chụp ảnh chứng từ hủy hàng gửi group Zalo / lưu Daily Note.

#### 6.6 Đối chiếu & báo cáo
- [ ] Tổng hợp số liệu kiểm kê vào form / Daily Note.
- [ ] Gửi báo cáo chênh lệch (nếu có) cho Site Manager trước khi rời ca.
- [ ] Nếu phát hiện thiếu NVL nghiêm trọng → đặt hàng giao trong 1 ngày.

---

### AFS-CHK-W01 — Vệ sinh sâu & bảo trì tuần (Thứ 6)
**Người làm:** Toàn team AFS.  
**Giám sát / Ký:** Site Manager.  
**Thời gian:** 1.5–2 giờ (sau giờ đóng cửa hoặc sáng sớm).  
**Mục tiêu:** Duy trì độ bền CSVC; vệ sinh những góc không làm hàng ngày.

- [ ] Vệ sinh sâu 4 trailer (lau ghế, sàn, cửa sổ, mái che).
- [ ] Vệ sinh sâu 2 xe buýt (trần, khe kẽ, tủ mát, gầm bếp).
- [ ] Kiểm tra cửa/khóa trailer (siết ốc, bôi trơn nếu cần).
- [ ] Kiểm tra điện xe buýt, dây điện, ổ cắm.
- [ ] Kiểm tra bạt che, dù, bàn ghế ngoài trời: ghi nhận hư hỏng cần sửa.
- [ ] Thu dọn lá thông sâu toàn bộ 4,000m².
- [ ] Kiểm tra hệ thống thoát nước, ống nước.
- [ ] Kiểm tra fairy light, đèn trailer — thay bóng đèn cháy.
- [ ] Chụp ảnh before/after; ghi vào nhật ký bảo trì.
- [ ] Lập danh sách hư hỏng cần gọi thợ, gửi OM / BOD.

---

### AFS-CHK-W02 — Review vận hành tuần (Thứ 2)
**Người làm:** Site Manager.  
**Tham dự:** OM / BOD (tuỳ lịch).  
**Thời gian:** 30–45 phút.  
**Mục tiêu:** Phát hiện điểm lệch sớm, điều chỉnh trước khi thành vấn đề lớn.

- [ ] Tổng hợp doanh thu 7 ngày, so sánh mục tiêu ≥15 triệu/ngày.
- [ ] Xem lại số liệu POS: món bán chạy, món bán chậm, giờ cao điểm.
- [ ] Tổng hợp feedback khách (trực tiếp, review, group chat).
- [ ] Rà số ca / đi trễ / nghỉ đột xuất trong tuần.
- [ ] Kiểm tra tình trạng NVL hao hụt, hủy hàng.
- [ ] Xem lại ảnh báo cáo kết ca tuần qua: vệ sinh, tiền mặt, khóa cửa.
- [ ] Cập nhật lịch làm tuần tới, đảm bảo ≥2 NV giờ cao điểm.
- [ ] Ghi 3 hành động cải tiện tuần tới vào Daily Note / Weekly Review.

---

### AFS-CHK-M01 — Kiểm tra PCCC & an toàn tháng (Ngày 5)
**Người làm:** Site Manager + kỹ thuật / bảo trì.  
**Giám sát / Ký:** OM / BOD.  
**Thời gian:** 1 giờ.  
**Mục tiêu:** 100% thiết bị PCCC hoạt động; đủ số lượng theo quy định.

- [ ] Kiểm tra áp suất bình chữa cháy CO2 5kg tại mỗi xe buýt (2 bình/xe).
- [ ] Kiểm tra bình CO2 2kg tại mỗi trailer.
- [ ] Kiểm tra bình MFZ 8kg tại khu trung tâm rừng.
- [ ] Kiểm tra 4 biển chỉ dẫn lối thoát hiểm còn sáng, không bị che khuất.
- [ ] Kiểm tra ngày hạn sử dụng bình chữa cháy; lập kế hoạch thay nếu gần hết hạn.
- [ ] Kiểm tra số điện thoại khẩn cấp (PCCC 114, y tế, đội cắt tỉa) lưu ở điện thoại Site Manager.
- [ ] Kiểm tra biển cấm lửa tại cổng và mỗi trailer.
- [ ] Ghi nhận kết quả vào biểu mẫu kiểm tra thiết bị an toàn.

---

### AFS-CHK-M02 — Kiểm kê & đối soát tháng
**Người làm:** Site Manager + Thu ngân + Kế toán.  
**Giám sát / Ký:** CFO / Kế toán trưởng.  
**Thời gian:** Theo lịch T+7 cuối tháng.  
**Mục tiêu:** Đối chiếu doanh thu, tiền mặt, tồn kho; lệch ≤2%.

- [ ] Kiểm kê toàn bộ NVL, ly, vật tư tiêu hao trong 2 xe buýt + kho.
- [ ] Đối chiếu tồn đầu + nhập – xuất (POS) = tồn cuối.
- [ ] Đối chiếu tiền mặt nộp BKL với báo cáo POS.
- [ ] Kiểm tra hóa đơn VAT, biên lai chi phí ca có đầy đủ.
- [ ] Rà lại các biên bản hủy NVL, chênh lệch BTP.
- [ ] Lập báo cáo kiểm kê gửi kế toán trước deadline T+7.

---

### AFS-CHK-Q01 — Audit tuân thủ quý
**Người làm:** QA Team + OM / BOD.  
**Giám sát / Ký:** COO NQDL.  
**Thời gian:** 1 buổi.  
**Mục tiêu:** Điểm tuân thủ ≥90%; không có vi phạm nghiêm trọng.

- [ ] Kiểm tra 4–5 ca gần nhất có đầy đủ chữ ký Site Manager.
- [ ] Spot-check 3–5 món đồ uống / burrito theo công thức.
- [ ] Kiểm tra nhiệt độ bảo quản, vệ sinh cá nhân, chống nhiễm chéo.
- [ ] Kiểm tra nhật ký an toàn rừng, nhật ký bảo trì, sổ bàn giao ca.
- [ ] Phỏng vấn ngắn 2–3 NV về quy trình sơ tán, sử dụng bình chữa cháy.
- [ ] Ghi nhận gap, lập kế hoạch hành động cải thiện 30 ngày.

---

### AFS-CHK-E01 — Sơ tán khẩn cấp / sự kiện đặc biệt
**Người làm:** Tất cả NV đang ca.  
**Chỉ huy:** Site Manager.  
**Kích hoạt khi:** Cảnh báo giông bão cấp 9+, cháy rừng, cành cây gãy nguy hiểm, sự cố an ninh.

- [ ] Site Manager quyết định sơ tán, thông báo toàn bộ NV qua loa/radio.
- [ ] Phân công: 1 NV/2 trailer, 1 NV/2 xe buýt.
- [ ] Thông báo khách: di chuyển theo lối thoát chính ra đường Trần Quang Diệu.
- [ ] Không để khách chạy qua khu rừng.
- [ ] Kiểm tra từng trailer, từng góc rừng — đảm bảo không còn ai.
- [ ] Đóng cửa, cố định xe buýt và trailer.
- [ ] Gọi 114 nếu cháy; gọi PCCC / y tế / đội cắt tỉa theo tình huống.
- [ ] Báo cáo CEO NQDL; ghi nhật ký sự kiện đầy đủ.
- [ ] Chỉ mở lại khi cảnh báo được gỡ bỏ và đã kiểm tra lại an toàn.

## 4. Ghi chú các SOP / form còn thiếu (PLANNED)

| SOP / Form | Trạng thái | Ảnh hưởng đến checklist | Hành động tiếp theo |
|---|---|---|---|
| NQDL-AFS-OPS-SOP-002 Vệ sinh & ATTP | PLANNED | Dùng checklist tạm trong AFS-CHK-D03 | Bảo/Thy soạn theo pattern OPS-SOP-001 + NQDL-OPS-CHK-001 |
| NQDL-AFS-OPS-SOP-004 Mobile POS Operations | PLANNED | Dùng mục POS trong AFS-CHK-D03/D05 | Chốt flow CUKCUK 2 máy, tài khoản riêng thu ngân |
| NQDL-AFS-OPS-SOP-005 Cash Control | PLANNED | Dùng mục tiền mặt trong AFS-CHK-D05 | Rà số tiền lẻ đầu ca, mức để lại 1M, nộp BKL |
| NQDL-AFS-FIN-SOP-001 Accounting Handbook | PLANNED | Dùng AFS-CHK-M02 tạm | Kế toán cung cấp form đối soát T+7 cho AFS |
| OPS-CHK-003 Checklist vận hành hàng ngày (từ KIET-DOCS) | PLANNED | File này thay thế tạm | Khi ban hành, merge các mục hợp lý vào AFS-CHK-D01–D05 |

## 5. Cách đo lường hiệu quả

| Chỉ số | Mục tiêu | Tần suất đo | Nguồn |
|---|---|---|---|
| Tỷ lệ hoàn thành checklist mở/đóng ca | 100% | Hàng ngày | Daily Note / form giấy |
| Thời gian phục vụ đồ uống | ≤3 phút | Quan sát ca / POS | AFS-OPS-PACK KPI |
| Thời gian ra burrito/snack | ≤5 phút | Quan sát ca | AFS-OPS-PACK KPI |
| Doanh thu 2 quầy | ≥15 triệu VND/ngày | Hàng ngày | Báo cáo POS |
| Sự cố an toàn | 0 | Hàng tháng | Nhật ký sự cố |
| Điểm tuân thủ audit | ≥90% | Hàng quý | QA audit |
| Food cost | ~35% | Hàng tháng | Báo cáo kế toán |

## 6. Liên kết để tra cứu nhanh

- [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/03_Business_Units/Airdream_Forest_Station/README.md|Airdream Forest Station — README]]
- [[../../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/11_Working/BU_Drafts/Airdream_Forest_Station/FINAL-REVIEW-PR33-AD2-AFS-SOP-20072026.md|Final Review PR #33 — AD2/AFS]]
- [[NQH/06 - Templates/Template - Daily Note.md|Template Daily Note]]
- [[NQH/06 - Templates/Template - Weekly Review.md|Template Weekly Review]]
