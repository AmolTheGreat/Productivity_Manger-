import tkinter as tk
from tkinter import messagebox
import pygetwindow as gw
import pyautogui
import threading
import time
import os

# --- THE HITLISTS & INSPECTOR LOGIC ---
HARD_BLOCK = ["youtube", "tiktok", "instagram", "roblox", "discord", "netflix", "facebook"]
BAD_CODE_WORDS = ["game", "play", "arcade", "video", "stream", "fun", "social", "tv"]
WORK_CODE_WORDS = ["python", "vscode", "scratch", "math", "homework", "docs", "lesson", "editor"]

class GuardianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AMOL GIRI: GUARDIAN AI")
        self.root.geometry("450x550")
        self.root.configure(bg="#020617")
        self.root.attributes("-topmost", True)
        
        self.chances = 3 
        self.is_running = False 
        self.seconds_left = 0

        # UI Header
        self.status_label = tk.Label(root, text="SYSTEM: STANDBY", font=("Courier", 22, "bold"), fg="#38bdf8", bg="#020617")
        self.status_label.pack(pady=20)
        
        self.chance_label = tk.Label(root, text=f"EXIT CHANCES: {self.chances}", font=("Helvetica", 14, "bold"), fg="#eab308", bg="#020617")
        self.chance_label.pack()

        # Triple Input System
        input_frame = tk.Frame(root, bg="#020617")
        input_frame.pack(pady=40)

        entry_style = {"font": ("Consolas", 35), "width": 3, "bg": "#1e293b", "fg": "white", "border": 0, "justify": "center", "insertbackground": "white"}
        
        self.h_entry = tk.Entry(input_frame, **entry_style); self.h_entry.insert(0, "00")
        self.m_entry = tk.Entry(input_frame, **entry_style); self.m_entry.insert(0, "25")
        self.s_entry = tk.Entry(input_frame, **entry_style); self.s_entry.insert(0, "00")

        self.h_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text=":", font=("Consolas", 25), fg="#38bdf8", bg="#020617").pack(side=tk.LEFT)
        self.m_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text=":", font=("Consolas", 25), fg="#38bdf8", bg="#020617").pack(side=tk.LEFT)
        self.s_entry.pack(side=tk.LEFT, padx=5)

        # Bind Arrows & Enter
        for e in (self.h_entry, self.m_entry, self.s_entry):
            e.bind("<Up>", lambda event, target=e: self.adj(target, 1))
            e.bind("<Down>", lambda event, target=e: self.adj(target, -1))
            e.bind("<Return>", lambda event: self.parse_and_start())

        self.timer_display = tk.Label(root, text="00:00:00", font=("Consolas", 50), fg="#94a3b8", bg="#020617")
        self.timer_display.pack(pady=10)

        self.start_btn = tk.Button(root, text="ENGAGE LOCKDOWN", command=self.parse_and_start, font=("Helvetica", 12, "bold"), bg="#22c55e", fg="white", width=20)
        self.start_btn.pack(pady=10)

        self.exit_btn = tk.Button(root, text="USE EXIT CHANCE", command=self.use_panic, font=("Helvetica", 12, "bold"), bg="#b91c1c", fg="white", width=25, state="disabled")
        self.exit_btn.pack(pady=10)

        tk.Label(root, text="BY AMOL", font=("Courier", 14, "bold"), fg="#38bdf8", bg="#020617").pack(side=tk.BOTTOM, pady=20)

    def adj(self, target, delta):
        try:
            val = int(target.get()) + delta
            if val < 0: val = 59
            elif val > 59 and target != self.h_entry: val = 0
            target.delete(0, tk.END); target.insert(0, f"{val:02d}")
        except: pass

    def inspect_and_snipe(self, window):
        try:
            title = str(window.title).lower()
            if "amol giri" in title or "guardian" in title: return
            
            is_bad = any(word in title for word in HARD_BLOCK)
            score = sum(1 for word in BAD_CODE_WORDS if word in title)
            score -= sum(2 for word in WORK_CODE_WORDS if word in title)
            
            if is_bad or score > 0:
                if "roblox" in title:
                    os.system("taskkill /F /IM RobloxPlayerBeta.exe /T")
                window.activate()
                time.sleep(0.05)
                pyautogui.hotkey('ctrl', 'w')
        except: pass

    def deep_sweep(self):
        for win in gw.getAllWindows():
            if win.title: self.inspect_and_snipe(win)

    def parse_and_start(self):
        try:
            h, m, s = int(self.h_entry.get()), int(self.m_entry.get()), int(self.s_entry.get())
            total = h * 3600 + m * 60 + s
            if total > 0:
                self.is_running = True
                self.deep_sweep()
                self.seconds_left = float(total)
                self.start_btn.config(state="disabled")
                self.exit_btn.config(state="normal")
                self.status_label.config(text="SYSTEM: REINFORCED", fg="#22c55e")
                self.timer_display.config(fg="#ef4444")
                threading.Thread(target=self.run_logic, daemon=True).start()
        except: pass

    def use_panic(self):
        if self.chances > 0:
            self.is_running = False 
            self.chances -= 1
            self.timer_display.config(text="00:00:00", fg="#94a3b8")
            self.exit_btn.config(state="disabled")
            self.start_btn.config(state="normal")
            self.chance_label.config(text=f"EXIT CHANCES: {self.chances}")
            self.status_label.config(text="SYSTEM: STANDBY", fg="#38bdf8")
        else: messagebox.showerror("LOCKED", "Zero chances!")

    def run_logic(self):
        while self.seconds_left > 0 and self.is_running:
            h, rem = divmod(int(self.seconds_left), 3600)
            m, s = divmod(rem, 60)
            self.timer_display.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            active = gw.getActiveWindow()
            if active: self.inspect_and_snipe(active)
            time.sleep(0.3)
            self.seconds_left -= 0.3
        if self.seconds_left <= 0 and self.is_running:
            self.is_running = False
            self.root.after(0, self.victory)

    def victory(self):
        self.chances += 1
        self.start_btn.config(state="normal")
        self.chance_label.config(text=f"EXIT CHANCES: {self.chances}")
        self.status_label.config(text="SYSTEM: STANDBY", fg="#38bdf8")
        messagebox.showinfo("VICTORY", "Goal Reached! +1 Chance.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuardianApp(root)
    root.mainloop()