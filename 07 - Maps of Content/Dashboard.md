---
tags: [moc, dashboard]
---

# 📊 Dashboard — Nguyễn Hoàng Ngọc Thy

> Trung tâm điều khiển công việc. Tự cập nhật từ các `#task` trong vault (cần plugin Dataview + Tasks).
> 🔗 [[Home]] · [[My-Role]] · [[Working-Preferences]]

## 🔥 Quá hạn — cần xử lý ngay
```dataview
TASK
WHERE !completed AND due AND due < date(today)
SORT due ASC
```

## 📅 Đến hạn hôm nay
```dataview
TASK
WHERE !completed AND due AND due = date(today)
SORT priority ASC
```

## 📋 Đến hạn trong 3 ngày tới
```dataview
TASK
WHERE !completed AND due AND due > date(today) AND due <= date(today) + dur(3 days)
SORT due ASC
```

## 🚀 Dự án đang chạy
```dataview
TABLE status AS "Trạng thái", deadline AS "Deadline", priority AS "Ưu tiên"
FROM "01 - Projects"
WHERE status != "done"
SORT deadline ASC
```

## 🏢 Trách nhiệm lâu dài (Areas) cần theo dõi
```dataview
LIST
FROM "02 - Areas"
```

## ✅ Vừa xong (7 ngày)
```dataview
TASK
WHERE completed AND completion >= date(today) - dur(7 days)
LIMIT 15
```

## 📥 Inbox — cần dọn
- Xem thư mục `00 - Inbox` và dọn về PARA định kỳ.
- Lệnh: `/inbox` hoặc *"giúp tôi phân loại Inbox"*.
