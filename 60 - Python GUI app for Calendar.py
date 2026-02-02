import tkinter as tk
import calendar
from datetime import datetime

# ---------------- CONFIG ----------------
BG = "#f8fafc"
MONTH_BG = "#ffffff"
TODAY_COLOR = "#2563eb"
EVENT_COLOR = "#16a34a"
SUNDAY_COLOR = "#dc2626"
TEXT_COLOR = "#0f172a"

CARD_W = 260
CARD_H = 190
CELL_W = 3

# ---------------- FESTIVALS (ALL YEARS) ----------------
FESTIVALS = {
    (1, 26): "Republic Day 🇮🇳",
    (3, 8): "Holi 🎨",
    (8, 15): "Independence Day 🇮🇳",
    (10, 2): "Gandhi Jayanti",
    (12, 25): "Christmas 🎄",
}

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Full Year Calendar")
root.geometry("1150x780")
root.configure(bg=BG)

today = datetime.now()
current_year = today.year

# ---------------- FUNCTIONS ----------------
def show_event(text):
    event_label.config(text=text if text else "No event on this date")

def draw_calendar(year):
    for w in cal_frame.winfo_children():
        w.destroy()

    year_label.config(text=str(year))
    show_event("")

    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    row = col = 0
    for month in range(1, 13):
        card = tk.Frame(
            cal_frame, bg=MONTH_BG,
            width=CARD_W, height=CARD_H,
            bd=1, relief="solid"
        )
        card.grid(row=row, column=col, padx=8, pady=8)
        card.grid_propagate(False)

        # Month title
        tk.Label(
            card, text=calendar.month_name[month],
            font=("Arial", 11, "bold"),
            bg=MONTH_BG, fg=TEXT_COLOR
        ).pack()

        grid = tk.Frame(card, bg=MONTH_BG)
        grid.pack()

        # Weekdays
        for i, d in enumerate(weekdays):
            tk.Label(
                grid, text=d, width=CELL_W,
                bg=MONTH_BG,
                fg=SUNDAY_COLOR if d == "Su" else TEXT_COLOR,
                font=("Arial", 9, "bold")
            ).grid(row=0, column=i)

        # Always 6 rows (IMPORTANT FIX)
        month_days = calendar.monthcalendar(year, month)
        while len(month_days) < 6:
            month_days.append([0]*7)

        for r in range(6):
            for c in range(7):
                day = month_days[r][c]
                text = "" if day == 0 else str(day)

                fg = TEXT_COLOR
                bg = MONTH_BG
                event_text = ""

                if day != 0 and (month, day) in FESTIVALS:
                    fg = EVENT_COLOR
                    event_text = FESTIVALS[(month, day)]

                if (day == today.day and month == today.month and year == today.year):
                    bg = TODAY_COLOR
                    fg = "white"

                lbl = tk.Label(
                    grid, text=text, width=CELL_W,
                    bg=bg, fg=fg, font=("Arial", 9)
                )

                if event_text:
                    lbl.bind("<Button-1>", lambda e, t=event_text: show_event(t))

                lbl.grid(row=r+1, column=c, pady=1)

        col += 1
        if col == 4:
            col = 0
            row += 1

def prev_year():
    global current_year
    current_year -= 1
    draw_calendar(current_year)

def next_year():
    global current_year
    current_year += 1
    draw_calendar(current_year)

def go_year():
    global current_year
    try:
        current_year = int(year_entry.get())
        draw_calendar(current_year)
    except:
        year_entry.delete(0, tk.END)

# ---------------- HEADER ----------------
top = tk.Frame(root, bg=BG)
top.pack(pady=5)

tk.Button(top, text="◀", command=prev_year).pack(side="left", padx=5)

year_label = tk.Label(
    top, text="", font=("Arial", 22, "bold"),
    bg=BG
)
year_label.pack(side="left", padx=10)

tk.Button(top, text="▶", command=next_year).pack(side="left", padx=5)

year_entry = tk.Entry(top, width=8)
year_entry.pack(side="left", padx=10)

tk.Button(top, text="Go", command=go_year).pack(side="left")

# ---------------- EVENT DISPLAY ----------------
event_label = tk.Label(
    root,
    text="Click green date to see event",
    bg="#ecfeff",
    fg="#0369a1",
    font=("Arial", 12),
    height=2
)
event_label.pack(fill="x", padx=20, pady=5)

# ---------------- CALENDAR GRID ----------------
cal_frame = tk.Frame(root, bg=BG)
cal_frame.pack()

draw_calendar(current_year)

root.mainloop()
