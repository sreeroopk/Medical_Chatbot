# Medical Chatbot | Generative AI

A domain-specific conversational AI for medical assistance using transformer-based models.  
The chatbot is fine-tuned on curated medical corpora to enhance **domain adaptation** and **contextual accuracy**.

---

## 🚀 Features
- Answers medical queries using **transformer-based NLP models**.
- Fine-tuned pre-trained language models (PLMs) for medical context.
- Context-aware, accurate, and reliable responses.

---

## 🛠️ Tech Stack
- Python
- PyTorch / TensorFlow
- Hugging Face Transformers
- Streamlit (for web demo)

---

## 📦 Installation
Clone this repository:
```bash
git clone https://github.com/<your-username>/medical-chatbot.git
cd medical-chatbot
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the chatbot:
```bash
python app.py
```

Or launch the Streamlit demo:
```bash
streamlit run app.py
```

---

## 📓 Training
A sample training pipeline is available in [`notebooks/training.ipynb`](notebooks/training.ipynb).

---

## 📌 Example
```
User: What are the symptoms of diabetes?
Bot: Common symptoms include increased thirst, frequent urination, extreme hunger, fatigue, and blurred vision.
```

---

## 📜 License
This project is open-source for educational purposes.
