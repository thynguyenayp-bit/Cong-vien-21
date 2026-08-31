---
tags: [sop, airdream, co-location, order-flow, token]
sop-code: CL-3
status: draft
updated: "2026-06-29"
ap-dung-cho: Tất cả tại quầy (Barista, Pizza Staff, SM)
giam-sat: Site Manager
---

# SOP CL-3 — Token & Order Flow
**Airdream Forest Station | Tầng 2 — Co-location Layer**

> Quy trình order và quản lý thẻ rung cho địa điểm co-location 2 xe. Mục tiêu: khách nhận đồ đúng · thẻ rung không thất lạc · KPI SLA đạt chuẩn.

---

## 1. Tổng quan hệ thống

**Thẻ rung** (pager/buzzer) là thiết bị rung-đèn báo hiệu khi đồ sẵn sàng. Mỗi khách nhận **1 thẻ** dùng chung cho cả 2 xe — khách không cần quay lại quầy nhiều lần.

```
Khách vào cổng
      │
      ▼
Xe Cafe (XC) — điểm order đầu tiên  ←  Bảng "Order Here →" ở cổng
      │
      ├── Chỉ order Cafe      → nhận 1 thẻ rung từ XC
      ├── Chỉ order Pizza     → chuyển sang XP, nhận thẻ rung từ XP
      └── Order cả 2 xe       → order XC trước → XP sau → nhận 1 thẻ rung (XC giữ, XP ghi số)
      │
      ▼
Khách tự chọn chỗ ngồi (Zone B/C/D/E)
      │
      ▼
Thẻ rung rung + đèn nhấp nháy
      │
      ▼
Khách lên quầy lấy đồ · trả thẻ rung
```

---

## 2. Quy trình order tại Xe Cafe (XC)

### Bước 1 — Tiếp nhận order

1. Chào khách, hỏi nhu cầu
2. Nhập order vào **CUKCUK** (chọn bàn hoặc take-away)
3. Báo giá, nhận thanh toán (tiền mặt hoặc chuyển khoản)
4. In phiếu order (nếu hệ thống cấu hình) hoặc nhớ số thẻ

### Bước 2 — Phát thẻ rung

- Chọn **thẻ rung theo số thứ tự** từ bộ thẻ tại quầy XC
- Ghi số thẻ vào order trên CUKCUK (ghi ở trường ghi chú bàn)
- Đưa thẻ cho khách: *"Anh/chị ngồi đâu cũng được, thẻ rung sẽ báo khi đồ sẵn sàng"*

### Bước 3 — Làm đồ & giao đồ

- Pha chế theo thứ tự order nhận
- Khi đồ sẵn sàng: bấm số thẻ tương ứng trên bộ phát → thẻ rung kêu
- Khách lên lấy: xác nhận số thẻ, đưa đồ, **thu thẻ rung về ngay**
- Cập nhật trạng thái order trên CUKCUK (hoàn thành)

---

## 3. Quy trình order tại Xe Pizza (XP)

### Khách chỉ order Pizza (không order Cafe)

1. Tiếp nhận order, nhập vào CUKCUK
2. Nhận thanh toán
3. **Phát thẻ rung từ bộ thẻ của XP** (hoặc lấy từ thẻ gom về nếu còn)
4. Ghi số thẻ vào order
5. Giao đồ → thu thẻ rung

### Khách order cả 2 xe

Trường hợp này khách đã có thẻ rung từ XC:

1. Khách báo đã có thẻ rung số **[X]** từ XC
2. Pizza Staff nhập order vào CUKCUK, ghi chú: *"Thẻ [X] — đã order Cafe"*
3. **Không phát thẻ mới** — dùng cùng 1 thẻ
4. Khi pizza xong: bấm số thẻ [X] → thẻ đang ở tay khách sẽ rung
5. Giao pizza → thu thẻ sau khi giao cả 2 món (phối hợp với XC nếu cần)

> **Điều phối 2 xe:** Khi khách order combo Cafe + Pizza, XC và XP cần ước tính thời gian để đồ ra gần nhau. Nếu lệch nhau >5 phút, báo khách trước: *"Cafe sẽ ra trước khoảng [X] phút anh/chị nhé".*

---

## 4. Quản lý thẻ rung

### Tổng số thẻ & phân bổ

| Vị trí | Số lượng | Ghi chú |
|---|---|---|
| Bộ phát tại XC | [điền số] | Đặt trên quầy, cắm sạc thường xuyên |
| Bộ phát tại XP | [điền số] | Đặt trên quầy XP |
| Thẻ tại XC | [điền số] | Số thẻ cần xác nhận với SM |
| Thẻ tại XP | [điền số] | Gom về XC mỗi sáng |

> ⚠️ *Điền số lượng thực tế sau khi kiểm kê — SM cập nhật.*

### Quy tắc quản lý thẻ

1. **Mỗi sáng** (7:00): Barista gom toàn bộ thẻ từ XP về quầy XC, đếm tổng số
2. **Trong ca**: thẻ luôn được thu về ngay khi giao đồ — không để khách cầm thẻ rời đi
3. **Khách quên trả thẻ**: PT Server quan sát, nhắc nhở trước khi khách ra cổng
4. **Thẻ mất/hỏng**: báo SM ngay, ghi vào sổ giao ca → SM liên hệ thay thế
5. **Cuối ca**: đếm tổng thẻ, ghi vào form giao ca (xem [[O2 — Bàn giao ca]])

### Đếm thẻ cuối ngày

```
Thẻ đang lưu hành = Tổng thẻ có − Thẻ tại quầy XC − Thẻ tại quầy XP
Thẻ đang lưu hành phải = 0 khi đóng cửa
```

Nếu thẻ đang lưu hành > 0 khi cuối ca → rà soát từng khu ngồi trước khi đóng cửa.

---

## 5. SLA Order

| Loại order | SLA tối đa | Tính từ |
|---|---|---|
| Cafe đơn lẻ | ≤ 5 phút | Lúc khách nhận thẻ rung |
| Set nước 2–3 ly | ≤ 8 phút | Lúc khách nhận thẻ rung |
| Pizza gập | ≤ 8 phút | Lúc khách nhận thẻ rung |
| Mini pizza | ≤ 6 phút | Lúc khách nhận thẻ rung |
| Set pizza (4/6) | ≤ 10 phút | Lúc khách nhận thẻ rung |
| Khoai tây chiên | ≤ 5 phút | Lúc khách nhận thẻ rung |

**Khi sắp trễ SLA:**
- Barista/Pizza Staff chủ động thông báo qua bộ đàm cho SM
- SM hoặc PT Server đến báo khách trực tiếp: *"Xin lỗi anh/chị, đồ sẽ ra trong thêm [X] phút nữa"*
- Không để thẻ rung quá 10 phút mà không có thông báo

---

## 6. Các tình huống đặc biệt

### Khách đặt set lớn (>4 ly hoặc >2 pizza)

- Barista/Pizza Staff báo SM ngay khi nhận order
- SM thông báo cho PT Server chuẩn bị hỗ trợ giao
- Dùng khay để giao, PT Server mang đến bàn

### Giờ cao điểm (hàng queue dài)

- SM bật bộ đàm thông báo: *"High volume — XC ưu tiên, XP ưu tiên"*
- Khách chờ >10 phút tại quầy: chủ động mời khách ngồi, sẽ mang thẻ rung ra
- Xem [[CL-2 — Phối hợp giờ cao điểm]]

### Khách muốn đổi / hủy order

- Chưa làm: đổi trên CUKCUK, không tính phí
- Đang làm: tùy trường hợp — SM quyết định
- Đã hoàn thành: không đổi; nếu sự cố chất lượng → làm lại hoặc hoàn tiền (SM quyết định)

### Mất điện / POS lỗi

- Ghi order tay vào giấy, giữ thứ tự
- Nhập lại vào CUKCUK khi hệ thống ổn định
- Xem [[H3 — Mất điện]]

---

## 7. RACI

| Bước | SM | Barista | Pizza Staff | PT Server |
|---|:---:|:---:|:---:|:---:|
| Tiếp nhận order + nhập CUKCUK | C | **R** | **R** | — |
| Phát thẻ rung | I | **R** | **R** | — |
| Điều phối 2 xe khi combo | **R** | C | C | — |
| Giao đồ + thu thẻ | I | **R** | **R** | C |
| Quản lý thẻ hàng ngày | **A** | **R** | C | C |
| Xử lý SLA trễ | **R/A** | R | R | R |
| Đếm thẻ giao ca | **R/A** | C | C | — |

---

*Áp dụng cho: Barista · Pizza Staff · Site Manager — Airdream Forest Station*
*Giám sát / Accountable: Site Manager*
*Thuộc: [[Framework — SOP Airdream Forest Station]] — Tầng 2, nhóm CL*
*Xem thêm: [[CL-2 — Phối hợp giờ cao điểm]] · [[CL-6 — Đối soát doanh thu]] · [[O1 — Mở cửa]]*
