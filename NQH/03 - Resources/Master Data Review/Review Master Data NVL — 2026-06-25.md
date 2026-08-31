---
tags: [resource, masterdata, ketoan, review]
updated: "2026-06-25"
nguồn: "Google Sheet master data NVL (gid=0)"
---

# 🔎 Review Master Data NVL — 25/06/2026

> Soát file master data NVL (Google Sheet) để phục vụ **nhập kho Bflow** + hoàn thiện phân loại/nhóm mã. Liên quan: [[Bảng điều hành công việc]] · [[Quy trình phê duyệt Bflow (DAG)]].

## Tổng quan
- **1.351 mã sản phẩm** có đủ Mã + Tên (RAW-0001 → RAW-1522).
- ~1.078 dòng template trống (mã `RAW-0000`, chưa dùng) — không phải việc cần lên mã.
- ✅ Không có mặt hàng "có tên nhưng thiếu mã" trong sheet này.

## 🔴 Phát hiện CHÍNH — 7 cột hệ thống Bflow đang **100% trống**
Dữ liệu đã điền ở **cột người-dùng (bên trái)** nhưng **chưa map sang cột hệ thống** mà Bflow cần để nhập kho:

| Cột hệ thống (Bflow) | Tình trạng      | Lấy/suy từ đâu                                  |
| -------------------- | --------------- | ----------------------------------------------- |
| `DVT_Mua`            | trống 1351/1351 | **copy** từ `ĐVT đơn vị mua hàng` (có sẵn 1343) |
| `DVT_Xuat_Kho`       | trống           | **copy** từ `DVT Nhập kho` (có sẵn 1339)        |
| `He_So_Quy_Doi`      | trống           | =1 nếu mua/xuất cùng ĐVT; khác thì tính         |
| `TK_Kho`             | trống           | **suy theo Cap_1** (đề xuất bên dưới)           |
| `TK_Chi_Phi`         | trống           | theo bộ phận sử dụng / nhóm                     |
| `Loai_Thue_VAT`      | trống           | mặc định theo nhóm hàng (8%/10%/KCT)            |
| `NCC_Mac_Dinh_Ten`   | trống           | từ NCC mua gần nhất                             |
| `Trang_Thai`         | trống           | mặc định "Đang dùng"                            |

> 💡 **Điểm mấu chốt:** đây KHÔNG phải nhập tay 1.351×7 ô. Phần lớn **fill hàng loạt bằng quy tắc map** (copy cột + suy theo Cap_1). Chỉ số ít cần điền tay (hệ số quy đổi khác ĐVT, NCC).

### Đề xuất map `TK_Kho` theo Cap_1 *(cần Kế toán trưởng duyệt)*
| Cap_1   | Số mã | Ý nghĩa (suy đoán)            | TK_Kho đề xuất        |
| ------- | ----- | ----------------------------- | --------------------- |
| RAW     | 723   | Nguyên liệu thô               | 152                   |
| NRM     | 310   | NVL phụ/non-raw               | 152                   |
| CON     | 182   | Công cụ/consumable (ống hút…) | 153                   |
| RET     | 28    | Hàng bán lại (rượu…)          | 156                   |
| INT     | 12    | Nội bộ/BTP                    | 154/155 ?             |
| (trống) | 93    | **chưa phân loại**            | — cần lên Cap_1 trước |

## ⚠️ Phân loại / nhóm mã chưa hoàn thiện
- **Thiếu `Cap_1`: 93 mã** → danh sách: [[Thiếu Cap_1 (93 mã)]] (.tsv, mở/dán vào Sheet để điền).
- **Thiếu `Cap_2` / `Loai_Chi_Tiet`: 566 mã (41%)** → danh sách: [[Thiếu Cap_2-LoaiChiTiet (566 mã)]].
- **Không nhất quán**: `Cap_2` chỗ để trống, chỗ ghi `-` (gạch). → thống nhất 1 quy ước (trống = chưa phân loại; `-` = không áp dụng).
- **`Vật tư phòng` (3 mã)** đang ghi **chữ tự do** thay vì mã Cap_1 → đặt 1 mã chuẩn (vd `SUP`).

## 🔁 6 cặp tên TRÙNG — cần quyết "gộp hay giữ"
| Tên | Mã A (đầy đủ) | Mã B (thiếu data) | Nhận định |
|-----|---------------|-------------------|-----------|
| Mực ống | RAW-0430 (RM01, 240k) | RAW-1286 (Cap_2 `-`, 270k) | giá khác → kiểm tra quy cách, có thể là 2 loại |
| Rượu mai quế lộ | RAW-0455 (RAW/RM05, 120k) | RAW-1008 (RET, trống giá) | B mới/thiếu → gộp? |
| Rượu mùi Cointreau | RAW-0456 (RAW/RM05, 642k) | RAW-0920 (RET, trống) | B mới/thiếu → gộp? |
| Ống hút rượu cần | RAW-0593 (CON, 6k) | RAW-0827 (CON, trống) | trùng → gộp |
| Lạp xưởng | RAW-1097 (trống giá) | RAW-1289 (130k) | gộp, giữ mã có giá |
| Bún gạo | RAW-1225 (trống giá) | RAW-1288 (42k) | gộp, giữ mã có giá |

## 💰 Khác
- **Thiếu `Gia_Binh_Quan`: 737 mã (54%)** — ảnh hưởng tính giá vốn khi xuất kho.
- 171 số mã bị khuyết trong dãy RAW (do đã xoá/gộp) — bình thường, không cần xử lý.

## ✅ Việc đề xuất (ưu tiên để nhập kho được)
1. **Fill hàng loạt 7 cột hệ thống** bằng quy tắc map (copy + suy Cap_1) → em có thể sinh sẵn file để chị dán vào Sheet.
2. **Lên Cap_1 cho 93 mã** (danh sách đã xuất) — chặn việc map TK_Kho.
3. **Chốt 6 tên trùng** (gộp/giữ) với Bếp + KTT.
4. **Thống nhất quy ước `-` vs trống** + đổi "Vật tư phòng" thành mã.
5. **Bổ sung giá BQ** 737 mã (lấy từ giá mua gần nhất).
6. Duyệt bảng map `TK_Kho`/`TK_Chi_Phi`/`VAT` với **Kế toán trưởng** → khớp [[Quy trình phê duyệt Bflow (DAG)]].

## 📎 File bàn giao (thư mục này)
| File                                                  | Nội dung                                                                      | Dùng để                                   |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------- |
| `REMAP Item Type + TK_Kho (1351 mã).tsv`              | 1.351 mã + Item Type chuẩn + cờ Quản lý kho + TK_Kho gợi ý + cột `Cần_review` | Dán vào Google Sheet cho kế toán nhập kho |
| `Trùng - gần trùng (cần soát).tsv`                    | 54 nhóm / 139 mã trùng hoặc gần trùng                                         | Soát gộp/giữ                              |
| `Thiếu Cap_1 (93 mã).tsv`                             | Mã chưa có Item Type                                                          | Phân loại tay                             |
| `Thiếu Cap_2-LoaiChiTiet (566 mã).tsv`                | Mã thiếu nhóm con                                                             | Phân loại tay                             |
| [[Bộ phân loại Master Data (Item Type + Usage Dept)]] | Chuẩn 19 Item Type + 14 Usage Dept                                            | Tra khi tạo mã mới                        |

> ⚠️ File REMAP là **bản tự phân loại bằng máy (draft)** — cột `Cần_review` (101 dòng) và `?` (59 mã chưa phân loại được) **phải kiểm tay** trước khi import. TK_Kho là **gợi ý**, cần Kế toán trưởng duyệt.
