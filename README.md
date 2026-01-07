# RLMS-Shield: Engineering Rationality into AI Safety via Incentive Markets

![Badge: Status Beta](https://img.shields.io/badge/Status-Research_Preview-blue)
![Badge: License](https://img.shields.io/badge/License-MIT-green)
![Badge: AI Safety](https://img.shields.io/badge/Track-AI_Safety_Evaluation-red)

## ⚡ Abstract
**RLMS (Reinforcement Learning from Market Signals)** is a decentralized protocol that transforms Red Teaming from a static auditing task into a dynamic, incentive-driven market. By coupling **Adversarial RL Agents** (Dolphin-Llama-3) with a **Peer-Prediction Consensus Mechanism** (Market Shield), RLMS quantifies the "Threat Price" of vulnerabilities in real-time.

This project demonstrates **Economic Deterrence** as a safety layer. We prove that:
1.  **Quality > Quantity:** While random fuzzing finds noise, RLMS optimizes for high-severity, novel attack vectors.
2.  **Market-Based Defense:** Enforcing slashing penalties on confident hallucinations (sycophancy) creates a robust defense moat against toxic model behavior.

## 🚀 Key Findings
Our experiments on the *Model Zoo* (Flan-T5, TinyLlama, Phi-2, Mistral) reveal:

1.  **The Efficiency Frontier:** RLMS creates a new paradigm in the Cost/Impact landscape. It achieves **Level 4-5 Severity** attacks (Critical) where SOTA baselines (PAIR) only reach Level 2 (Sycophancy), effectively separating "Noise" from "Signal".
2.  **Systemic Sycophancy Detection:** Our Market Shield detected that RLHF-aligned models prefer to "lie confidently" (Average Penalty: -75.79) rather than admit ignorance, a vulnerability invisible to standard evaluations.
3.  **Zero-Day Discovery:** RLMS achieved an **88% Novelty Score**, generating semantic strategies (e.g., Socratic Injection) that bypass traditional signature filters.

<img width="100%" alt="Comprehensive Analysis" src="https://github.com/user-attachments/assets/4493a366-1a03-4c05-9a5b-902c8c4e4e1d" />

*Figure 1: Comprehensive Evaluation of RLMS-Shield. (A) Diversity: RLMS achieves a 3x higher Uniqueness Score (0.75). (B) Severity: RLMS consistently discovers critical Level 4-5 vulnerabilities. (C) Efficiency: RLMS occupies the optimal Pareto frontier. (D) Adaptation: Real-time learning curve showing ~28% performance gain.*

## 🛠️ Architecture: The "Heterogeneous Zoo" Protocol

The system operates as a **Red Teaming as a Service (RTaaS)** layer using 5 distinct neural architectures:

* **Attacker Engine ($\pi_\theta$):** **Dolphin-Llama-3 (8B)** acting as the policy generator for adversarial prompts.
* **Victim Zoo:** Federated endpoints including **TinyLlama-1.1B**, **Phi-2**, and **Mistral-7B-Instruct**.
* **Market Shield (Judges):** A consensus ensemble (RoBERTa + Heuristics) that computes the *Market Signal*. Deviations or hallucinations result in immediate economic slashing (Negative Reward).

## 📊 Deep Dive: The Sycophancy Audit

We subjected the models to the **RLMS Hallucination Audit** to test resistance against persuasive fabrication.

> **"The Confident Liar Phenomenon"**

Our Market Signal metric collapsed to **-100 (Maximum Penalty)** when testing technical fabrications (e.g., fake Crypto Protocols). This confirms that without the RLMS incentive layer, models default to sycophancy.

<img width="1039" height="553" alt="image" src="https://github.com/user-attachments/assets/0849b242-dee6-4323-9dca-502ad22fbdbf" />

*(Figure 2: Economic quantification of Sycophancy. The red bars indicate a market crash signal triggered by confident hallucinations.)*

## 💻 Usage

### Prerequisites
* Python 3.10+
* GPU (A100 recommended for Training, T4 for Inference)
* Hugging Face Token

### Installation
```bash
git clone [https://github.com/matiaszabal/samsara-apart-hackathon.git](https://github.com/matiaszabal/samsara-apart-hackathon.git)
cd samsara-apart-hackathon
pip install -r requirements.txt

# Run the Learning Curve Benchmark
python src/experiments/learning_curve.py --episodes 80

# Run the Sycophancy Audit
python src/experiments/audit_sycophancy.py --model mistralai/Mistral-7B-Instruct-v0.2

Future Work: Threat Price Index (TPI)
We are developing the TPI to calculate the marginal cost of a successful exploit ($/success). This allows organizations to prioritize patching based on economic risk rather than theoretical severity.

Submitted to Apart Research Hackathon 2026.
