---
tags: [review, weekly]
week: "{{date:YYYY-[W]ww}}"
---

# Weekly Review — {{date:YYYY-[W]ww}}

> 🗓 Tuần {{date:[W]ww}} năm {{date:YYYY}} — [[Dashboard]] · [[Home]]

## 1. Tổng kết tuần qua
### Hoàn thành (nhớ ghi cảm giác / kết quả)
- 

### Chưa xong / cần dời
- 

## 2. Việc đã xong (7 ngày qua)
```dataview
TASK
WHERE completed AND completion >= date(today) - dur(7 days)
```

## 3. Việc còn tồn / quá hạn
```dataview
TASK
WHERE !completed AND due AND due < date(today)
SORT due ASC
```

## 4. Dự án đang chạy — cập nhật nhanh
```dataview
TABLE status AS "Trạng thái", deadline AS "Deadline", owner AS "Owner"
FROM "01 - Projects"
WHERE status != "done"
SORT deadline ASC
```

## 5. Dọn Inbox còn sót
- [ ] Review `00 - Inbox` — phân loại về PARA.
- [ ] Dọn các ghi chú rời trong `05 - Daily Notes` cần chuyển thành note.

## 6. Kế hoạch tuần tới (3 ưu tiên chính)
1. 
2. 
3. 

## 7. Cần follow / nhờ sếp / phối hợp
- 👤 [[ ]] — 

## 8. Ghi nhận / học bài (cho /distill)
- 
