def analyze_message(message):

    text = message.lower()

    score = 0
    scam_type = "Unknown"

    reasons = []
    tips = []

    # ---------------- OTP ----------------

    otp_keywords = [
        "otp","verification code","one time password","share otp"
    ]

    if any(word in text for word in otp_keywords):
        score += 40
        scam_type = "OTP Scam"
        reasons.append("Requests or mentions an OTP.")

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

    # ---------------- Links ----------------

    if "http://" in text or "https://" in text or ".com" in text or ".xyz" in text:

        score += 20

        reasons.append("Contains a suspicious link.")

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
    "reasons": reasons,
    "tips": tips
}