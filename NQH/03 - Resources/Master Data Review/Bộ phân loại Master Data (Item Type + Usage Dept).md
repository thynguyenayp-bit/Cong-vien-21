---
tags: [resource, masterdata, ketoan, standard]
updated: "2026-06-25"
---

# 🏷️ Bộ phân loại chuẩn Master Data NVL — Item Type & Usage Department

> Danh mục cố định để **mọi mã NVL tạo mới đều phân loại được**, phủ 4 mô hình: 🍽️ nhà hàng · 🏨 khách sạn · ☕ cafe · 🦌 khu du lịch nuôi thú. Liên quan: [[Review Master Data NVL — 2026-06-25]] · [[Quy trình phê duyệt Bflow (DAG)]].

## 🧱 Kiến trúc 2 lớp (đã có sẵn — đừng lẫn)
| Tab | Bản chất | Sinh ra | Ví dụ |
|-----|----------|---------|-------|
| **NVL (`RAW…`)** ← *note này* | Hàng **mua vào** (đầu vào) | **Chi phí / giá vốn** | thịt, hộp, dép, cám thú |
| **Mã món (`PRD`)** | Sản phẩm **bán ra** (đầu ra) | **Doanh thu** | món ăn, nước (nước Trại Mèo đã gồm tham quan) |

> Hàng mua-về-bán-lại (bia chai, quà lưu niệm) nằm ở **cả 2 tab**: NVL gắn `RET` (tồn kho, TK 156) ↔ PRD là mã bán. Liên kết 1–1.
>
> **Khi tạo 1 mã NVL, gán tối thiểu:** ① Item Type (`Cap_1`) · ② Quản lý kho (Có/Không) · ③ Usage Department · ④ BU áp dụng (`Ap_Dung_*`).

---

## 📦 BẢNG A — ITEM TYPE (`Cap_1`): hàng đó LÀ GÌ
🆕 = mã mới bổ sung. Quản lý kho: **Có** = qua nhập/xuất kho · **Không** = mua thẳng chi phí.

> **Giải nghĩa mã** (3 chữ đầu tiếng Anh): RAW=**Raw** · INT=**Int**ernal · RET=**Ret**ail · PKG=**P**ac**k**a**g**e · CON=**Con**sumable · CHM=**Ch**e**m**ical · FUE=**Fue**l · AMN=**Am**e**n**ity · LNN=**L**i**n**e**n** · ANI=**Ani**mal · LND=**L**a**nd**scape · EQP=**Eq**ui**p**ment · ICT=Info-Comm-Tech · DEC=**Dec**oration · AST=**As**se**t** · OFF=**Off**ice · UNI=**Uni**form · MNT=**M**ai**nt**enance · SVC=**S**er**v**i**c**e.

| Mã                                 | Tên                                  | Ví dụ                                             | Phủ      |  QL kho   | TK_Kho/CP*  |
| ---------------------------------- | ------------------------------------ | ------------------------------------------------- | -------- | :-------: | ----------- |
| **RAW**                            | Nguyên liệu thô                      | thịt, rau, gia vị, cơm                            | 🍽️☕🏨   |    Có     | 152         |
| **INT**                            | Bán thành phẩm (BTP)                 | sốt, cold brew, trà sữa BTP                       | 🍽️☕     |    Có     | 154/155     |
| **RET**                            | Hàng bán lại (hàng hoá)              | bia, rượu chai, quà lưu niệm                      | 🍽️☕🏨🦌 |    Có     | 156         |
| **PKG** 🆕                         | Bao bì đóng gói                      | hộp Pizza Gập, ly, túi, ống hút                   | 🍽️☕     |    Có     | 153         |
| **CON**                            | Vật tư tiêu hao vận hành             | củi, băng keo, bảng đặt bàn                       | tất cả   |    Có     | 153         |
| **CHM** 🆕                         | Hoá chất vệ sinh                     | nước rửa chén, cloramin                           | tất cả   |    Có     | 153         |
| **FUE** 🆕                         | Nhiên liệu                           | gas, củi đốt, dầu                                 | 🍽️🦌    |    Có     | 152         |
| **AMN** 🆕 *(thay "Vật tư phòng")* | Tiện ích phòng **dùng 1 lần**        | bàn chải, dao cạo, dầu gội, dép                   | 🏨       |    Có     | 153         |
| **LNN** 🆕                         | Đồ vải/linen **tái sử dụng**         | khăn tắm, drap, vỏ gối, rèm                       | 🏨       |    Có     | 153         |
| **ANI** 🆕                         | Thức ăn & vật tư chăm sóc thú        | cám, cỏ, thuốc thú y, lót chuồng                  | 🦌       |    Có     | 152/153     |
| **LND** 🆕                         | Vật tư cảnh quan & cây xanh          | cây, phân bón, đất, đá                            | 🦌🏨     |    Có     | 152/153     |
| **EQP** 🆕 *(thay "NRM")*          | Công cụ–dụng cụ (CCDC)               | bàn, bản gang, dụng cụ bếp                        | tất cả   |    Có     | 153         |
| **ICT** 🆕                         | Thiết bị CNTT/mạng/điện tử           | router, camera, POS, máy tính, máy in             | tất cả   |    Có     | 153         |
| **DEC** 🆕                         | Trang trí nội thất / décor           | tranh, lọ hoa, đèn trang trí                      | tất cả   |    Có     | 153         |
| **AST** 🆕                         | Tài sản cố định (TSCĐ ≥30tr, >1 năm) | lò, tủ đông, hệ thống lớn                         | tất cả   |    Có     | 211–214     |
| **OFF** 🆕                         | Văn phòng phẩm                       | giấy, bút, mực in                                 | tất cả   |    Có     | 153         |
| **UNI** 🆕                         | Đồng phục & bảo hộ                   | áo bếp, găng tay, tạp dề                          | tất cả   |    Có     | 153         |
| **MNT** 🆕                         | Vật tư bảo trì & phụ tùng            | bóng đèn, ốc vít, phụ tùng                        | tất cả   |    Có     | 153         |
| **SVC** 🆕                         | **Dịch vụ & chi phí mua ngoài**      | cước SIM, internet, thuê, phần mềm, nhạc acoustic | tất cả   | **Không** | 627/641/642 |

*\*TK đề xuất — cần Kế toán trưởng duyệt khớp [[Quy trình phê duyệt Bflow (DAG)]].*

### 🔑 Nguyên tắc Kho vs Dịch vụ (giải quyết vụ SIM)
- **Vẫn tạo mã** cho dịch vụ (để mua được trên Bflow) — nhưng gắn `SVC` + **Quản lý kho = Không** → mua đi **thẳng chi phí**, KHÔNG tạo phiếu nhập/xuất kho (tránh tồn kho ảo).
- VD: **SIM/internet/thuê nhạc** = `SVC`, kho = Không. **Router** = `ICT`, kho = Có.

### 🔄 Map mã cũ → chuẩn mới
| Hiện có | Số mã | Chuyển thành |
|---------|-------|--------------|
| RAW 723 | giữ **RAW** |
| NRM 310 (đang là bàn ghế/thiết bị) | nhỏ → **EQP** · CNTT → **ICT** · ≥30tr → **AST** |
| CON 182 | bao bì → **PKG** · hoá chất → **CHM** · còn lại **CON** |
| RET 28 | giữ **RET** |
| INT 12 | giữ **INT** |
| "Vật tư phòng" 3 | **AMN** (1 lần) / **LNN** (linen) |
| (trống) 93 | phân loại theo bảng A — xem `Thiếu Cap_1 (93 mã).tsv` |

---

## 🧑‍🍳 BẢNG B — USAGE DEPARTMENT (`Bo_Phan_Su_Dung`): bộ phận DÙNG
| Mã | Bộ phận | Áp dụng |
|----|---------|---------|
| **KIT** | Bếp (Kitchen) | 🍽️☕🏨 |
| **BAR** | Quầy bar / pha chế | ☕🍽️🏨 |
| **CK** 🆕 | Bếp tổng (Central Kitchen) | sản xuất BTP |
| **SVC** 🆕 | Phục vụ / sảnh (FOH) | 🍽️☕ |
| **HK** 🆕 | Buồng phòng (Housekeeping) | 🏨 |
| **FO** 🆕 | Lễ tân (Front Office) | 🏨 |
| **ZOO** 🆕 | Khu nuôi thú / chăm sóc động vật | 🦌 |
| **LND** 🆕 | Cảnh quan & cây xanh | 🦌🏨 |
| **MKT** 🆕 | Marketing | tất cả |
| **IT** 🆕 | CNTT | tất cả |
| **OFF** 🆕 | Văn phòng / hành chính | tất cả |
| **MNT** 🆕 | Kỹ thuật / bảo trì | tất cả |
| **WH** 🆕 | Kho | tất cả |
| **SEC** 🆕 | Bảo vệ | tất cả |

**Hiện có:** KIT (450) · BAR (89) · combo KIT/BAR (14) → giữ; cho phép **combo** `KIT/BAR`.

---

## 📏 Quy ước chung
- **Trống = chưa phân loại** (cần điền) · **`-` = không áp dụng** (chủ động) → không dùng lẫn lộn.
- Mã phân loại **HOA, 3 ký tự** (trừ combo). Mỗi mã NVL bắt buộc có `Cap_1` + `Quản lý kho` + `Bo_Phan_Su_Dung` trước khi nhập kho Bflow.

## 🧭 Các trục khác đang có (chuẩn hoá luôn)
- `Loai_Chi_Tiet`: GIA=gia vị · RAU=rau · THI=thịt · HAI=hải sản · FRU=trái cây · DRI=đồ uống · LIQ=rượu · BAK=bánh · DAI=sữa.
- `Tinh_Trang_NVL`: FRE=tươi · DRY=khô · LIQ=lỏng · POW=bột · CAN=đóng hộp · FRO=đông.
- `Muc_Do_Che_Bien`: THO=thô · INT=sơ chế · RTU=dùng ngay · PRE=đã chế biến.

## ✅ Bước tiếp theo (em làm được ngay)
1. Chị duyệt/chỉnh 2 bảng → em **sinh file re-map 1.351 mã** sang Item Type chuẩn + điền `Bo_Phan_Su_Dung`.
2. Phân loại **93 mã thiếu Cap_1**.
3. Sinh file fill `TK_Kho` + cờ `Quản lý kho` theo Item Type → kế toán nhập kho Bflow.
