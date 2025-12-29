from datetime import datetime

def generate_report(message, fraud_type, probability):
    return {
        "timestamp": datetime.now().isoformat(),
        "fraud_type": fraud_type,
        "risk_probability": f"{probability}%",
        "message_snapshot": message
    }
