This project is an AI-powered Resume Analyzer that evaluates resumes and provides structured, professional feedback using a Large Language Model (Gemini).

It simulates how modern AI systems assist recruiters and job seekers by analyzing resumes for strengths, weaknesses, and role fit.


Features:
1. Accepts PDF resumes
2. AI-based analysis using Gemini API
3. Resume scoring (0–100)
4. Identifies key skills
5. Highlights weaknesses
6. Provides improvement suggestions
7. Suggests suitable job roles

Architecture:
PDF Resume
   ↓
Text Extraction (PyPDF)
   ↓
LLM (Gemini API)
   ↓
Structured Analysis Output


Tech Stack:
Python
Google Gemini API
PyPDF
dotenv


HOW TO RUN:
1. Clone the repository: git clone https://github.com/your-username/agentic-ai-projects.git
cd resume-analyzer
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add API key
Create .env file:
GEMINI_API_KEY=your_api_key_here
5. Run the project
python src/main.py

Future Improvements:
1.Web interface (React / Streamlit)
2.ATS keyword matching
3.Resume comparison
4.Multi-language support

Key Learning: This project demonstrates:
1.Agentic AI design (LLM + structured reasoning)
2.Document processing pipeline
3.Prompt engineering for structured outputs
4.Real-world AI application development

Live Demo
- Go to this link: https://resume-analyzer-w7dw.onrender.com/docs

