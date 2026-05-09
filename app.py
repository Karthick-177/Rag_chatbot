from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

# ── Config ────────────────────────────────────────────────────
GROQ_API_KEY = "your-groq-api-key-here"
client = Groq(api_key=GROQ_API_KEY)

# ── Load Knowledge Base ───────────────────────────────────────
with open("knowledge_base.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

# ── Build FAISS Index ─────────────────────────────────────────
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# ── App Setup ─────────────────────────────────────────────────
app = FastAPI(title="RAG Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG Chatbot API is running!"}

@app.post("/chat")
def chat(input: ChatInput):
    question_embedding = embedder.encode([input.question], convert_to_numpy=True)
    _, indices = index.search(question_embedding, k=3)
    relevant_chunks = [chunks[i] for i in indices[0]]
    context = "\n\n".join(relevant_chunks)
    prompt = f"""You are a helpful AI assistant like Claude. Answer the question as accurately and helpfully as possible.
Use the context below if relevant, otherwise use your own knowledge to answer.

Context:
{context}

Question: {input.question}

Answer:"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"answer": response.choices[0].message.content}
