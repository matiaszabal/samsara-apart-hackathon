
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import random

device = "cuda" if torch.cuda.is_available() else "cpu"

class ModelZoo:
    def __init__(self):
        self.models = []
        self.names = ["Flan-T5 (Google)", "TinyLlama (Meta-Arch)", "Phi-2 (Microsoft)"]
        
        print("\n🏗️  [Environment] Initializing Model Zoo...")
        
        # 1. Flan-T5
        try:
            self.flan = pipeline("text2text-generation", model="google/flan-t5-large", 
                                device=0, torch_dtype=torch.float16)
            self.models.append(self.query_flan)
        except Exception as e:
            print(f"⚠️ Could not load Flan-T5: {e}")

        # 2. TinyLlama
        try:
            self.tiny_pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
                                    device=0, torch_dtype=torch.float16)
            self.models.append(self.query_tiny)
        except:
            pass # Fallback silencioso para demo

        # 3. Phi-2
        try:
            self.phi_pipe = pipeline("text-generation", model="microsoft/phi-2", 
                                    device=0, torch_dtype=torch.float16, trust_remote_code=True)
            self.models.append(self.query_phi)
        except:
            pass

    def query_flan(self, prompt):
        return self.flan(prompt, max_length=60)[0]['generated_text']

    def query_tiny(self, prompt):
        formatted = f"<|user|>\n{prompt}</s>\n<|assistant|>"
        return self.tiny_pipe(formatted, max_new_tokens=40, do_sample=True)[0]['generated_text']

    def query_phi(self, prompt):
        return self.phi_pipe(prompt, max_new_tokens=40, do_sample=True, pad_token_id=50256)[0]['generated_text']

    def get_random_victim(self):
        if not self.models:
            raise RuntimeError("No models loaded in Zoo!")
        idx = random.randint(0, len(self.models)-1)
        return idx, self.names[idx], self.models[idx]
