import tkinter as tk
import math
import time

class WowClock(tk.Tk):
    def __init__(self):
        super().__init__()   
        self.title("Digital Analog Clock")
        self.geometry("420x520")
        self.configure(bg = "#0f172a")
        self.resizable(False, False)
        
        self.cx = 210
        self.cy = 200
        self.radius = 140
        
        self.canvas = tk.Canvas( self,
            width=420,
            height=400,
            bg = '#0f172a',
            highlightthickness=0  
        )
        self.canvas.pack()
        self.create_clock_face()
        self.create_hands()
        self.create_digital_display()
        self.update_clock()
        
        
        
    #Creating Clock Face 
    def create_clock_face(self):
        self.canvas.create_oval(
            self.cx - self.radius,
            self.cy - self.radius,
            self.cx + self.radius,
            self.cy + self.radius,
            outline = '#38bdf8',
            width=4
        )
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x = self.cx + (self.radius - 20) * math.cos(angle)
            y = self.cy + (self.radius - 20) * math.sin(angle)
            self.canvas.create_text(
                x,y,
                text=str(i if i else 12),
                fill = "white",
                font=("Arial", 14, "bold")
            )        
    # Creating Hands
    def create_hands(self):
        self.hour_hand = self.canvas.create_line(
            self.cx, self.cy, self.cx, self.cy - 60,
            width=6, fill = "white", capstyle=tk.ROUND
        )
        self.min_hand = self.canvas.create_line(
            self.cx, self.cy, self.cx, self.cy - 95,
            width=2, fill="#38bdf8", capstyle= tk.ROUND
        )
        self.sec_hand = self.canvas.create_line(
            self.cx, self.cy, self.cx, self.cy - 115,
            width=2, fill="#ef4444", capstyle= tk.ROUND
        )
        self.canvas.create_oval(
            self.cx - 6, self.cy - 6,
            self.cx + 6, self.cy + 6,
            fill='white'
        )
    # Create Digital
    def create_digital_display(self):
        self.time_label  = tk.Label(
            self,
            font = ("Consolas", 28, "bold"),
            bg = "#0f172a",
            fg = "#38bdf8"
        )
        self.time_label.pack(pady=(10, 0))
        self.date_label = tk.Label(
            self,
            font = ("Consolas",14),
            bg = "#0f172a",
            fg = "white"
        )
        self.date_label.pack()
        
    #Upadting 
    def update_clock(self):
        now = time.localtime()
        hour = (now.tm_hour %12) + now.tm_min / 60
        minute = now.tm_min + now.tm_sec / 60
        second = now.tm_sec
        
        self.rotate_hand(self.hour_hand, hour * 30, 70)
        self.rotate_hand(self.min_hand, minute * 6, 100)
        self.rotate_hand(self.sec_hand, second * 6, 120)
        
        self.time_label.config(
            text= time.strftime(" %I:%M:%S %p")
        )
        self.date_label.config(
            text= time.strftime("%A, %d %B %Y")
        )
        self.after(1000, self.update_clock)
        
    def rotate_hand(self, hand, angle, length):
        rad = math.radians(angle - 90)
        x = self.cx + length * math.cos(rad)
        y = self.cy + length * math.sin(rad)
        self.canvas.coords(hand, self.cx, self.cy, x, y)
        
if __name__ =="__main__":
    WowClock().mainloop()
        