import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.theme_use("arc")  

        # تنظيم رنگ پس زمينه
        self.style.configure("TFrame", background="purple")

        self.time_var = tk.StringVar()
        self.time_var.set("00:00")

        
        self.frame = ttk.Frame(self.master, style="TFrame")
        self.frame.grid(row=0, column=0, columnspan=2, pady=10)

        self.label = ttk.Label(self.frame, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.minutes_var = tk.StringVar()
        self.minutes_entry = ttk.Entry(self.frame, textvariable=self.minutes_var, font=("Helvetica", 14), width=5)
        self.minutes_entry.grid(row=1, column=0, padx=5)

        self.start_button = ttk.Button(self.frame, text="شروع", command=self.start_timer)
        self.start_button.grid(row=1, column=1, padx=5)

        self.stop_button = ttk.Button(self.frame, text="توقف", command=self.stop_timer)
        self.stop_button.grid(row=1, column=2, padx=5)

        self.is_running = False
        self.end_time = 0

    def start_timer(self):
        if not self.is_running:
            try:
                minutes = int(self.minutes_var.get())
            except ValueError:
                messagebox.showerror("خطا", "لطفاً یک عدد صحیح وارد کنید.")
                return

            self.is_running = True
            self.end_time = time.time() + (minutes * 60)
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            remaining_time = max(0, round(self.end_time - time.time()))
            minutes, seconds = divmod(remaining_time, 60)
            time_string = f"{minutes:02d}:{seconds:02d}"
            self.time_var.set(time_string)
            if remaining_time > 0:
                self.master.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.time_var.set("انجام شد")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # استفاده از ThemedTk برای اعمال تم
    app = TimerApp(root)
    root.mainloop()

