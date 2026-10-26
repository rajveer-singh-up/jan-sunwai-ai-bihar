# Jan-Sunwai AI - Bihar Police Cyber Hackathon 2026
Problem #4 - Analysing Public Grievances

How to run:
pip install -r requirements.txt
uvicorn app:app --reload

API:
POST /analyze {"text":"Mere account se 50000 UPI se kat gaye","amount":50000,"district":"Patna"}

Solves: Auto-categorize, prioritize, and detect fraud patterns in Bihar cyber complaints.
Future: Add Indic-BERT for Hindi/Bhojpuri, Map dashboard.
