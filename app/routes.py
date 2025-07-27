import requests
from flask import render_template
from app import app

VLR_API_BASE = "https://vlrggapi.vercel.app"

@app.route('/')
def index():
    # Fetch live match scores
    try:
        resp = requests.get(f"{VLR_API_BASE}/match", params={"q": "live_score"}, timeout=10)
        data = resp.json().get('data', {})
        matches = data.get('segments', []) if data.get('status') == 200 else []
    except Exception:
        matches = []
    return render_template('index.html', matches=matches)
