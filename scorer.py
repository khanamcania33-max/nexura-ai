def calculate_score(p):

    score = 0

    # Demand
    if p["searchVolume"] >= 3000:
        score += 25
    elif p["searchVolume"] >= 2000:
        score += 20
    else:
        score += 10

    # Competition
    if p["reviews"] < 500:
        score += 20
    elif p["reviews"] < 1500:
        score += 10

    # Margin
    if p["margin"] >= 30:
        score += 25
    elif p["margin"] >= 20:
        score += 15
    elif p["margin"] >= 15:
        score += 10

    # Weight
    if p["weight"] <= 5:
        score += 10

    # Price rule
    if p["price"] <= 40:
        score += 10

    # Evergreen
    if p["trend"] == "Evergreen":
        score += 10

    return score
