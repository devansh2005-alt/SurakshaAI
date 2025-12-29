import json

def analyze_message(message):
    with open("config/fraud_patterns.json", "r") as f:
        patterns = json.load(f)

    msg = message.lower()

    findings = {
        "matched": [],
        "fear": False,
        "urgency": False
    }

    for key, data in patterns.items():
        if key == "BEHAVIOR":
            continue
        for word in data["keywords"]:
            if word in msg:
                findings["matched"].append(key)
                break

    for word in patterns["BEHAVIOR"]["fear"]:
        if word in msg:
            findings["fear"] = True
            break

    for word in patterns["BEHAVIOR"]["urgency"]:
        if word in msg:
            findings["urgency"] = True
            break

    return findings
