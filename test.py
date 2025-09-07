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
            "fa cup": "liverpool",
            "europa league": "aston villa",
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

def render_html(predictions, actual):
    # leaderboard rows (integer scores)
    rows = "\n".join(
        f"<tr><td>{p['name']}</td><td style='text-align:right'>{int(p['score'])}</td></tr>"
        for p in predictions
    )

    # actual: Top 6
    top6_rows = "\n".join(
        f"<tr><td style='text-align:right'>{i+1}</td><td>{team}</td></tr>"
        for i, team in enumerate(actual.get("top6", []))
    )

    # actual: Bottom 3
    bottom3_rows = "\n".join(
        f"<tr><td style='text-align:right'>{i+1}</td><td>{team}</td></tr>"
        for i, team in enumerate(actual.get("bottom3", []))
    )

    # actual: Cups (winner / runner-up)
    cups_rows = "\n".join(
        f"<tr><td>{cup}</td><td>{res.get('winner','')}</td><td>{res.get('runner_up','')}</td></tr>"
        for cup, res in actual.get("cups", {}).items()
    )

    # actual: Awards
    awards_rows = "\n".join(
        f"<tr><td>{award}</td><td>{winner}</td></tr>"
        for award, winner in actual.get("awards", {}).items()
    )

    rules = """
    <section style="margin-top:24px">
      <h2 style="margin:0 0 8px;font-size:18px">Scoring Rules</h2>
      <ul style="line-height:1.6;margin:0 0 8px 18px;padding:0">
        <li><b>Top 6</b>: 10 pts for champions; 5 pts for any other exact position; 2 pts if the team is in the top 6 (wrong spot).</li>
        <li><b>Bottom 3</b>: 5 pts for exact position; 2 pts if the team is in the bottom 3 (wrong spot).</li>
        <li><b>Cups</b>: 5 pts for winner; 2 pts for runner-up.</li>
        <li><b>Awards</b> (Golden Boot, Most Assists, Most Clean Sheets, First Manager Sacked): 5 pts each correct pick.</li>
      </ul>
    </section>
    """

    actual_html = f"""
    <section style="margin-top:28px">
      <h2 style="margin:0 0 8px;font-size:18px">Actual Results</h2>

      <h3 style="margin:12px 0 6px;font-size:16px">Top 6</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead><tr><th style="text-align:right;width:60px">Pos</th><th>Team</th></tr></thead>
        <tbody>
          {top6_rows}
        </tbody>
      </table>

      <h3 style="margin:12px 0 6px;font-size:16px">Bottom 3</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead><tr><th style="text-align:right;width:60px">Pos</th><th>Team</th></tr></thead>
        <tbody>
          {bottom3_rows}
        </tbody>
      </table>

      <h3 style="margin:12px 0 6px;font-size:16px">Cups</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead><tr><th>Cup</th><th>Winner</th><th>Runner-up</th></tr></thead>
        <tbody>
          {cups_rows}
        </tbody>
      </table>

      <h3 style="margin:12px 0 6px;font-size:16px">Awards</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%">
        <thead><tr><th>Award</th><th>Winner</th></tr></thead>
        <tbody>
          {awards_rows}
        </tbody>
      </table>
    </section>
    """

    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Predictions — Scores</title>
<body style="font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;max-width:760px;margin:40px auto;padding:0 16px">
  <h1 style="margin:0 0 12px">Predictions — Scores</h1>

  <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%">
    <thead>
      <tr>
        <th style="text-align:left">Name</th>
        <th style="text-align:right">Score</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>

  {rules}
  {actual_html}
</body>
</html>"""

def build_predictions_tables(predictions, actual):
    # columns we’ll use
    top6_cols = [f"Pos {i}" for i in range(1, 7)]
    bottom3_cols = [f"Pos {i}" for i in range(18, 21)]  # label however you prefer

    # use the actual keys so everyone lines up to the same set/order
    cup_cols = list(actual.get("cups", {}).keys())
    award_cols = list(actual.get("awards", {}).keys())

    def row(cells):
        tds = "".join(f"<td>{(c if c is not None else '')}</td>" for c in cells)
        return f"<tr>{tds}</tr>"

    # Top 6 table (rows = names, columns = positions)
    top6_header = row(["Name"] + top6_cols)
    top6_body = "\n".join(
        row([p["name"]] + [p.get("top6", [""]*6)[i] if i < len(p.get("top6", [])) else "" for i in range(6)])
        for p in predictions
    )
    top6_table = f"""
      <h3 style="margin:12px 0 6px;font-size:16px">Predictions — Top 6</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead>{top6_header}</thead>
        <tbody>{top6_body}</tbody>
      </table>
    """

    # Bottom 3 table
    bottom3_header = row(["Name"] + bottom3_cols)
    bottom3_body = "\n".join(
        row([p["name"]] + [p.get("bottom3", [""]*3)[i] if i < len(p.get("bottom3", [])) else "" for i in range(3)])
        for p in predictions
    )
    bottom3_table = f"""
      <h3 style="margin:12px 0 6px;font-size:16px">Predictions — Bottom 3</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead>{bottom3_header}</thead>
        <tbody>{bottom3_body}</tbody>
      </table>
    """

    # Cups table (winner picks only; if you later capture runner_up in predictions, add another column)
    cups_header = row(["Name"] + cup_cols)
    cups_body = "\n".join(
        row([p["name"]] + [p.get("cups", {}).get(cup, "") for cup in cup_cols])
        for p in predictions
    )
    cups_table = f"""
      <h3 style="margin:12px 0 6px;font-size:16px">Predictions — Cups (winner pick)</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;margin-bottom:10px">
        <thead>{cups_header}</thead>
        <tbody>{cups_body}</tbody>
      </table>
    """

    # Awards table
    awards_header = row(["Name"] + award_cols)
    awards_body = "\n".join(
        row([p["name"]] + [p.get("awards", {}).get(aw, "") for aw in award_cols])
        for p in predictions
    )
    awards_table = f"""
      <h3 style="margin:12px 0 6px;font-size:16px">Predictions — Awards</h3>
      <table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%">
        <thead>{awards_header}</thead>
        <tbody>{awards_body}</tbody>
      </table>
    """

    return f"""
    <section style="margin-top:28px">
      <h2 style="margin:0 0 8px;font-size:18px">Predictions (by person)</h2>
      {top6_table}
      {bottom3_table}
      {cups_table}
      {awards_table}
    </section>
    """

# after scoring:
ranked = predictions  # or your sorted list if you sort elsewhere
html = render_html(ranked, actual) + build_predictions_tables(ranked, actual)

# write to dist/index.html for GitHub Pages action
out = Path("dist")
out.mkdir(parents=True, exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")