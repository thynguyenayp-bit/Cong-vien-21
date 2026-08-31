#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sơ đồ Airdream Forest Station - cải tiến bố cục"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def draw_layout():
    fig, ax = plt.subplots(1, 1, figsize=(22, 28))
    ax.set_xlim(-2, 24)
    ax.set_ylim(-4, 30)
    ax.set_aspect('equal')
    ax.axis('off')

    colors = {
        't0': '#E8D5B7',
        't1': '#B7D5E8',
        't2': '#B7E8C5',
        't3': '#E8B7D5',
        't4': '#D5B7E8',
        't5': '#F0E68C',
        'suoi': '#A0C4FF',
        'buon': '#D4EDDA',
        'co': '#C8E6C9',
        'xe': '#FFE0B2',
        'wc': '#E0E0E0',
        'duong': '#F5F5F5',
    }

    def rect(x, y, w, h, color, label, text_color='black', fontsize=9, bold=False, alpha=1.0, ls='-'):
        r = patches.Rectangle((x, y), w, h, linewidth=2 if bold else 1.5, edgecolor='#333', facecolor=color, alpha=alpha, linestyle=ls)
        ax.add_patch(r)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=fontsize,
                color=text_color, weight=weight, wrap=True)
        return r

    def label(x, y, text, fontsize=11, color='black', ha='center', va='center', weight='bold'):
        ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize, color=color, weight=weight)

    def arrow(x1, y1, x2, y2, text='', color='#555', lw=1.5, style='->'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle=style, color=color, lw=lw, connectionstyle='arc3,rad=0'))
        if text:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my+0.25, text, ha='center', va='bottom', fontsize=8, color='#444',
                    bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.85, edgecolor='none'))

    def stairs(x1, y1, x2, y2, n=3, text='bậc thang'):
        ax.plot([x1, x2], [y1, y2], 'k--', lw=1.2)
        for i in range(1, n):
            t = i / n
            xi = x1 + t*(x2-x1)
            yi = y1 + t*(y2-y1)
            dx = (x2-x1)*0.04
            dy = (y2-y1)*0.04
            ax.plot([xi, xi+dx], [yi, yi], 'k-', lw=1.2)
            ax.plot([xi+dx, xi+dx], [yi, yi+dy], 'k-', lw=1.2)
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx, my+0.15, text, ha='center', va='center', fontsize=8, color='#333',
                bbox=dict(boxstyle='round,pad=0.12', facecolor='white', alpha=0.9, edgecolor='none'))

    # ========== TẦNG 0 ==========
    label(11, 29, 'TẦNG 0', fontsize=13, color='#5D4037')
    # Hàng rào + mặt tiền Trần Quang Diệu
    ax.plot([-1, 23], [28.5, 28.5], 'k-', lw=2.5)
    label(11, 28.8, 'Mặt tiền Trần Quang Diệu', fontsize=10, color='#5D4037', weight='normal')
    # Cổng chính
    rect(6, 27.2, 10, 1.2, colors['t0'], 'CỔNG CHÍNH\nTrần Quang Diệu', fontsize=11, bold=True)
    # Bãi xe máy hai bên
    rect(1, 27.0, 4.5, 1.5, colors['t0'], 'Bãi xe máy', fontsize=10)
    rect(16.5, 27.0, 4.5, 1.5, colors['t0'], 'Bãi xe máy', fontsize=10)
    # 4 bậc thang xuống tầng 1
    arrow(11, 27.2, 11, 25.3, text='4 bậc thang xuống', color='#444', lw=2)

    # ========== TẦNG 1 ==========
    label(11, 24.8, 'TẦNG 1', fontsize=13, color='#1565C0')
    # Ngã tư
    rect(10.2, 23.5, 1.6, 1.2, colors['duong'], 'NGÃ TƯ', fontsize=9, bold=True)
    # Xe cà phê trái
    rect(3.5, 22.8, 5.5, 2.2, colors['xe'], 'XE CÀ PHÊ\n(order chính)', fontsize=10, bold=True)
    # Xe pizza phải
    rect(13, 22.8, 5.5, 2.2, colors['xe'], 'XE PIZZA\n(order chính)', fontsize=10, bold=True)
    # Lối chính xuống sảnh B
    arrow(11, 23.5, 11, 20.8, text='lối đi chính', color='#444', lw=2)
    # Lối lấy món từ sau xe
    arrow(5.5, 22.8, 8.5, 21.5, text='lấy món', color='#666', lw=1.5)
    arrow(16.5, 22.8, 13.5, 21.5, text='lấy món', color='#666', lw=1.5)
    # Hợp lại với lối chính
    arrow(8.5, 21.5, 10.2, 21.0, text='', color='#666', lw=1.5)
    arrow(13.5, 21.5, 11.8, 21.0, text='', color='#666', lw=1.5)
    # Bậc thang từ cổng xuống ngã tư
    stairs(10.2, 25.3, 10.2, 24.7, n=4, text='từ cổng')
    stairs(11.8, 25.3, 11.8, 24.7, n=4, text='')

    # ========== TẦNG 2 ==========
    label(11, 20.2, 'TẦNG 2', fontsize=13, color='#2E7D32')
    # Sảnh B trung tâm
    rect(7, 18.2, 8, 2.5, colors['t2'], 'B\nSảnh trung tâm\n(~72m²)', fontsize=12, bold=True)
    # R1 bên phải B
    rect(15.5, 18.2, 3.5, 2.5, colors['xe'], 'R1\nXe trang trí\n(~20m²)', fontsize=9, bold=True)
    # Chỗ ngồi phía trước R1
    rect(15.5, 16.5, 3.5, 1.4, colors['t2'], 'chỗ ngồi\ntrước R1\n(~8m²)', fontsize=8)
    # Lối B -> R1
    arrow(15, 19.45, 15.5, 19.45, text='0.8m', color='#444', lw=1.5)
    # Bậc thang xuống tầng 3: BL1 (trái) và BR1 (phải)
    stairs(8.5, 18.2, 5.5, 15.8, n=3, text='xuống BL1')
    stairs(13.5, 18.2, 16.5, 15.8, n=3, text='xuống BR1')

    # ========== TẦNG 3 ==========
    label(11, 15.2, 'TẦNG 3', fontsize=13, color='#C2185B')
    # BL1 bên trái
    rect(3, 13.8, 5, 2.5, colors['t3'], 'BL1\n(~35m²)', fontsize=11, bold=True)
    # BR1 bên phải
    rect(14, 13.8, 4, 2.5, colors['t3'], 'BR1\n(~25m²)', fontsize=11, bold=True)
    # Lối BR1 -> R1 (ngược lên)
    arrow(14, 14.95, 15.5, 17.5, text='lối đi', color='#444', lw=1.5)
    # Lối đi từ BL1 sang trái ~3m
    rect(-1.5, 14.5, 4.5, 0.8, colors['duong'], 'lối đi ~3m', fontsize=8)
    arrow(3, 15.0, -1.5, 15.0, text='0.8m', color='#444', lw=1.5)
    # L1, L2 từ lối đi rẽ ra
    rect(-3.5, 15.8, 2, 1.6, colors['xe'], 'L1\nxe trang trí', fontsize=9)
    rect(-3.5, 13.5, 2, 1.8, colors['xe'], 'L2\nxe trang trí\n(nhỏ hơn)', fontsize=8)
    arrow(-1.5, 15.5, -2.5, 16.6, text='rẽ', color='#444', lw=1.2)
    arrow(-1.5, 15.5, -2.5, 14.4, text='rẽ', color='#444', lw=1.2)
    # Bậc thang BL1 -> BL2
    stairs(5.5, 13.8, 5.5, 10.8, n=3, text='xuống BL2')

    # ========== TẦNG 4 ==========
    label(11, 10.2, 'TẦNG 4', fontsize=13, color='#7B1FA2')
    # BL2 bên trái
    rect(3, 8.8, 5, 2.5, colors['t4'], 'BL2\n(~30m²)', fontsize=11, bold=True)
    # BR2 bên phải
    rect(14, 8.8, 4.5, 2.5, colors['t4'], 'BR2\n(~42m²)', fontsize=11, bold=True)
    # Bậc thang BR1 -> BR2
    stairs(16, 13.8, 16, 11.3, n=3, text='xuống BR2')
    # R2 mái che bên phải
    rect(15.5, 6.0, 4, 2.0, colors['t4'], 'R2\nMái che\n(~25m²)', fontsize=9)
    # R3 mái che xéo bên phải dưới (giáp trái suối)
    rect(19, 6.0, 3.5, 2.0, colors['t4'], 'R3\nMái che\n(~25m²)\n[giáp suối]', fontsize=8)
    # M mái che giữa
    rect(9, 6.0, 4, 2.0, colors['t4'], 'M\nMái che\n(~25m²)\n[giữa suối]', fontsize=9, bold=True)
    # L3 xe trang trí bên trái
    rect(-2.5, 8.5, 3, 2.0, colors['xe'], 'L3\nXe trang trí', fontsize=9)
    # Lối từ BL2 -> L3
    arrow(3, 10.0, -0.5, 9.5, text='0.8m', color='#444', lw=1.5)
    # Các lối từ BR2
    arrow(16.25, 8.8, 17.5, 8.0, text='0.8m', color='#444', lw=1.5)
    arrow(16.25, 8.8, 20.5, 8.0, text='0.8m', color='#444', lw=1.5)
    arrow(14, 9.5, 11, 8.0, text='0.8m', color='#444', lw=1.5)
    # Bậc thang từ R3 xuống đầu suối
    stairs(20.5, 6.0, 20.5, 4.5, n=3, text='xuống đầu suối')
    # Bậc thang từ lối L3 xuống cuối suối
    stairs(-0.5, 8.5, -0.5, 4.5, n=4, text='xuống cuối suối')

    # ========== SUỐI NHÂN TẠO & BÃI CỎ ==========
    # Bãi cỏ 3m ranh giới
    grass = patches.Rectangle((-2, 3.5), 26, 1.0, linewidth=2, edgecolor='#388E3C',
                              facecolor=colors['co'], alpha=0.5)
    ax.add_patch(grass)
    label(11, 4.0, 'Bãi cỏ 3m (ranh giới Airdream - Buôn Ko Lang)', fontsize=10, color='#2E7D32', weight='normal')

    # Suối nhân tạo
    suoi = patches.Rectangle((-2, 2.3), 26, 1.0, linewidth=2, edgecolor='#1E88E5',
                              facecolor=colors['suoi'], alpha=0.6)
    ax.add_patch(suoi)
    label(11, 2.8, 'Suối nhân tạo - đầu suối (phải) → cuối suối (trái)', fontsize=10, color='#0D47A1', weight='normal')
    arrow(20, 2.8, 2, 2.8, text='', color='#1E88E5', lw=2.5)

    # ========== TẦNG 5 ==========
    label(11, 1.6, 'TẦNG 5 (sau suối)', fontsize=13, color='#F57F17')
    # Nhà vệ sinh
    rect(0, 0.2, 3.5, 1.5, colors['wc'], 'WC trái\n(dùng chung)', fontsize=10, bold=True)
    rect(18.5, 0.2, 3.5, 1.5, colors['wc'], 'WC phải\n(dùng chung)', fontsize=10, bold=True)
    # Bậc thang từ WC lên suối (ngầm định)
    arrow(3.5, 1.0, -0.5, 2.3, text='', color='#666', lw=1.2)
    arrow(18.5, 1.0, 20.5, 2.3, text='', color='#666', lw=1.2)

    # ========== BUÔN KO LANG ==========
    rect(2, -2.8, 18, 2.0, colors['buon'], 'BUÔN KO LANG\n(~4500m², mặt tiền Hùng Vương)', fontsize=12, bold=True)
    ax.annotate('', xy=(11, -2.8), xytext=(11, -3.2),
                arrowprops=dict(arrowstyle='->', color='#555', lw=2))
    label(11, -3.4, 'Mặt tiền Hùng Vương', fontsize=10, color='#555', weight='normal')

    # ========== CHÚ THÍCH ==========
    legend_items = [
        ('Tầng 0', colors['t0']),
        ('Tầng 1', colors['t1']),
        ('Tầng 2', colors['t2']),
        ('Tầng 3', colors['t3']),
        ('Tầng 4', colors['t4']),
        ('Tầng 5 / WC', colors['t5']),
        ('Xe / trang trí', colors['xe']),
        ('Suối nhân tạo', colors['suoi']),
        ('Bãi cỏ ranh giới', colors['co']),
        ('Buôn Ko Lang', colors['buon']),
    ]
    lx = 0
    ly = 30.2
    for i, (txt, c) in enumerate(legend_items):
        ax.add_patch(patches.Rectangle((lx + i*2.1, ly), 1.8, 0.45, facecolor=c, edgecolor='#333'))
        ax.text(lx + i*2.1 + 0.9, ly - 0.25, txt, ha='center', va='top', fontsize=8)

    ax.set_title('AIRDREAM FOREST STATION - SƠ ĐỒ BỐ TRÍ KHÔNG GIAN', fontsize=18, weight='bold', y=0.97)

    plt.tight_layout()
    plt.savefig('/Users/teatea/Documents/Nhật Quang/SecondBrain/airdream_forest_station_layout.png',
                dpi=250, bbox_inches='tight', facecolor='white')
    plt.close()
    print('Saved: airdream_forest_station_layout.png')

def draw_topology():
    """Sơ đồ topology - mối liên kết giữa các khu vực"""
    fig, ax = plt.subplots(1, 1, figsize=(18, 16))
    ax.set_xlim(-2, 22)
    ax.set_ylim(-2, 20)
    ax.set_aspect('equal')
    ax.axis('off')

    # Nodes: (x, y, label, color, fontsize)
    nodes = [
        (11, 18, 'Cổng\n(Tầng 0)', '#E8D5B7', 10),
        (11, 15, 'Ngã tư\nTầng 1', '#B7D5E8', 10),
        (7, 15, 'Xe cà phê\n(order)', '#FFE0B2', 9),
        (15, 15, 'Xe pizza\n(order)', '#FFE0B2', 9),
        (11, 11, 'B\nSảnh trung tâm\n(Tầng 2)', '#B7E8C5', 11),
        (15.5, 11, 'R1\nxe trang trí', '#FFE0B2', 9),
        (5, 8, 'BL1\nTầng 3', '#E8B7D5', 10),
        (17, 8, 'BR1\nTầng 3', '#E8B7D5', 10),
        (2, 8, 'L1\nxe trang trí', '#FFE0B2', 8),
        (2, 5.5, 'L2\nxe trang trí', '#FFE0B2', 8),
        (5, 4, 'BL2\nTầng 4', '#D5B7E8', 10),
        (17, 4, 'BR2\nTầng 4', '#D5B7E8', 10),
        (2, 4, 'L3\nxe trang trí', '#FFE0B2', 8),
        (13, 1, 'M\nmái che', '#D5B7E8', 9),
        (17, 1, 'R2\nmái che', '#D5B7E8', 9),
        (20, 1, 'R3\nmái che', '#D5B7E8', 9),
        (11, -1, 'Suối nhân tạo', '#A0C4FF', 10),
        (4, -1, 'WC trái', '#E0E0E0', 9),
        (18, -1, 'WC phải', '#E0E0E0', 9),
        (11, -3, 'Buôn Ko Lang', '#D4EDDA', 10),
    ]

    node_positions = {}
    for x, y, lab, c, fs in nodes:
        r = 0.9
        circle = patches.Circle((x, y), r, facecolor=c, edgecolor='#333', linewidth=2, alpha=0.95)
        ax.add_patch(circle)
        ax.text(x, y, lab, ha='center', va='center', fontsize=fs, weight='bold', wrap=True)
        node_positions[lab.split('\n')[0]] = (x, y)

    # Edges: (from, to, label, color)
    edges = [
        ('Cổng', 'Ngã tư', '4 bậc', '#444'),
        ('Ngã tư', 'Xe cà phê', 'lối đi', '#666'),
        ('Ngã tư', 'Xe pizza', 'lối đi', '#666'),
        ('Ngã tư', 'B', 'lối chính', '#444'),
        ('Xe cà phê', 'B', 'lấy món', '#666'),
        ('Xe pizza', 'B', 'lấy món', '#666'),
        ('B', 'R1', '0.8m', '#444'),
        ('B', 'BL1', '3 bậc', '#444'),
        ('B', 'BR1', '3 bậc', '#444'),
        ('BR1', 'R1', 'lối đi', '#666'),
        ('BR1', 'BR2', '3 bậc', '#444'),
        ('BL1', 'L1', 'rẽ', '#666'),
        ('BL1', 'L2', 'rẽ', '#666'),
        ('BL1', 'BL2', '3 bậc', '#444'),
        ('BL2', 'L3', '0.8m', '#666'),
        ('BR2', 'R2', '0.8m', '#666'),
        ('BR2', 'R3', '0.8m', '#666'),
        ('BR2', 'M', '0.8m', '#666'),
        ('R3', 'Suối', 'xuống đầu', '#1E88E5'),
        ('L3', 'Suối', 'xuống cuối', '#1E88E5'),
        ('Suối', 'WC trái', 'sau suối', '#666'),
        ('Suối', 'WC phải', 'sau suối', '#666'),
        ('Suối', 'Buôn Ko Lang', 'bãi cỏ 3m', '#388E3C'),
    ]

    def get_pos(name):
        # Map short names to node keys
        mapping = {
            'Cổng': 'Cổng',
            'Ngã tư': 'Ngã tư',
            'Xe cà phê': 'Xe cà phê',
            'Xe pizza': 'Xe pizza',
            'B': 'B',
            'R1': 'R1',
            'BL1': 'BL1',
            'BR1': 'BR1',
            'L1': 'L1',
            'L2': 'L2',
            'BL2': 'BL2',
            'BR2': 'BR2',
            'L3': 'L3',
            'M': 'M',
            'R2': 'R2',
            'R3': 'R3',
            'Suối': 'Suối',
            'WC trái': 'WC trái',
            'WC phải': 'WC phải',
            'Buôn Ko Lang': 'Buôn Ko Lang',
        }
        return node_positions[mapping[name]]

    for f, t, lab, col in edges:
        x1, y1 = get_pos(f)
        x2, y2 = get_pos(t)
        # Offset for arrow start/end to not overlap circle
        dx, dy = x2 - x1, y2 - y1
        dist = np.hypot(dx, dy)
        r = 0.95
        if dist > 0:
            x1p, y1p = x1 + r*dx/dist, y1 + r*dy/dist
            x2p, y2p = x2 - r*dx/dist, y2 - r*dy/dist
        else:
            x1p, y1p, x2p, y2p = x1, y1, x2, y2
        ax.annotate('', xy=(x2p, y2p), xytext=(x1p, y1p),
                    arrowprops=dict(arrowstyle='->', color=col, lw=1.5, connectionstyle='arc3,rad=0.05'))
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx, my, lab, ha='center', va='center', fontsize=8, color='#333',
                bbox=dict(boxstyle='round,pad=0.12', facecolor='white', alpha=0.85, edgecolor='none'))

    ax.set_title('AIRDREAM FOREST STATION - SƠ ĐỒ KẾT NỐI / FLOW GIỮA CÁC KHU VỰC', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig('/Users/teatea/Documents/Nhật Quang/SecondBrain/airdream_forest_station_topology.png',
                dpi=250, bbox_inches='tight', facecolor='white')
    plt.close()
    print('Saved: airdream_forest_station_topology.png')

if __name__ == '__main__':
    draw_layout()
    draw_topology()
