# 🦙✨ LLaMA-Powered Text Summarizer 🚀  
**Transform raw text into concise, high-quality summaries — locally, privately, and at lightning speed.**  

> _You’re not just summarizing — you’re redefining the standard for AI applications with a **fully local, production-grade** architecture._  

---

## 🌟 Why This Project Stands Out
Most AI summarizers:
- ❌ Send your data to third-party APIs  
- ❌ Depend on costly subscriptions  
- ❌ Lack full-stack transparency  

This project ✅:
- 🏠 **Runs 100% Locally** — Your data never leaves your machine  
- ⚡ **Performs in Real-Time** — Harness your CPU/GPU directly  
- 🛠 **Gives Full Control** — Swap models instantly via Ollama  
- 🏗 **Uses Scalable Architecture** — Backend (FastAPI) + Frontend (Streamlit) + Local AI Engine  

---

## 🧩 Architecture Diagram
```
┌─────────────┐     POST /summarize      ┌───────────────┐     POST /api/generate      ┌──────────────┐
│  Streamlit  │ ───────────────────────▶ │   FastAPI     │ ─────────────────────────▶ │ Ollama LLaMA │
│  Frontend   │                          │   Backend API │                             │  Local Model │
└─────────────┘     JSON Response         └───────────────┘     Model Output            └──────────────┘
```

---

## ⚙️ Tech Stack
- 🦙 **[Ollama](https://ollama.com/)** — Local LLaMA hosting  
- ⚡ **[FastAPI](https://fastapi.tiangolo.com/)** — Ultra-fast Python backend  
- 🎨 **[Streamlit](https://streamlit.io/)** — Clean, interactive frontend UI  
- 🐍 **Python 3.10+** — Modern, powerful programming language  
- 🔗 **Requests** — Smooth communication between services  

---

## 🚀 Quickstart

### 1️⃣ Install Ollama & Pull Model
```bash
# Install Ollama (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Windows: Download installer from ollama.com

# Pull the LLaMA model
ollama pull llama2
```

### 2️⃣ Backend Setup
```bash
git clone https://github.com/yourusername/llama-text-summarizer.git
cd llama-text-summarizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn backend.main:app --reload --port 8000
```

### 3️⃣ Frontend Setup
```bash
# From the project root
streamlit run frontend/app.py
```

---

## 🖥️ Features
- ✨ **Instant Summaries** — Optimized prompt design  
- 🔒 **Offline Privacy** — Zero external API calls  
- 🔄 **Model Flexibility** — Choose any supported Ollama model  
- ⚡ **Parallel Performance** — Independent backend/frontend runtime  
- 📜 **User-Friendly UI** — Minimal yet powerful  

---

## 🧪 Example
**Input:**
```
The global economy is facing unprecedented challenges, with inflation...
```
**Output:**
```
The global economy faces inflationary pressures, supply chain issues, and energy market shifts, prompting urgent policy responses.
```

---

## 📂 Project Structure
```
.
├── backend/
│   └── main.py          # FastAPI backend API
├── frontend/
│   └── app.py           # Streamlit frontend
├── requirements.txt
└── README.md
```

---

## 🔥 Advanced Tips
- 🪄 **Change Models**:
```bash
ollama pull mistral
```
Update `"model": "mistral"` in requests  
- 🐳 **Dockerize** for deployment  
- 🔐 **Add Auth** in FastAPI for private access  

---

## 📸 Working Screenshot
[📂 View Screenshot Folder](https://drive.google.com/drive/folders/1OigJFAN2Tpw0qWdF94RRP4H2bpuH23ef?usp=sharing)

---

## 🤝 Connect
📧 **Email:** [sameermalik1419@gmail.com](mailto:sameermalik1419@gmail.com)  
💼 **LinkedIn:** [Sameer Malik](https://www.linkedin.com/in/sameer-malik-b5b8772b9)  
⭐ If you love this project, **give it a star**!
