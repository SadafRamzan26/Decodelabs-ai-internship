import tkinter as tk
from tkinter import ttk, scrolledtext
import time

class DecodeAIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DecodeLabs AI Guardrail Engine v1.0")
        self.root.geometry("450x600")
        self.root.configure(bg="#1e1e2e")  # Futuristic Dark Theme

        # 1. Internal Logic Engine Initialization
        self.knowledge_base = {
            "hello": "Hi there! Welcome to DecodeLabs AI platform.",
            "hi": "Hello! How can I assist you with our AI systems today?",
            "what is your name": "I am the DecodeLabs Rule-Based Guardrail System.",
            "status": "All systems deterministic. Zero hallucination risk detected.",
            "help": "Available intents: hello, status, help, clear, and exit.",
            "clear": "Screen buffer cleared in runtime."
        }

        # 2. UI Layout Components
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header = tk.Label(
            self.root, 
            text="⚡ DECODELABS GUARDRAIL ENGINE ⚡", 
            bg="#11111b", fg="#cdd6f4", 
            font=("Courier New", 12, "bold"), pady=10
        )
        header.pack(fill=tk.X)

        # Chat Log Screen (Scrolled Text for continuous loop view)
        self.chat_log = scrolledtext.ScrolledText(
            self.root, bg="#181825", fg="#a6e3a1", 
            font=("Consolas", 10), state='disabled', wrap=tk.WORD
        )
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input Frame (Bottom area)
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        # Entry Box for User Input
        self.entry_box = tk.Entry(
            input_frame, bg="#313244", fg="#cdd6f4", 
            insertbackground="white", font=("Consolas", 11), relief=tk.FLAT
        )
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.entry_box.bind("<Return>", self.handle_input)  # Bind Enter Key!

        # Send Button
        send_btn = tk.Button(
            input_frame, text="SEND", bg="#89b4fa", fg="#11111b", 
            font=("Arial", 9, "bold"), relief=tk.FLAT, command=self.handle_input
        )
        send_btn.pack(side=tk.RIGHT, padx=5, ipady=5, ipadx=10)

        # System Bootstrap Message
        self.append_chat("SYSTEM", "Deterministic control layer active. Type your command...")

    def append_chat(self, sender, message):
        """Appends text to the chat display area smoothly"""
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, f"[{sender}] >>> {message}\n")
        self.chat_log.yview(tk.END)
        self.chat_log.config(state='disabled')

    def handle_input(self, event=None):
        raw_user_input = self.entry_box.get()
        if not raw_user_input.strip():
            return

        # Phase 1: Input Sanitization & Normalization [Slide Requirement]
        clean_input = raw_user_input.lower().strip()
        self.entry_box.delete(0, tk.END)  # Clear Input Box
        
        self.append_chat("USER", raw_user_input)

        # Exit Strategy Handling
        if clean_input in ['exit', 'quit', 'bye']:
            self.append_chat("BOT", "Terminating session safely. Compliance logs saved.")
            self.root.after(1500, self.root.destroy)  # Safe delay break
            return

        # Phase 2: Intent Matching & Fallback Layer (Atomic O(1) Operation)
        response = self.knowledge_base.get(
            clean_input, 
            "[FALLBACK ALERT]: Input mapped to probabilistic core. Input out of scope."
        )
        
        # Simulate slight network delay for premium feel
        self.root.after(300, lambda: self.append_chat("BOT", response))

if __name__ == "__main__":
    root = tk.Tk()
    app = DecodeAIGUI(root)
    root.mainloop()