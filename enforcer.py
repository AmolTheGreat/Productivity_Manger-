import psutil
import time
import tkinter as tk
from tkinter import messagebox
import threading

# ID: SYSTEM-ENFORCER-001 | AUTHORIZED BY AMOL GIRI
class AmolGiriEnforcer:
    def __init__(self, root):
        self.root = root
        self.root.title("Amol Giri | System Enforcer")
        self.root.geometry("400x400")
        self.root.configure(bg="#050505")
        
        self.is_active = False
        
        # This is the "Kill List" for non-productive apps
        self.blacklist = ["roblox", "discord", "youtube", "tiktok", "netflix", "spotify", "fortnite"]
        
        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="AI SYSTEM ENFORCER", font=("Impact", 24), fg="#00ff88", bg="#050505").pack(pady=20)
        
        label_text = "Once initiated, the AI logic will monitor all laptop processes.\nNon-productive signatures will be forced to close."
        tk.Label(self.root, text=label_text, fg="#888", bg="#050505", font=("Arial", 9)).pack(pady=10)

        # Start Button
        self.start_btn = tk.Button(self.root, text="INITIATE LOCKDOWN", command=self.ask_permission, 
                                   bg="#00ff88", fg="black", font=("Arial", 12, "bold"), width=20)
        self.start_btn.pack(pady=30)

        # Footer
        tk.Label(self.root, text="ID: AMOL-GIRI-001", fg="#444", bg="#050505").pack(side="bottom", pady=10)

    def ask_permission(self):
        # The "Ton of Permissions" sequence
        perms = [
            "Grant Amol Giri AI permission to take control of laptop processes?",
            "Authorize the system to FORCE CLOSE non-productive apps?",
            "Final Step: This will lock your focus. Are you ready?"
        ]
        for p in perms:
            if not messagebox.askyesno("PERMISSION REQUEST", p):
                return

        self.is_active = True
        self.start_btn.config(state="disabled", text="ENFORCING...")
        threading.Thread(target=self.kill_logic, daemon=True).start()

    def kill_logic(self):
        """The AI loop that scans and kills non-productive apps"""
        while self.is_active:
            # Look at every app running on the laptop
            for proc in psutil.process_iter(['name']):
                try:
                    p_name = proc.info['name'].lower()
                    # If any name on our blacklist is found, kill it
                    for item in self.blacklist:
                        if item in p_name:
                            proc.kill() # This is the "Hard Block"
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            time.sleep(1) # Scan every 1 second

if __name__ == "__main__":
    root = tk.Tk()
    app = AmolGiriEnforcer(root)
    root.mainloop()