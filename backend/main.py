# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

class SummarizeRequest(BaseModel):
    text: str
    model: str = "llama2"

app = FastAPI()
OLLAMA_URL = os.getenv("OLLAMA_API", "http://localhost:11434/api/generate")

@app.post("/summarize")
def summarize(req: SummarizeRequest):
    payload = {
        "model": req.model,
        "prompt": f"Summarize this:\n\n{req.text}",
        "stream": False
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        # Ollama final text is often in data["response"]; fallback to str(data)
        summary = data.get("response") or data.get("choices", [{}])[0].get("message", {}).get("content") or str(data)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Ollama: {e}")
