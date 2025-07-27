# VLR Scoreboard

A simple Flask web application that displays live Valorant match scores using the [vlr.gg API](https://github.com/axsddlr/vlrggapi).

## Setup

1. Create and activate a Python virtual environment (optional).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python run.py
```

4. Open your browser at [http://localhost:5000](http://localhost:5000) to see the dashboard.

The app fetches live match data from `https://vlrggapi.vercel.app/match?q=live_score` and displays the teams, scores, and event information.
