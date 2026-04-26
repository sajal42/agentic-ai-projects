from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai
from pypdf import PdfReader
import tempfile

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#model = genai.GenerativeModel("gemini-2.0-flash")
model = genai.GenerativeModel("gemini-2.5-flash-lite")

app = FastAPI(title="Resume Analyzer API")


# -------------------------
# Extract PDF text
# -------------------------
def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# -------------------------
# Analyze Resume
# -------------------------
def analyze_resume(text):

    prompt = f"""
You are an expert resume reviewer.

Analyze the resume and provide:

1. Score (0-100)
2. Key Skills
3. Strengths
4. Weaknesses
5. Suggestions
6. Suitable Roles

Resume:
{text}
"""

    response = model.generate_content(prompt)
    return response.text


# -------------------------
# API Endpoint
# -------------------------
@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = extract_text(tmp_path)
    result = analyze_resume(text)

    return {"analysis": result}