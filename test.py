from functions import *
from pathlib import Path

actual = {
    "top6": ["liverpool", "chelsea", "arsenal", "spurs", "everton", "sunderland"],
    "bottom3": ["fulham", "villa", "wolves"],
    "cups": {
        "fa cup":           {"winner": "placeholder", "runner_up": "placeholder"},
        "europa league":    {"winner": "placeholder", "runner_up": "placeholder"},
        "carabao cup":      {"winner": "placeholder", "runner_up": "placeholder"},
        "champions league": {"winner": "placeholder", "runner_up": "placeholder"},
        "conference league":{"winner": "placeholder", "runner_up": "placeholder"},
    },

    "awards": {
        "golden boot": "haaland",
        "most assists": "grealish",
        "clean sheets": "pope",
        "first manager sacked": "placeholder",
    },
}


predictions = [
    {
        "name": "Richard",
        "top6": ["manchester city", "liverpool", "chelsea", "manchester united", "newcastle", "arsenal"],
        "bottom3": ["brentford", "sunderland", "burnley"],
        "cups": {
            "fa cup": "manchester united",
            "europa league": "",
            "carabao cup": "",
            "champions league": "",
            "conference league": "",
            },
        "awards": {
            "golden boot": "haaland",
            "most assists": "wirtz",
            "clean sheets": "alisson",
            "first manager sacked": "parker",
        },
        "score": 0.0,
    },
    {
        "name": "Hickey",
        "top6": [ "liverpool", "manchester city", "arsenal" "chelsea", "villa", "manchester united" ],
        "bottom3": ["burnley", "sunderland", "leeds"],
        "cups": {
            "fa cup": "liverpool",
            "europa league": "villa",
            "carabao cup": "manchester city",
            "champions league": "bayern munich",
            "conference league": "real betis",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "salah",
            "clean sheets": "arsenal",
            "first manager sacked": "parker",
        },
        "score": 0.0,
    },
    {
        "name": "Shelton",
        "top6": [ "liverpool", "manchester city", "arsenal", "chelsea", "manchester united", "villa" ],
        "bottom3": [ "bournemouth", "leeds", "burnley", ],
        "cups": {
            "fa cup": "arsenal",
            "europa league": "roma",
            "carabao cup": "chelsea",
            "champions league": "barcelona",
            "conference league": "besiktas",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "wirtz",
            "clean sheets": "alisson",
            "first manager sacked": "pereira",
        },
        "score": 0.0,
    },
    {
        "name": "David",
        "top6": [
            "manchester united",
            "chelsea",
            "manchester city",
            "arsenal",
            "liverpool",
            "brighton"
            ],
        "bottom3": [ "wolves", "city", "leeds", ],
        "cups": {
            "fa cup": "chelsea",
            "europa league": "roma",
            "carabao cup": "manchester united",
            "champions league": "real madrid",
            "conference league": "crystal palace",
        },
        "awards": {
            "golden boot": "sesko",
            "most assists": "bruno",
            "clean sheets": "alisson",
            "first manager sacked": "farke",
        },
        "score": 0.0,
    },
    {
        "name": "rob",
        "top6": [
            "liverpool",
            "arsenal",
            "manchester city",
            "chelsea",
            "manchester united",
            "villa"
            ],
        "bottom3": [ "brentford", "burnley", "sunderland" ],
        "cups": {
            "fa cup": "liverpool",
            "europa league": "roma",
            "carabao cup": "manchester city",
            "champions league": "real madrid",
            "conference league": "fiorentina",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "salah",
            "clean sheets": "allison",
            "first manager sacked": "andrews",
        },
        "score": 0.0,
    },
    {
        "name": "kieron",
        "top6": [
            "manchester city",
            "liverpool",
            "arsenal",
            "chelsea",
            "villa"
            "spurs",
            ],
        "bottom3": [ "wolves", "sunderland", "burnley" ],
        "cups": {
            "fa cup": "manchester city",
            "europa league": "athletic bilbao",
            "carabao cup": "manchester city",
            "champions league": "manchester city",
            "conference league": "stuttgart",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "salah",
            "clean sheets": "raya",
            "first manager sacked": "amorim",
        },
        "score": 0.0,
    },
    {
        "name": "ste",
        "top6": [
            "arsenal",
            "manchester city",
            "liverpool",
            "chelsea",
            "newcastle",
            "manchester united"
            ],
        "bottom3": [
            "bournemouth",
            "brentford",
            "leeds"
            ],
        "cups": {
            "fa cup": "manchester city",
            "europa league": "porto",
            "carabao cup": "chelsea",
            "champions league": "barcelona",
            "conference league": "fiorentina",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "saka",
            "clean sheets": "raya",
            "first manager sacked": "andrews",
        },
        "score": 0.0,
    },
    {
        "name": "matt",
        "top6": [
            "liverpool",
            "arsenal",
            "chelsea",
            "manchester city",
            "villa"
            "nottingham forest",
            ],
        "bottom3": [
            "brentford",
            "leeds",
            "sunderland",
            ],
        "cups": {
            "fa cup": "arsenal",
            "europa league": "roma",
            "carabao cup": "chelsea",
            "champions league": "barcelona",
            "conference league": "real betis",
        },
        "awards": {
            "golden boot": "haaland",
            "most assists": "salah",
            "clean sheets": "raya",
            "first manager sacked": "howe",
        },
        "score": 0.0,
    },
]

# Variables
actual_top6 = actual["top6"]
actual_bottom3 = actual["bottom3"]

# Calculations
predictions = score_top6(actual, predictions)
predictions = score_bottom3(actual, predictions)
predictions = score_cups_simple(actual, predictions)
predictions = score_awards_simple(actual, predictions)

def render_html(predictions):
    rows = "\n".join(
        f"<tr><td>{p['name']}</td><td style='text-align:right'>{p['score']:.1f}</td></tr>"
        for p in predictions
    )
    return f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Predictions — Scores</title>
<body style="font-family:system-ui;max-width:700px;margin:40px auto;padding:0 16px">
  <h1>Predictions — Scores</h1>
  <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%">
    <thead><tr><th>Name</th><th style="text-align:right">Score</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body></html>"""

# after computing:
# ranked = score_awards_simple(actual, predictions)  # plus your other scorers first
html = render_html(predictions)  # or ranked, depending on your flow
Path("dist").mkdir(exist_ok=True)
Path("dist/index.html").write_text(html, encoding="utf-8")