import re


def analyze_url(url):

    url = url.lower()

    score = 0
    reasons = []
    detected = []

    # ---------------- Suspicious Domains ----------------

    bad_domains = [
        ".xyz",
        ".top",
        ".click",
        ".live",
        ".shop",
        ".online",
        ".site"
    ]

    for domain in bad_domains:
        if domain in url:
            score += 30
            reasons.append(f"Uses suspicious domain ({domain})")
            detected.append(domain)

    # ---------------- Phishing Words ----------------

    phishing_words = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "wallet",
        "account",
        "otp"
    ]

    for word in phishing_words:
        if word in url:
            score += 15
            reasons.append(f"Contains suspicious keyword '{word}'")
            detected.append(word)

    # ---------------- IP Address ----------------

    ip_pattern = r"(https?:\/\/)?(\d{1,3}\.){3}\d{1,3}"

    if re.search(ip_pattern, url):

        score += 35
        reasons.append("Uses an IP address instead of a domain.")
        detected.append("IP Address")

    # ---------------- Long URL ----------------

    if len(url) > 70:

        score += 15
        reasons.append("URL is unusually long.")
        detected.append("Long URL")

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
        "Avoid opening suspicious URLs.",
        "Verify the official website manually.",
        "Check the domain name carefully.",
        "Never enter passwords on unknown sites."
    ]
    

    confidence = min(score + 5, 99)

    return {
    "risk": risk,
    "score": score,
    "confidence": confidence,
    "type": "Suspicious URL",
    "reasons": reasons,
    "tips": tips,
    "keywords": list(set(detected))
}