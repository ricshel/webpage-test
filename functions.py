def score_top6(actual, predictions):
    actual_top6 = actual["top6"]
    in_top6 = set(actual_top6)

    for p in predictions:
        p.setdefault("score", 0)
        picks = p.get("top6", [])[:6]
        for i, v in enumerate(picks):
            if not v:
                continue
            if i == 0:
                if v == actual_top6[0]:
                    p["score"] += 10
                elif v in in_top6:
                    p["score"] += 2
            else:
                if v == actual_top6[i]:
                    p["score"] += 5
                elif v in in_top6:
                    p["score"] += 2
    # for p in predictions:
    #     print(f"{p['name']}: {p['score']}")
    return predictions

def score_bottom3(actual, predictions):
    actual_bottom3 = actual["bottom3"]
    in_bottom3 = set(actual_bottom3)

    for p in predictions:
        p.setdefault("score", 0)
        picks = p.get("bottom3", [])[:3]
        for i, v in enumerate(picks):
            if not v:
                continue
            if v == actual_bottom3[i]:
                p["score"] += 5       # exact spot
            elif v in in_bottom3:
                p["score"] += 2       # in bottom 3, wrong spot
    # for p in predictions:
    #     print(f"{p['name']}: {p['score']}")
    return predictions

def score_cups_simple(actual, predictions):
    for p in predictions:
        p.setdefault("score", 0)
        for cup, res in actual["cups"].items():
            guess = p.get("cups", {}).get(cup, "")
            if not guess:
                continue
            if guess == res.get("winner", ""):
                p["score"] += 5
            elif guess == res.get("runner_up", ""):
                p["score"] += 2
    # for p in predictions:
    #     print(f"{p['name']}: {p['score']}")
    return predictions

def score_awards_simple(actual, predictions):
    for p in predictions:
        p.setdefault("score", 0)
        for award, winner in actual.get("awards", {}).items():
            if winner and p.get("awards", {}).get(award, "") == winner:
                p["score"] += 5

    # THIS BIT
    # return highest → lowest by score
    return sorted(predictions, key=lambda p: p.get("score", 0), reverse=True)