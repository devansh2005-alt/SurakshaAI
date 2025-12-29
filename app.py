from engine.analyzer import analyze_message
from engine.scorer import calculate_risk
from engine.classifier import classify
from prevention.interrupter import interrupt_action
from reporting.cyber_report import generate_report

print("🔐 SurakshaAI | Cyber Fraud Prevention System")
print("---------------------------------------------")

message = input("Enter suspicious message or call text: ")

findings = analyze_message(message)
probability, reasons = calculate_risk(findings)
fraud_type = classify(findings)

print(f"\nFraud Type: {fraud_type}")
print(f"Fraud Probability: {probability}%")

print("\nDetection Reasons:")
for r in reasons:
    print("-", r)

if probability >= 80:
    interrupt_action()
    report = generate_report(message, fraud_type, probability)

    print("\n📄 Cyber Cell Report Generated:")
    for k, v in report.items():
        print(f"{k}: {v}")
else:
    print("\n✅ No immediate high-risk threat detected.")
