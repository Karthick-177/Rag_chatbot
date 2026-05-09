# 🤖 RAG Chatbot — Claude Knowledge Bot

A conversational AI chatbot built using **Retrieval Augmented Generation (RAG)** that answers questions using a custom knowledge base powered by FAISS vector search and Groq LLaMA.

---

## 🚀 Live Demo
> Run locally — see setup instructions below

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Groq LLaMA 3.3 70B |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Store | FAISS |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |

---

## 📌 Features

- 🔍 Semantic search using FAISS vector index
- 🧠 Answers from custom knowledge base + general LLM knowledge
- ⚡ Fast responses via Groq API
- 💬 Clean dark-themed chat UI with typing indicator
- 📡 REST API with auto Swagger docs

---

## 🏗️ Architecture

```
User Question
     ↓
Sentence Transformer (embed question)
     ↓
FAISS Vector Search (find top 3 relevant chunks)
     ↓
Groq LLaMA (generate answer using context)
     ↓
Response to User
```

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Karthick-177/Rag_chatbot.git
cd Rag_chatbot
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn sentence-transformers faiss-cpu groq
```

### 3. Add your Groq API key
Open `app.py` and replace:
```python
GROQ_API_KEY = "your-groq-api-key-here"
```

### 4. Start the API
```bash
python -m uvicorn app:app --reload
```

### 5. Start the frontend
```bash
python -m http.server 3000
```

### 6. Open browser
```
http://localhost:3000
```

---

## 📁 Project Structure

```
Rag_chatbot/
├── app.py               # FastAPI backend
├── knowledge_base.txt   # Custom knowledge source
└── index.html           # Chat UI frontend
```

---

## 🔮 Future Improvements
- Add PDF upload support
- Deploy on Hugging Face Spaces
- Add conversation memory
- Support multiple knowledge bases

---

## 👨‍💻 Author
**Karthick** — AI Engineer (Fresher)
- GitHub: [Karthick-177](https://github.com/Karthick-177)
