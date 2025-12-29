def classify(findings):
    if "DIGITAL_ARREST" in findings["matched"]:
        return "Digital Arrest Scam"
    if "FAKE_POLICE" in findings["matched"]:
        return "Authority Impersonation Scam"
    if "OTP_FRAUD" in findings["matched"]:
        return "OTP Fraud"
    if "UPI_SCAM" in findings["matched"]:
        return "UPI Payment Scam"
    return "Suspicious Activity"
