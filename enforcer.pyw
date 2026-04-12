import customtkinter as ctk  # The "Websitey" UI library
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

# Setup the look and feel
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GuardianApp(ctk.CTk): # Switched to ctk.CTk for the window
    def __init__(self):
        super().__init__()
        
        self.title("AMOL GIRI: GUARDIAN AI")
        self.geometry("450x600")
        self.attributes("-topmost", True)
        
        self.chances = 3 
        self.is_running = False 
        self.seconds_left = 0

        # --- UI ELEMENTS (The Websitey Look) ---
        
        # Header Status
        self.status_label = ctk.CTkLabel(self, text="SYSTEM: STANDBY", font=ctk.CTkFont(family="Courier", size=24, weight="bold"), text_color="#38bdf8")
        self.status_label.pack(pady=(30, 10))
        
        self.chance_label = ctk.CTkLabel(self, text=f"EXIT CHANCES: {self.chances}", font=ctk.CTkFont(size=14, weight="bold"), text_color="#eab308")
        self.chance_label.pack()

        # Input Container
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=30)

        entry_style = {"width": 70, "height": 70, "font": ("Consolas", 35), "justify": "center", "corner_radius": 10}
        
        self.h_entry = ctk.CTkEntry(self.input_frame, **entry_style); self.h_entry.insert(0, "00")
        self.m_entry = ctk.CTkEntry(self.input_frame, **entry_style); self.m_entry.insert(0, "25")
        self.s_entry = ctk.CTkEntry(self.input_frame, **entry_style); self.s_entry.insert(0, "00")

        self.h_entry.pack(side="left", padx=5)
        ctk.CTkLabel(self.input_frame, text=":", font=("Consolas", 30), text_color="#38bdf8").pack(side="left")
        self.m_entry.pack(side="left", padx=5)
        ctk.CTkLabel(self.input_frame, text=":", font=("Consolas", 30), text_color="#38bdf8").pack(side="left")
        self.s_entry.pack(side="left", padx=5)

        # Big Timer Display
        self.timer_display = ctk.CTkLabel(self, text="00:00:00", font=("Consolas", 60), text_color="#94a3b8")
        self.timer_display.pack(pady=20)

        # High-Tech Buttons
        self.start_btn = ctk.CTkButton(self, text="ENGAGE LOCKDOWN", command=self.parse_and_start, font=ctk.CTkFont(size=14, weight="bold"), fg_color="#22c55e", hover_color="#16a34a", height=45, corner_radius=20)
        self.start_btn.pack(pady=10, padx=40, fill="x")

        self.exit_btn = ctk.CTkButton(self, text="USE EXIT CHANCE", command=self.use_panic, font=ctk.CTkFont(size=14, weight="bold"), fg_color="#b91c1c", hover_color="#991b1b", height=45, corner_radius=20, state="disabled")
        self.exit_btn.pack(pady=10, padx=40, fill="x")

        # Footer
        self.footer = ctk.CTkLabel(self, text="BY AMOL GIRI", font=ctk.CTkFont(family="Courier", size=16, weight="bold"), text_color="#38bdf8")
        self.footer.pack(side="bottom", pady=20)

    # --- YOUR LOGIC (UNCHANGED) ---
    def inspect_and_snipe(self, window):
        try:
            title = str(window.title).lower()
            if "amol giri" in title or "guardian" in title: return
            is_bad = any(word in title for word in HARD_BLOCK)
            score = sum(1 for word in BAD_CODE_WORDS if word in title)
            score -= sum(2 for word in WORK_CODE_WORDS if word in title)
            if is_bad or score > 0:
                if "roblox" in title: os.system("taskkill /F /IM RobloxPlayerBeta.exe /T")
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
                self.start_btn.configure(state="disabled")
                self.exit_btn.configure(state="normal")
                self.status_label.configure(text="SYSTEM: REINFORCED", text_color="#22c55e")
                self.timer_display.configure(text_color="#ef4444")
                threading.Thread(target=self.run_logic, daemon=True).start()
        except: pass

    def use_panic(self):
        if self.chances > 0:
            self.is_running = False 
            self.chances -= 1
            self.timer_display.configure(text="00:00:00", text_color="#94a3b8")
            self.exit_btn.configure(state="disabled")
            self.start_btn.configure(state="normal")
            self.chance_label.configure(text=f"EXIT CHANCES: {self.chances}")
            self.status_label.configure(text="SYSTEM: STANDBY", text_color="#38bdf8")
        else: messagebox.showerror("LOCKED", "Zero chances!")

    def run_logic(self):
        while self.seconds_left > 0 and self.is_running:
            h, rem = divmod(int(self.seconds_left), 3600)
            m, s = divmod(rem, 60)
            self.timer_display.configure(text=f"{h:02d}:{m:02d}:{s:02d}")
            active = gw.getActiveWindow()
            if active: self.inspect_and_snipe(active)
            time.sleep(0.3)
            self.seconds_left -= 0.3
        if self.seconds_left <= 0 and self.is_running:
            self.is_running = False
            self.after(0, self.victory)

    def victory(self):
        self.chances += 1
        self.start_btn.configure(state="normal")
        self.chance_label.configure(text=f"EXIT CHANCES: {self.chances}")
        self.status_label.configure(text="SYSTEM: STANDBY", text_color="#38bdf8")
        messagebox.showinfo("VICTORY", "Goal Reached! +1 Chance.")

if __name__ == "__main__":
    app = GuardianApp()
    app.mainloop()