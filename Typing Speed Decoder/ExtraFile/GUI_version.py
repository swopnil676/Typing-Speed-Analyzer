import tkinter as tk
from tkinter import font as tkfont
import random, time

BG="#0f1117"; PANEL="#171a23"; ACCENT="#7c5cff"; ACCENT_2="#00e0a8"
TEXT_MAIN="#e6e6f0"; TEXT_DIM="#8a8fa3"; CORRECT="#00e0a8"; WRONG="#ff5c7a"

PARAGRAPHS=[
    "The quick brown fox jumps over the lazy dog while the sun sets slowly behind the mountains.",
    "Practice makes a person better every single day, one small step after another toward mastery.",
    "Technology keeps changing how people work, learn, communicate, and connect across the whole world.",
    "A calm mind and steady hands are the real secrets behind fast and accurate typing skills.",
    "Success is not an accident, it is built through consistent effort, patience, and daily discipline.",
    "Reading widely and typing regularly both help sharpen the brain and improve overall focus.",
    "Every expert was once a beginner who simply refused to give up after early mistakes.",
    "Good habits are hard to build but easy to live with once they finally take hold.",
]

class TypingSpeedTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test"); self.geometry("880x520"); self.configure(bg=BG); self.resizable(False, False)
        self.font_main=tkfont.Font(family="Consolas", size=16)
        self.font_ui=tkfont.Font(family="Segoe UI", size=11)
        self.font_big=tkfont.Font(family="Segoe UI", size=28, weight="bold")
        self.target_text=""; self.start_time=None; self.finished=False
        self._build_ui(); self.new_test()

    def _build_ui(self):
        header=tk.Frame(self, bg=BG); header.pack(fill="x", padx=30, pady=(24,10))
        tk.Label(header, text="⌨️  Typing Speed Test", font=self.font_big, bg=BG, fg=TEXT_MAIN).pack(side="left")
        self.stats_var=tk.StringVar(value="WPM: 0    Accuracy: 100%")
        tk.Label(header, textvariable=self.stats_var, font=self.font_ui, bg=BG, fg=ACCENT_2).pack(side="right")

        panel=tk.Frame(self, bg=PANEL, highlightbackground=ACCENT, highlightthickness=1)
        panel.pack(fill="both", padx=30, pady=10)
        self.display=tk.Text(panel, wrap="word", height=6, font=self.font_main, bg=PANEL, fg=TEXT_DIM, bd=0,
                              highlightthickness=0, insertbackground=TEXT_MAIN, padx=20, pady=20, state="disabled", cursor="arrow")
        self.display.pack(fill="both", expand=True)
        self.display.tag_configure("correct", foreground=CORRECT)
        self.display.tag_configure("wrong", foreground=WRONG, background="#3a1420")
        self.display.tag_configure("pending", foreground=TEXT_DIM)

        input_frame=tk.Frame(self, bg=BG); input_frame.pack(fill="x", padx=30, pady=20)
        self.entry_var=tk.StringVar()
        self.entry=tk.Entry(input_frame, textvariable=self.entry_var, font=self.font_main, bg="#1e2130", fg=TEXT_MAIN,
                             insertbackground=TEXT_MAIN, relief="flat")
        self.entry.pack(fill="x", ipady=10)
        self.entry.bind("<KeyRelease>", self.on_key)

        btn_frame=tk.Frame(self, bg=BG); btn_frame.pack(fill="x", padx=30)
        self.result_var=tk.StringVar(value="")
        tk.Label(btn_frame, textvariable=self.result_var, font=self.font_ui, bg=BG, fg=ACCENT).pack(side="left")
        tk.Button(btn_frame, text="⟳  New Test", font=self.font_ui, bg=ACCENT, fg="#ffffff", bd=0, padx=16, pady=8,
                  activebackground=ACCENT_2, cursor="hand2", command=self.new_test).pack(side="right")

        tk.Label(self, text="Made by Shahzaib Malik", font=("Segoe UI", 9), bg=BG, fg=TEXT_DIM).pack(side="bottom", pady=10)

    def new_test(self):
        self.target_text=random.choice(PARAGRAPHS); self.start_time=None; self.finished=False
        self.entry_var.set(""); self.result_var.set(""); self.stats_var.set("WPM: 0    Accuracy: 100%")
        self.display.config(state="normal"); self.display.delete("1.0", "end"); self.display.insert("1.0", self.target_text)
        self.display.tag_add("pending", "1.0", "end"); self.display.config(state="disabled")
        self.entry.config(state="normal", bg="#1e2130"); self.entry.focus_set()

    def on_key(self, event):
        if self.finished: return
        typed=self.entry_var.get()
        if self.start_time is None and typed: self.start_time=time.time()

        self.display.config(state="normal")
        self.display.tag_remove("correct", "1.0", "end")
        self.display.tag_remove("wrong", "1.0", "end")
        self.display.tag_remove("pending", "1.0", "end")

        correct_count=0
        for i, ch in enumerate(self.target_text):
            s, e = f"1.{i}", f"1.{i+1}"
            if i < len(typed):
                if typed[i] == ch:
                    self.display.tag_add("correct", s, e); correct_count += 1
                else:
                    self.display.tag_add("wrong", s, e)
            else:
                self.display.tag_add("pending", s, e)
        self.display.config(state="disabled")

        accuracy = int((correct_count/len(typed))*100) if typed else 100
        elapsed = max(time.time()-self.start_time, 0.001) if self.start_time else 0.001
        wpm = int((len(typed.split())/elapsed)*60) if elapsed > 0 else 0
        self.stats_var.set(f"WPM: {wpm}    Accuracy: {accuracy}%")

        if len(typed) >= len(self.target_text):
            self.finish_test(wpm, accuracy)

    def finish_test(self, wpm, accuracy):
        self.finished=True
        elapsed=round(time.time()-self.start_time, 2)
        self.entry.config(state="disabled", bg="#182018")
        self.result_var.set(f"Done! {wpm} WPM  •  {accuracy}% accuracy  •  {elapsed}s")

if __name__ == "__main__":
    app=TypingSpeedTest()
    app.mainloop()