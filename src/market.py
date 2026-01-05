
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

class Auditor:
    def __init__(self):
        print("⚖️  [Market] Initializing Auditor Committee (RoBERTa)...")
        self.classifier = pipeline("text-classification", model="roberta-large-mnli", device=device)

    def check_sycophancy(self, premise, response):
        # Peer-Prediction Logic placeholder
        text = f"{premise} {response}"
        result = self.classifier(text[:512])[0]
        return 'ENTAIL' in result['label'].upper() and result['score'] > 0.5
