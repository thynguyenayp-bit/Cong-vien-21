---
tags: [resource, finance, bflow, sop]
updated: "2026-06-24"
---

# 💳 Quy trình phê duyệt Bflow (DAG v2.2)

> Tóm tắt để tra nhanh. Nguồn: **NQH-HO-FIN-WI-001 — Payment Approval Quick Reference** tại `../NQH-GROUP-SOP-SYSTEM/01_NQH-SOPs/01_Nhat_Quang_Holding/Finance/NQH-HO-FIN-WI-001_Payment_Approval_Quick_Reference.md`. Ma trận gốc: NQH-HO-CGF-002 (DAG v2.2).

## Cơ chế: phê duyệt 2 điều kiện
1. **Loại chi phí** (mã Bflow) → xác định **luồng** (1 trong 6): OPEX · CAPEX · Personnel · Vendor Mgmt · AP (trả NCC) · Advance/Reimb (tạm ứng/hoàn ứng).
2. **Số tiền** → xác định **cấp phê duyệt** theo ma trận DAG.

Nhân viên chỉ chọn 1 trong **11 nhóm đơn giản** (📦 NVL · 🔧 CCDC · 🏭 TSCĐ · 💰 lương · 🎁 thưởng · 📢 MKT · 🏢 VP · 🎓 đào tạo · 🤝 NCC · 💵 tạm ứng · 🎁 giao tế) → DAG tự ra cấp duyệt; kế toán map mã chi tiết + TK VAS (Layer 2).

## Ma trận phê duyệt (cấp duyệt theo số tiền)
| Luồng | <5M | 5–10M | 10–50M | 50–200M | ≥200M |
|-------|-----|-------|--------|---------|-------|
| OPEX | TP | TP | TP+GĐ | GĐ+CFO | CFO+CEO |
| CAPEX | TP | TP+GĐ | GĐ+CFO | CFO+CEO | CEO+HĐQT |
| Personnel | TP | TP+GĐ | GĐ+CFO | CFO+CEO | CEO+HĐQT |
| Vendor Mgmt | TP | TP+GĐ | GĐ+CFO | CFO+CEO | CFO+CEO+HĐQT |
| AP (trả NCC) | TP | TP | TP+GĐ | GĐ+CFO | CFO+CEO |
| Tạm ứng/Hoàn ứng | TP | TP | TP+GĐ | GĐ+CFO | CFO+CEO |

TP=Trưởng phòng · GĐ=Giám đốc · CFO · CEO · HĐQT.

## Quy tắc quan trọng
- **BCC (mã vụ việc) bắt buộc** khi ≥5M (mọi luồng) hoặc **CAPEX bất kể số tiền**. Không BCC → kế toán từ chối xử lý (nguyên tắc "DNA 0").
- **SLA**: TP (1 cấp) = 4h · TP+GĐ = 24h · GĐ+CFO = 3 ngày · CFO+CEO = 7 ngày (giờ làm T2–T6, không tính lễ).
- **3 PHẢI**: có BCC · đủ phê duyệt theo DAG · chứng từ hợp lệ (hoá đơn VAT đúng tên/MST).
- **Quyết toán tạm ứng**: công tác T+7 · mua hàng T+3 · **dự án T+14** ngày làm việc (quá hạn bị phạt).

## 🔗 Áp dụng cho việc của tôi
- **Hoàn ứng tạm ứng 10tr (Pizza Gập)** → luồng **Tạm ứng/Hoàn ứng**. Hoàn ứng = trả lại tiền thừa (mã ADV-RET, TK 141). Nhớ quyết toán đúng hạn (dự án T+14). → [[PRJ - Pizza Gập]].
- **Báo cáo chi phí đầu tư ban đầu PZG** → luồng **CAPEX** (BCC bắt buộc; ≥10M cần báo giá nhiều NCC / Business Case theo mức).
- **Review luồng thanh toán theo DAG với Kế toán trưởng** → đối chiếu đúng ma trận này + cấu hình `expense_groups` (11 nhóm). → [[Bảng điều hành công việc]].
