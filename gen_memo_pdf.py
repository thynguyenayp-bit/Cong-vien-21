#!/usr/bin/env python3
"""Generate the weekly payment plan memo PDF – v2 fix blank pages."""

from fpdf import FPDF

FONT_DIR = "/System/Library/Fonts/Supplemental/"


class MemoPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arial", "", FONT_DIR + "Arial.ttf")
        self.add_font("Arial", "B", FONT_DIR + "Arial Bold.ttf")
        self.add_font("Arial", "I", FONT_DIR + "Arial Italic.ttf")
        self.add_font("Arial", "BI", FONT_DIR + "Arial Bold Italic.ttf")
        self.set_auto_page_break(auto=True, margin=22)

    C_PRIMARY = (26, 82, 118)
    C_ACCENT = (243, 156, 18)
    C_RED = (192, 57, 43)
    C_GREEN = (39, 174, 96)
    C_PURPLE = (142, 68, 173)
    C_LIGHT_BG = (234, 242, 248)
    C_YELLOW_BG = (254, 249, 231)
    C_GRAY_BG = (248, 249, 250)
    C_BORDER = (212, 230, 241)
    C_TEXT = (26, 26, 26)
    C_MUTED = (127, 140, 141)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 7)
        self.set_text_color(*self.C_MUTED)
        self.cell(0, 10, f"Trang {self.page_no()}/{{nb}}", align="C")

    def section_title(self, num, title):
        self.ln(5)
        x, y = self.l_margin, self.get_y()
        # blue circle
        self.set_fill_color(*self.C_PRIMARY)
        self.ellipse(x, y + 1, 7, 7, style="F")
        self.set_font("Arial", "B", 9)
        self.set_text_color(255, 255, 255)
        self.set_xy(x + 0.8, y + 1.5)
        self.cell(5.5, 5, str(num), align="C")
        self.set_xy(x + 9, y)
        self.set_font("Arial", "B", 12)
        self.set_text_color(*self.C_PRIMARY)
        self.cell(0, 9, title)
        self.ln(9)
        self.set_draw_color(*self.C_BORDER)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def sub_title(self, text):
        self.set_font("Arial", "B", 10)
        self.set_text_color(44, 62, 80)
        self.cell(0, 7, text)
        self.ln(7)

    def body_text(self, text, bold=False):
        self.set_font("Arial", "B" if bold else "", 9.5)
        self.set_text_color(*self.C_TEXT)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def info_box(self, text, bg=None, border_color=None, icon=""):
        if bg is None:
            bg = self.C_LIGHT_BG
        if border_color is None:
            border_color = self.C_PRIMARY
        x = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        # measure text height
        self.set_font("Arial", "", 9.5)
        full = (icon + "  " if icon else "") + text
        lines = self.multi_cell(w - 10, 5.5, full, dry_run=True, output="LINES")
        h = len(lines) * 5.5 + 8
        # check page break
        if self.get_y() + h > self.h - 22:
            self.add_page()
            x = self.l_margin
        y = self.get_y()
        # draw bg
        self.set_fill_color(*bg)
        self.rect(x, y, w, h, style="F")
        # left accent
        self.set_fill_color(*border_color)
        self.rect(x, y, 1.5, h, style="F")
        # text
        self.set_xy(x + 5, y + 4)
        self.set_text_color(*self.C_TEXT)
        self.set_font("Arial", "", 9.5)
        self.multi_cell(w - 10, 5.5, full)
        self.set_y(y + h + 2)

    def simple_table(self, headers, rows, col_widths=None):
        w = self.w - self.l_margin - self.r_margin
        if col_widths is None:
            col_widths = [w / len(headers)] * len(headers)
        # header
        self.set_font("Arial", "B", 8.5)
        self.set_fill_color(*self.C_PRIMARY)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=0, fill=True, align="C")
        self.ln()
        # rows
        self.set_font("Arial", "", 8.5)
        self.set_text_color(*self.C_TEXT)
        for r_idx, row in enumerate(rows):
            bg = self.C_GRAY_BG if r_idx % 2 == 1 else (255, 255, 255)
            self.set_fill_color(*bg)
            # calc row height
            self.set_font("Arial", "", 8.5)
            max_h = 7
            for i, cell in enumerate(row):
                ls = self.multi_cell(col_widths[i] - 2, 5, cell, dry_run=True, output="LINES")
                rh = len(ls) * 5 + 2
                if rh > max_h:
                    max_h = rh
            # check page break
            if self.get_y() + max_h > self.h - 22:
                self.add_page()
                # re-draw header
                self.set_font("Arial", "B", 8.5)
                self.set_fill_color(*self.C_PRIMARY)
                self.set_text_color(255, 255, 255)
                for i, h in enumerate(headers):
                    self.cell(col_widths[i], 7, h, border=0, fill=True, align="C")
                self.ln()
                self.set_font("Arial", "", 8.5)
                self.set_text_color(*self.C_TEXT)
                self.set_fill_color(*bg)
            x_start = self.l_margin
            y_start = self.get_y()
            for i, cell in enumerate(row):
                cx = x_start + sum(col_widths[:i])
                self.set_fill_color(*bg)
                self.rect(cx, y_start, col_widths[i], max_h, style="F")
                self.set_xy(cx + 1, y_start + 1)
                self.multi_cell(col_widths[i] - 2, 5, cell)
            self.set_y(y_start + max_h)
        self.ln(3)

    def priority_table(self, rows):
        w = self.w - self.l_margin - self.r_margin
        col_widths = [w * 0.12, w * 0.22, w * 0.66]
        colors = [self.C_GREEN, (41, 128, 185), self.C_ACCENT, self.C_PURPLE]
        # header
        self.set_font("Arial", "B", 8.5)
        self.set_fill_color(*self.C_PRIMARY)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(["Ưu tiên", "Nhóm", "Ví dụ"]):
            self.cell(col_widths[i], 7, h, border=0, fill=True, align="C")
        self.ln()
        for r_idx, row in enumerate(rows):
            self.set_font("Arial", "", 8.5)
            ls = self.multi_cell(col_widths[2] - 2, 5, row[2], dry_run=True, output="LINES")
            row_h = max(len(ls) * 5 + 2, 10)
            if self.get_y() + row_h > self.h - 22:
                self.add_page()
            x_start = self.l_margin
            y_start = self.get_y()
            bg = self.C_GRAY_BG if r_idx % 2 == 1 else (255, 255, 255)
            for i in range(3):
                self.set_fill_color(*bg)
                self.rect(x_start + sum(col_widths[:i]), y_start, col_widths[i], row_h, style="F")
            self.set_fill_color(*colors[r_idx])
            self.rect(x_start, y_start, 1.5, row_h, style="F")
            # text
            self.set_text_color(*self.C_TEXT)
            self.set_font("Arial", "B", 8.5)
            self.set_xy(x_start + 2, y_start + 1)
            self.cell(col_widths[0] - 4, 5, row[0], align="C")
            self.set_font("Arial", "", 8.5)
            self.set_xy(x_start + col_widths[0] + 1, y_start + 1)
            self.cell(col_widths[1] - 2, 5, row[1])
            self.set_xy(x_start + col_widths[0] + col_widths[1] + 1, y_start + 1)
            self.multi_cell(col_widths[2] - 2, 5, row[2])
            self.set_y(y_start + row_h)
        self.ln(3)

    def step_list(self, steps):
        for i, step in enumerate(steps, 1):
            x = self.l_margin
            w = self.w - self.l_margin - self.r_margin
            # measure
            self.set_font("Arial", "", 9)
            ls = self.multi_cell(w - 12, 5, step, dry_run=True, output="LINES")
            h = max(len(ls) * 5 + 1, 8)
            # Removed page break check - let content flow naturally
            y = self.get_y()
            # bg rect
            self.set_fill_color(*self.C_GRAY_BG)
            self.rect(x + 8, y, w - 8, h, style="F")
            # circle
            self.set_fill_color(*self.C_PRIMARY)
            self.ellipse(x + 1, y + 1, 5.5, 5.5, style="F")
            self.set_font("Arial", "B", 7.5)
            self.set_text_color(255, 255, 255)
            self.set_xy(x + 1.8, y + 1.5)
            self.cell(4, 4, str(i), align="C")
            # text
            self.set_xy(x + 10, y + 0.5)
            self.set_text_color(*self.C_TEXT)
            self.set_font("Arial", "", 9)
            self.multi_cell(w - 12, 5, step)
            self.set_y(y + h + 1.5)

    def bullet_list(self, items):
        self.set_font("Arial", "", 9.5)
        self.set_text_color(*self.C_TEXT)
        for item in items:
            if self.get_y() + 8 > self.h - 22:
                self.add_page()
            x = self.l_margin
            self.set_fill_color(*self.C_PRIMARY)
            self.ellipse(x + 2, self.get_y() + 2, 2, 2, style="F")
            self.set_x(x + 7)
            self.multi_cell(self.w - self.l_margin - self.r_margin - 7, 5.5, item)
            self.ln(1)


def build():
    pdf = MemoPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    lm = 20
    pdf.set_left_margin(lm)
    pdf.set_right_margin(lm)
    w = pdf.w - lm - pdf.r_margin

    # ── HEADER ──
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(*MemoPDF.C_PRIMARY)
    pdf.cell(0, 8, "NHẬT QUANG ĐÀ LẠT", align="C")
    pdf.ln(7)
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 6, "PHÒNG KẾ TOÁN", align="C")
    pdf.ln(7)
    pdf.set_draw_color(*MemoPDF.C_PRIMARY)
    pdf.set_line_width(0.8)
    pdf.line(lm, pdf.get_y(), lm + w, pdf.get_y())
    pdf.set_line_width(0.3)
    pdf.line(lm + w * 0.2, pdf.get_y() + 1.5, lm + w * 0.8, pdf.get_y() + 1.5)
    pdf.ln(6)

    # ── TITLE ──
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(*MemoPDF.C_MUTED)
    pdf.cell(0, 5, "MEMO NỘI BỘ", align="C")
    pdf.ln(6)
    pdf.set_font("Arial", "B", 15)
    pdf.set_text_color(*MemoPDF.C_PRIMARY)
    pdf.cell(0, 8, "HƯỚNG DẪN TRIỂN KHAI", align="C")
    pdf.ln(7)
    pdf.cell(0, 8, "KẾ HOẠCH THANH TOÁN THEO TUẦN", align="C")
    pdf.ln(7)
    pdf.set_font("Arial", "I", 9.5)
    pdf.set_text_color(52, 73, 94)
    pdf.cell(0, 6, 'V/v: Sử dụng mẫu file "Kế hoạch thanh toán – Đặt hàng"', align="C")
    pdf.ln(10)

    # ── META ──
    pdf.set_font("Arial", "", 8.5)
    pdf.set_text_color(85, 85, 85)
    meta_y = pdf.get_y()
    pdf.set_fill_color(240, 244, 248)
    pdf.rect(lm, meta_y, w / 3 - 2, 7, style="F")
    pdf.rect(lm + w / 3, meta_y, w / 3 - 2, 7, style="F")
    pdf.rect(lm + 2 * w / 3, meta_y, w / 3 - 2, 7, style="F")
    pdf.set_xy(lm + 2, meta_y + 1)
    pdf.cell(w / 3 - 6, 5, "Số: …/2026/MEMO-KT")
    pdf.set_xy(lm + w / 3 + 2, meta_y + 1)
    pdf.cell(w / 3 - 6, 5, "Ngày: 21/08/2026")
    pdf.set_xy(lm + 2 * w / 3 + 2, meta_y + 1)
    pdf.cell(w / 3 - 6, 5, "TL: Phòng Kế toán")
    pdf.set_y(meta_y + 12)

    # ── INTRO ──
    pdf.info_box(
        'Phòng Kế toán ban hành mẫu file "Kế hoạch thanh toán – Đặt hàng" để các cơ sở '
        "sử dụng trong việc lập kế hoạch thanh toán và theo dõi công nợ hàng tuần. "
        "Đề nghị các cơ sở thực hiện theo hướng dẫn dưới đây.",
        icon=">>"
    )

    # ── 1 ──
    pdf.section_title(1, "THỜI GIAN GỬI KẾ HOẠCH THANH TOÁN")

    y = pdf.get_y()
    if y + 20 > pdf.h - 22:
        pdf.add_page()
        y = pdf.get_y()
    pdf.set_fill_color(*MemoPDF.C_YELLOW_BG)
    pdf.rect(lm, y, w, 18, style="F")
    pdf.set_fill_color(*MemoPDF.C_ACCENT)
    pdf.rect(lm, y, 1.5, 18, style="F")
    pdf.set_xy(lm + 5, y + 2)
    pdf.set_font("Arial", "B", 10)
    pdf.set_text_color(125, 102, 8)
    pdf.cell(0, 6, "Hạn chót: Trước 12h00 trưa Thứ Bảy hàng tuần")
    pdf.set_xy(lm + 5, y + 9)
    pdf.set_font("Arial", "", 9)
    pdf.set_text_color(*MemoPDF.C_RED)
    pdf.cell(0, 5, "* Riêng tuần đầu tiên: trước 12h00 trưa Chủ Nhật")
    pdf.set_y(y + 22)

    pdf.body_text(
        "Các cơ sở gửi file đã điền đầy đủ thông tin về Phòng Kế toán "
        "để tổng hợp và xử lý thanh toán cho tuần tiếp theo."
    )

    # ── 2 ──
    pdf.section_title(2, "HƯỚNG DẪN ĐIỀN THÔNG TIN")
    pdf.body_text(
        'File gồm 4 tab, trong đó cơ sở chỉ cần điền thông tin vào tab "Chi tiết phải trả". '
        "Các tab còn lại phục vụ tra cứu và theo dõi."
    )
    pdf.sub_title('>>> Tab "Chi tiết phải trả" – Tab cần điền')
    pdf.body_text("Quy ước màu sắc trên file:", bold=True)

    y = pdf.get_y()
    legends = [
        ((254, 249, 231), (249, 231, 159), "Ô vàng = Cần điền"),
        ((212, 230, 241), (133, 193, 233), "Xanh dương = Nhập tay"),
        ((242, 243, 244), (213, 216, 220), "Cột tự động = Không điền"),
    ]
    for i, (bg, border, label) in enumerate(legends):
        x = lm + i * (w / 3)
        pdf.set_fill_color(*bg)
        pdf.set_draw_color(*border)
        pdf.rect(x + 1, y + 1, 5, 5, style="DF")
        pdf.set_font("Arial", "", 8)
        pdf.set_text_color(*MemoPDF.C_TEXT)
        pdf.set_xy(x + 8, y)
        pdf.cell(w / 3 - 10, 7, label)
    pdf.set_y(y + 10)

    pdf.body_text("Thông tin phần đầu file:", bold=True)
    pdf.simple_table(
        ["Mục", "Ghi chú"],
        [
            ["Từ ngày – Đến ngày", "Nhập khoảng thời gian của tuần thanh toán"],
            ["Cơ sở / Bộ phận", "Tên cơ sở của mình"],
            ["Người lập", "Họ tên nhân viên lập"],
            ["Trưởng bộ phận", "Họ tên người duyệt"],
        ],
        [w * 0.35, w * 0.65]
    )

    pdf.body_text("Các cột cần điền (chi tiết từng dòng):", bold=True)
    pdf.simple_table(
        ["Cột", "Nội dung", "Hướng dẫn"],
        [
            ["Tên NCC / Người yêu cầu", "Tên nhà cung cấp hoặc cá nhân", "Ghi đầy đủ họ tên"],
            ["Mặt hàng / Nội dung", "Nội dung thanh toán", "Mô tả ngắn gọn mặt hàng hoặc dịch vụ"],
            ["Ngày phát sinh nợ", "Ngày phát sinh khoản nợ", "Là ngày ord PO (ngày đặt hàng được duyệt)"],
            ["Hạn thanh toán", "Hạn phải thanh toán", 'Xem trong tab "Lịch thanh toán" của file'],
            ["Tổng nợ phải trả (VNĐ)", "Tổng số tiền nợ", "Ghi số tiền tổng cộng"],
            ["Phải trả lần này", "Số tiền đề xuất thanh toán đợt này", "Ghi số tiền cần thanh toán trong tuần"],
            ["Ghi chú", "Ghi chú thêm", "Nhập nếu cần"],
        ],
        [w * 0.22, w * 0.28, w * 0.50]
    )

    pdf.info_box(
        "Các cột Còn lại, Số ngày quá hạn, Ngày thanh toán, Thứ, Trạng thái/Mức ưu tiên "
        "tự động tính theo công thức — cơ sở KHÔNG cần nhập.",
        icon="[*]"
    )

    # ── 3 ──
    pdf.section_title(3, 'TAB "TỔNG HỢP" – THEO DÕI CÔNG NỢ')
    pdf.body_text(
        'Tab này tự động tổng hợp từ dữ liệu ở tab "Chi tiết phải trả", '
        "giúp cơ sở tự theo dõi tình hình công nợ:"
    )
    pdf.bullet_list([
        "Tổng số nhà cung cấp còn nợ",
        "Tổng công nợ phải trả",
        "Tổng số tiền phải trả lần này",
        "Tỷ lệ thanh toán",
        "Phân loại công nợ theo mức độ quá hạn (chưa đến hạn, quá hạn 1–30 ngày, 31–60 ngày, trên 60 ngày, đã thanh toán đủ)",
    ])
    pdf.info_box(
        'Cơ sở KHÔNG cần điền tab này, chỉ cần theo dõi để nắm tình trạng công nợ.',
        icon="[*]"
    )

    # ── 4 ──
    pdf.section_title(4, 'TAB "LỊCH THANH TOÁN" – TRA CỨU HẠN THANH TOÁN')
    pdf.body_text(
        "Tab này quy định lịch thanh toán cho từng nhóm đối tượng, chia theo 4 mức ưu tiên:"
    )
    pdf.priority_table([
        ["1", "Chi phí cơ sở", "Petty cash, taxi, hoa hồng CTV, công tác phí, hoàn tiền khách, ban nhạc, âm thanh ánh sáng, lương part-time, phí marketing, KOC/review, in ấn…"],
        ["2", "Định kỳ", "Điện, nước, hotline, rác thải, lương, bảo hiểm, thuê mặt bằng, thuế phí"],
        ["3", "Nhà cung cấp", "Bia, củi, rượu, nước rửa chén, giấy, thực phẩm, gia vị, nước đá, cồn, than, gạo, CCDC, hàng pha chế, gas…"],
        ["4", "Back office", "Chi phí hành chính, thiết bị IT, phát sinh khác"],
    ])
    pdf.info_box(
        "Khi phát sinh NCC mới: Cơ sở cần đề xuất thêm NCC theo quy trình hiện hành và "
        "bổ sung vào lịch thanh toán để Phòng Kế toán cập nhật khung thời gian phù hợp.",
        icon="[!]"
    )

    # ── 5 ──
    pdf.section_title(5, 'TAB "LỊCH MUA HÀNG" – THEO DÕI THỜI GIAN ĐẶT HÀNG')
    pdf.body_text(
        "Tab này quy định lịch đặt hàng và thời gian nhận hàng cho từng phân loại mặt hàng "
        "theo từng cơ sở (Buôn Kơ Lang, Air Dream 2, Thơm + Air Dream 1, Trại Mèo Mướp…)."
    )
    pdf.body_text(
        "Cơ sở tự theo dõi thời gian giao hàng theo từng nhóm mặt hàng để phân bổ "
        "thời gian đặt hàng (ord PO) phù hợp, đảm bảo hàng về đúng tiến độ phục vụ kinh doanh."
    )
    pdf.info_box(
        "Thời gian xử lý mua hàng được tính bắt đầu khi PO được duyệt thành công trên Bflow "
        "(không tính ngày Chủ Nhật).",
        bg=MemoPDF.C_YELLOW_BG,
        border_color=MemoPDF.C_ACCENT,
        icon="[!]"
    )

    # ── 6 ──
    pdf.section_title(6, "TÓM TẮT QUY TRÌNH HÀNG TUẦN")
    
    steps_content = [
        "Rà soát công nợ phải trả, đối chiếu với lịch thanh toán trên file",
        'Điền đầy đủ thông tin vào tab "Chi tiết phải trả" (tra mã NCC trên MDM, điền các cột theo hướng dẫn)',
        'Kiểm tra tab "Tổng hợp" để nắm tình trạng công nợ chung',
        "Gửi file về Phòng Kế toán trước 12h00 Thứ Bảy hàng tuần",
    ]
    
    pdf.step_list(steps_content)

    # ── CLOSING ──
    pdf.ln(2)
    y = pdf.get_y()
    pdf.set_fill_color(*MemoPDF.C_LIGHT_BG)
    pdf.rect(lm, y, w, 10, style="F")
    pdf.set_xy(lm + 4, y + 2)
    pdf.set_font("Arial", "", 9)
    pdf.set_text_color(*MemoPDF.C_TEXT)
    pdf.multi_cell(w - 8, 5, "Mọi thắc mắc vui lòng liên hệ Phòng Kế toán để được hỗ trợ.")
    pdf.set_y(y + 13)

    # ── SIGNATURE (compact) ──
    pdf.ln(3)
    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 4, "Trân trọng,", align="R")
    pdf.ln(5)
    pdf.set_font("Arial", "B", 9)
    pdf.cell(0, 4, "PHÒNG KẾ TOÁN — Nhật Quang Đà Lạt", align="R")
    pdf.ln(6)

    # ── FOOTER LINE ──
    pdf.set_draw_color(*MemoPDF.C_BORDER)
    pdf.set_line_width(0.3)
    pdf.line(lm, pdf.get_y(), lm + w, pdf.get_y())
    pdf.ln(2)
    pdf.set_font("Arial", "I", 7.5)
    pdf.set_text_color(*MemoPDF.C_MUTED)
    pdf.cell(0, 5, "Memo này có giá trị hướng dẫn nội bộ — Phòng Kế toán phát hành ngày 21/08/2026", align="C")

    out = "/Users/teatea/Documents/Nhật Quang/SecondBrain/Memo-KHTT-Tuan.pdf"
    pdf.output(out)
    print(f"PDF saved: {out}  ({pdf.page_no()} pages)")


if __name__ == "__main__":
    build()
