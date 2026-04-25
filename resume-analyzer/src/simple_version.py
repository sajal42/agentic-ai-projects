import os
from typing import TypedDict
from dotenv import load_dotenv
import google.generativeai as genai
from langgraph.graph import StateGraph, END

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

def analyze_resume(resume_text):

    prompt = f"""
You are an expert resume reviewer and career coach.

Analyze the following resume and provide:

1. Key Skills
2. Strengths
3. Weaknesses
4. Suggested Improvements
5. Suitable Job Roles

Resume:
{resume_text}

Return structured output with clear headings.
"""

    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":

    print("Paste your resume text (type END to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    resume_text = "\n".join(lines)

    result = analyze_resume(resume_text)

    print("\n--- ANALYSIS ---\n")
    print(result)