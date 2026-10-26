from fastapi import FastAPI
from pydantic import BaseModel
import re
from collections import defaultdict

app = FastAPI(title="Jan-Sunwai AI - Bihar Police")

class Complaint(BaseModel):
    text: str
    amount: int = 0
    district: str = ""

def classify_complaint(text):
    text = text.lower()
    if any(x in text for x in ["upi", "paytm", "account", "money", "rs", "rupees"]):
        return "Financial Fraud"
    elif any(x in text for x in ["instagram", "facebook", "abuse", "harass"]):
        return "Social Media Crime"
    elif any(x in text for x in ["apk", "app", "link", "download"]):
        return "Fake App Fraud"
    else:
        return "General Cyber Complaint"

def get_priority(amount, category):
    if amount > 50000 or category == "Financial Fraud":
        return "RED - Urgent"
    elif amount > 10000:
        return "YELLOW - Medium"
    else:
        return "GREEN - Low"

complaints_db = []

@app.post("/analyze")
def analyze(complaint: Complaint):
    category = classify_complaint(complaint.text)
    priority = get_priority(complaint.amount, category)
    complaints_db.append(complaint.dict())
    same_district = [c for c in complaints_db if c['district'] == complaint.district]
    pattern_alert = ""
    if len(same_district) >= 3:
        pattern_alert = f"ALERT: {complaint.district} me {len(same_district)} similar complaints - Possible Gang!"
    return {
        "category": category,
        "priority": priority,
        "district": complaint.district,
        "pattern": pattern_alert,
        "assigned_to": "Cyber Cell, Bihar Police"
    }

@app.get("/dashboard")
def dashboard():
    district_count = defaultdict(int)
    for c in complaints_db:
        district_count[c['district']] += 1
    return {"total_complaints": len(complaints_db), "district_wise": dict(district_count)}
