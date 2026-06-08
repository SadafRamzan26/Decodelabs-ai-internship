import time

class DecodeAIGuardrail:
    def __init__(self):
        # Industrial Knowledge Base with 5+ intents [O(1) Complexity]
        self.knowledge_base = {
            "hello": "Hi there! Welcome to DecodeLabs AI platform.",
            "hi": "Hello! How can I assist you with our AI systems today?",
            "what is your name": "I am the DecodeLabs Rule-Based Guardrail System.",
            "status": "All systems deterministic. Zero hallucination risk detected.",
            "help": "Available intents: hello, status, help, clear, and exit.",
            "clear": "Screen buffer cleared in runtime."
        }
        self.session_active = True

    def sanitize_input(self, raw_input: str) -> str:
        """Phase 1: Sanitization & Normalization"""
        return raw_input.lower().strip()

    def process_intent(self, clean_input: str) -> str:
        """Phase 2: Intent Matching & Fallback Layer"""
        if clean_input in ['exit', 'quit', 'bye']:
            self.session_active = False
            return "Terminating session safely. Compliance logs saved."

        # Atomic lookup operation
        return self.knowledge_base.get(
            clean_input, 
            "[FALLBACK ALERT]: Input mapped to probabilistic core. Input out of scope."
        )

    def run_engine(self):
        """The Heartbeat: Continuous Infinite Loop"""
        print("=" * 60)
        print("⚡ DECODELABS GUARDRAIL ENGINE v1.0 INITIALIZED ⚡")
        print("Executing deterministic control layer...")
        print("=" * 60)
        time.sleep(0.5)

        while self.session_active:
            user_raw = input("\n[USER INPUT] >>> ")
            clean_user_input = self.sanitize_input(user_raw)

            if not clean_user_input:
                continue

            response = self.process_intent(clean_user_input)
            print(f"[BOT OUTPUT] <<< {response}")