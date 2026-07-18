import customtkinter as ctk
from tkinter import Canvas

# =========================
# App Setup
# =========================
app = ctk.CTk()
app.title("MOMENTUM")

# Fullscreen (all monitors)
app.attributes("-fullscreen", True)
app.bind("<Escape>", lambda e: app.destroy())

WIDTH = app.winfo_screenwidth()
HEIGHT = app.winfo_screenheight()

# =========================
# Responsive Scaling
# =========================
scale = HEIGHT / 1080

TITLE_FONT = int(70 * scale)
SUBTITLE_FONT = int(22 * scale)
MENU_FONT = int(40 * scale)

# =========================
# Canvas
# =========================
canvas = Canvas(app, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# =========================
# Gradient Helpers
# =========================
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# =========================
# Gradient Background
# =========================
stops = [
    (0.00, "#0A0A0A"),
    (0.35, "#2B1450"),
    (0.70, "#3C1973"),
    (1.00, "#4C1D95")
]

for y in range(HEIGHT):
    t = y / HEIGHT

    for i in range(len(stops) - 1):
        if stops[i][0] <= t <= stops[i + 1][0]:

            t1, c1 = stops[i]
            t2, c2 = stops[i + 1]

            p = (t - t1) / (t2 - t1)

            r1, g1, b1 = hex_to_rgb(c1)
            r2, g2, b2 = hex_to_rgb(c2)

            r = int(r1 + (r2 - r1) * p)
            g = int(g1 + (g2 - g1) * p)
            b = int(b1 + (b2 - b1) * p)

            canvas.create_line(0, y, WIDTH, y, fill=rgb_to_hex((r, g, b)))
            break

# =========================
# Corner Decorations
# =========================
canvas.create_line(15, HEIGHT-120, 15, HEIGHT-15, 120, HEIGHT-15,
                   fill="white", width=4, capstyle="round", joinstyle="round")

canvas.create_line(27, HEIGHT-108, 27, HEIGHT-27, 108, HEIGHT-27,
                   fill="white", width=2, capstyle="round", joinstyle="round")

canvas.create_line(WIDTH-120, 15, WIDTH-15, 15, WIDTH-15, 120,
                   fill="white", width=4, capstyle="round", joinstyle="round")

canvas.create_line(WIDTH-108, 27, WIDTH-27, 27, WIDTH-27, 108,
                   fill="white", width=2, capstyle="round", joinstyle="round")

# =========================
# Title
# =========================
canvas.create_text(
    WIDTH // 2,
    HEIGHT // 6,
    text="W E L C O M E",
    fill="white",
    font=("Fontype Rounded", TITLE_FONT, "bold")
)

canvas.create_text(
    WIDTH // 2,
    HEIGHT // 4,
    text="Y O U ' R E  G O I N G  T O  C R U S H  I T  T O D A Y",
    fill="white",
    font=("Fontype Rounded", 30, "bold"),
    justify="center"
)

# =========================
# Menu
# =========================
start_y = HEIGHT // 3 + 50
spacing = 120 * scale

menu_items = [
    "S T A R T",
    "S T A T I S T I C S",
    "S E T T I N G S",
    "E X I T"
]

canvas_items = {}

for i, text in enumerate(menu_items):
    y = start_y + i * spacing

    item = canvas.create_text(
        WIDTH // 2,
        y,
        text=text,
        fill="white",
        font=("Bahnschrift Condensed", MENU_FONT, "bold")
    )

    canvas_items[text] = item

    def enter(e, i=item):
        canvas.itemconfig(i, fill="#000000")

    def leave(e, i=item):
        canvas.itemconfig(i, fill="white")

    canvas.tag_bind(item, "<Enter>", enter)
    canvas.tag_bind(item, "<Leave>", leave)


# =========================
# Version Text
# =========================
canvas.create_text(
    WIDTH - 20,
    HEIGHT - 15,
    text="VERSION 1.0",
    fill="white",
    font=("Bahnschrift Condensed", int(14 * scale)),
    anchor="se"
)

app.mainloop()