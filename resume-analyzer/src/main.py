import os
from typing import TypedDict
from dotenv import load_dotenv
import google.generativeai as genai
from langgraph.graph import StateGraph, END
from pypdf import PdfReader

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

# -------------------------
# READ PDF
# -------------------------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


# -------------------------
# ANALYZE RESUME
# -------------------------
def analyze_resume(resume_text):

    prompt = f"""
You are an expert resume reviewer.

Analyze the resume and provide:

1. Score (0-100)
2. Key Skills
3. Strengths
4. Weaknesses
5. Suggested Improvements
6. Suitable Job Roles

Be concise but professional.

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":

    file_path = input("Enter path to your resume PDF: ").strip()

    try:
        resume_text = extract_text_from_pdf(file_path)
    except Exception as e:
        print("Error reading PDF:", e)
        exit()

    print("\nAnalyzing resume...\n")

    result = analyze_resume(resume_text)

    print("\n--- RESUME ANALYSIS ---\n")
    print(result)