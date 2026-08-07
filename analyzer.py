from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
AI_EXPLANATIONS = {

    "OTP Scam":
    "This message attempts to obtain your One-Time Password (OTP). Genuine banks, payment apps and government agencies never ask for your OTP through SMS, WhatsApp or email.",

    "Bank KYC Scam":
    "Scammers often impersonate banks and claim your account will be blocked unless you immediately update your KYC using a fake website.",

    "Lottery Scam":
    "Unexpected lottery or prize notifications are a common scam. Legitimate organizations do not ask winners to pay processing fees or click unknown links.",

    "Fake Job Scam":
    "Real companies never ask candidates to pay registration fees, interview charges or security deposits before hiring.",

    "UPI Scam":
    "Fraudsters trick victims into approving UPI collect requests or fake payment confirmations instead of receiving money.",

    "Courier Scam":
    "Fake courier messages create urgency about a parcel and redirect victims to phishing websites asking for payment or personal information.",

    "Romance Scam":
    "Romance scammers build emotional trust before requesting money for emergencies, travel expenses or medical bills.",

    "Unknown":
    "The message contains suspicious characteristics commonly found in online scams. Always verify the sender before taking action."

}
def analyze_message(message):

    text = message.lower()

    score = 0
    scam_type = "Unknown"

    reasons = []
    tips = []
    detected_keywords = []

    # ---------------- OTP ----------------

    otp_keywords = [
        "otp","verification code","one time password","share otp"
    ]

    if any(word in text for word in otp_keywords):
        score += 40
        scam_type = "OTP Scam"
        reasons.append("Requests or mentions an OTP.")
        detected_keywords.extend(["OTP"])

    # ---------------- KYC ----------------

    kyc_keywords = [
        "kyc","verify your account","account blocked",
        "account suspended","update kyc","rbi",
        "bank account","verify now"
    ]

    if any(word in text for word in kyc_keywords):
        score += 45
        scam_type = "Bank KYC Scam"
        reasons.append("Fake KYC / account verification request.")
        detected_keywords.extend(["KYC", "Bank"])
    # ---------------- Fake Job ----------------

    job_keywords = [
        "work from home",
        "job offer",
        "registration fee",
        "interview fee",
        "salary",
        "hiring"
    ]

    if any(word in text for word in job_keywords):
        score += 40
        scam_type = "Fake Job Scam"
        reasons.append("Suspicious job offer.")
        detected_keywords.extend(["Job", "Salary"])
    # ---------------- Lottery ----------------

    lottery_keywords = [
        "lottery",
        "won",
        "winner",
        "jackpot",
        "prize",
        "claim reward"
    ]

    if any(word in text for word in lottery_keywords):
        score += 45
        scam_type = "Lottery Scam"
        reasons.append("Claims you won money or a prize.")
        detected_keywords.extend(["Lottery", "Prize"])

    # ---------------- UPI ----------------

    upi_keywords = [
        "upi",
        "google pay",
        "phonepe",
        "paytm",
        "accept payment",
        "collect request"
    ]

    if any(word in text for word in upi_keywords):
        score += 45
        scam_type = "UPI Scam"
        reasons.append("Suspicious UPI payment request.")
        detected_keywords.extend(["UPI", "Payment"])

    # ---------------- Courier ----------------

    courier_keywords = [
        "parcel",
        "delivery",
        "courier",
        "india post",
        "fedex",
        "dhl"
    ]

    if any(word in text for word in courier_keywords):
        score += 35
        scam_type = "Courier Scam"
        reasons.append("Fake parcel or courier notification.")
        detected_keywords.extend(["Parcel", "Courier"])

    # ---------------- Romance ----------------

    romance_keywords = [
        "send money",
        "i love you",
        "help me",
        "emergency",
        "airport"
    ]

    if any(word in text for word in romance_keywords):
        score += 40
        scam_type = "Romance Scam"
        reasons.append("Emotional manipulation requesting money.")
        detected_keywords.extend(["Emergency", "Money"])

    # ---------------- Links ----------------

    if "http://" in text or "https://" in text or ".com" in text or ".xyz" in text:

        score += 20

        
        reasons.append("Contains a suspicious link.")
        detected_keywords.append("Link")

    # ---------------- Urgency ----------------

    urgency = [
        "urgent",
        "immediately",
        "today",
        "within",
        "24 hours",
        "expire",
        "blocked",
        "suspended"
    ]

    if any(word in text for word in urgency):

        score += 15

        reasons.append("Creates urgency to pressure you.")
        detected_keywords.append("Urgency")

    # ---------------- Payment ----------------

    payment = [
        "pay",
        "fee",
        "processing fee",
        "registration fee",
        "₹",
        "$"
    ]

    if any(word in text for word in payment):

        score += 20

        reasons.append("Requests payment.")
        detected_keywords.append("Payment")

    # ---------------- Clamp ----------------

    if score > 100:
        score = 100

    # ---------------- Risk ----------------

    if score >= 75:
        risk = "High"

    elif score >= 40:
        risk = "Medium"

    else:
        risk = "Low"

    # ---------------- Tips ----------------

    tips = [

        "Never share OTPs or passwords.",

        "Do not click suspicious links.",

        "Verify with the official company before acting.",

        "Never pay registration or processing fees.",

        "Report phishing attempts."

    ]

    confidence = min(score + 5, 99)

    return {
    "risk": risk,
    "score": score,
    "confidence": confidence,
    "type": scam_type,
    "explanation": AI_EXPLANATIONS.get(
        scam_type,
        AI_EXPLANATIONS["Unknown"]
    ),
    "reasons": reasons,
    "keywords": list(set(detected_keywords)),
    "tips": tips
}
if __name__ == "__main__":
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Reply with exactly one word: WORKING"
    )
    print(response.text)