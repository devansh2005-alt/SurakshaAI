import json

def calculate_risk(findings):
    with open("config/fraud_patterns.json", "r") as f:
        patterns = json.load(f)

    score = 0
    reasons = []

    for key in findings["matched"]:
        score += patterns[key]["weight"]
        reasons.append(f"Pattern matched: {key}")

    if findings["fear"]:
        score += 20
        reasons.append("Fear-based language detected")

    if findings["urgency"]:
        score += 20
        reasons.append("Urgency-based pressure detected")

    probability = min(score, 100)
    return probability, reasons
