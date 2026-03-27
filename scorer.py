def calculate_score(p):
    score = 0

    if p["searchVolume"] >= 3000:
        score += 25
    elif p["searchVolume"] >= 2000:
        score += 20

    if p["reviews"] < 500:
        score += 20
    elif p["reviews"] < 1500:
        score += 10

    if p["margin"] >= 30:
        score += 25
    elif p["margin"] >= 20:
        score += 15
    elif p["margin"] >= 15:
        score += 10

    if p["weight"] <= 5:
        score += 10

    if p["price"] <= 40:
        score += 10

    if p["trend"] == "Evergreen":
        score += 10

    return score
