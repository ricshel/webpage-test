from functions import *
from pathlib import Path
from datetime import datetime

actual = {
    "top6": ["liverpool", "crystal palace",  "bournemouth", "manchester city", "arsenal", "spurs"],
    "bottom3": ["villa", "west ham", "wolves"],
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
        "clean sheets": "raya",
        "first manager sacked": "santo",
    },
}

predictions = [
    {
        "name": "Richard",
        "top6": ["manchester city", "liverpool", "chelsea", "manchester united", "newcastle", "arsenal"],
        "bottom3": ["brentford", "sunderland", "burnley"],
        "cups": {
            "fa cup": "liverpool",
            "europa league": "villa",
            "carabao cup": "manchester united",
            "champions league": "manchester city",
            "conference league": "aek athens",
            },
        "awards": {
            "golden boot": "haaland",
            "most assists": "wirtz",
            "clean sheets": "alisson",
            "first manager sacked": "parker",
        },
        "score": 0,
    },
    {
        "name": "Hickey",
        "top6": [ "liverpool", "manchester city", "arsenal", "chelsea", "villa", "manchester united" ],
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
        "score": 0,
    },
    {
        "name": "Shelton (not playing for cash)",
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
        "score": 0,
    },
    {
        "name": "Dave",
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
        "score": 0,
    },
    {
        "name": "Rob",
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
        "score": 0,
    },
    {
        "name": "Kieron",
        "top6": [
            "manchester city",
            "liverpool",
            "arsenal",
            "chelsea",
            "villa",
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
        "score": 0,
    },
    {
        "name": "Ste",
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
        "score": 0,
    },
    {
        "name": "Matt",
        "top6": [
            "liverpool",
            "arsenal",
            "chelsea",
            "manchester city",
            "villa",
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
        "score": 0,
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

try:
    from zoneinfo import ZoneInfo
    _TZ = ZoneInfo("Europe/London")
except Exception:
    _TZ = None

def render_single_table(predictions, actual, include_actual=True, actual_label="Actual", updated_at=None):
    # figure out the timestamp string
    if updated_at is None:
        if _TZ:
            now = datetime.now(_TZ)
        else:
            now = datetime.utcnow()
        updated_at = now.strftime("%a %d-%B-%Y, %R").strip()

    # column sets (use actual keys for consistent ordering)
    cup_cols = list(actual.get("cups", {}).keys())
    award_cols = list(actual.get("awards", {}).keys())

    headers = (
        ["Name", "Score"] +
        [f"Top {i}" for i in range(1, 7)] +
        [f"Bottom {i}" for i in range(1, 4)] +
        [f"{cup} (winner)" for cup in cup_cols] +
        award_cols
    )

    def td(x, align_right=False):
        style = " style='text-align:right'" if align_right else ""
        return f"<td{style}>{x}</td>"

    body_rows = []

    # "Actual" row
    if include_actual:
        actual_top = actual.get("top6", [])
        actual_bot = actual.get("bottom3", [])
        actual_cups_winners = [(actual["cups"].get(c, {}) or {}).get("winner", "") for c in cup_cols]
        actual_awards_vals  = [actual.get("awards", {}).get(a, "") for a in award_cols]

        cells = []
        cells.append(td(actual_label))
        cells.append(td("-", align_right=True))
        cells += [td(actual_top[i] if i < len(actual_top) else "") for i in range(6)]
        cells += [td(actual_bot[i] if i < len(actual_bot) else "") for i in range(3)]
        cells += [td(v) for v in actual_cups_winners]
        cells += [td(v) for v in actual_awards_vals]
        body_rows.append("<tr>" + "".join(cells) + "</tr>")

    # Participant rows
    for p in predictions:
        top = p.get("top6", [])
        bot = p.get("bottom3", [])
        cups = p.get("cups", {})
        awards = p.get("awards", {})

        cells = []
        cells.append(td(p.get("name", "")))
        cells.append(td(int(p.get("score", 0)), align_right=True))
        cells += [td(top[i] if i < len(top) else "") for i in range(6)]
        cells += [td(bot[i] if i < len(bot) else "") for i in range(3)]
        cells += [td(cups.get(c, "")) for c in cup_cols]
        cells += [td(awards.get(a, "")) for a in award_cols]
        body_rows.append("<tr>" + "".join(cells) + "</tr>")

    head = "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"

    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Predictions — Full Table</title>
<body style="font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;max-width:95vw;margin:40px auto;padding:0 16px">
  <h1 style="margin:0 0 6px">Predictions — Full Table</h1>
  <p style="margin:0 0 16px;color:#555">Last updated: {updated_at}</p>
  <div style="overflow:auto">
    <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;min-width:100%">
      <thead>{head}</thead>
      <tbody>
        {"\n".join(body_rows)}
      </tbody>
    </table>
  </div>
</body>
</html>"""

# after scoring:
ranked = predictions  # or your sorted list if you sort elsewhere
print(ranked)
html = render_single_table(ranked, actual)

# write to dist/index.html for GitHub Pages action
out = Path("dist")
out.mkdir(parents=True, exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
