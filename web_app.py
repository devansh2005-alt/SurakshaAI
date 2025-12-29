import streamlit as st
from engine.analyzer import analyze_message
from engine.scorer import calculate_risk
from engine.classifier import classify

st.set_page_config(page_title="SurakshaAI", page_icon="🛡️", layout="centered")

st.title("🛡️ SurakshaAI")
st.subheader("Cyber Fraud Prevention Advisory Tool")

st.write(
    "Paste any suspicious message or call text below. "
    "SurakshaAI will analyze it and warn you if it looks like a cyber fraud."
)

message = st.text_area("Enter message / call text", height=150)

if st.button("Check for Fraud"):
    if message.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        findings = analyze_message(message)
        probability, reasons = calculate_risk(findings)
        fraud_type = classify(findings)

        if probability >= 80:
            st.error(f"🚨 HIGH RISK FRAUD ({probability}%)")
        elif probability >= 50:
            st.warning(f"⚠️ POSSIBLE FRAUD ({probability}%)")
        else:
            st.success("✅ Low risk detected")

        st.write("### Likely Fraud Type:")
        st.info(fraud_type)

        st.write("### Detection Reasons:")
        for r in reasons:
            st.write("- ", r)

st.markdown("---")
st.caption(
    "⚠️ Disclaimer: SurakshaAI provides advisory analysis only. "
    "It does not replace law enforcement. "
    "If money is lost, immediately call 1930 or visit cybercrime.gov.in."
)
