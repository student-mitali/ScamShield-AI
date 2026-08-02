from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(result, filename="report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>ScamShield AI Threat Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Risk Level:</b> {result['risk']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Threat Score:</b> {result['score']}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>AI Confidence:</b> {result['confidence']}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Threat Type:</b> {result['type']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Threat Indicators</b>", styles["Heading2"]))

    for reason in result["reasons"]:
        story.append(Paragraph(f"• {reason}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Detected Keywords</b>", styles["Heading2"]))

    if result["keywords"]:
        story.append(Paragraph(", ".join(result["keywords"]), styles["BodyText"]))
    else:
        story.append(Paragraph("None", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Safety Recommendations</b>", styles["Heading2"]))

    for tip in result["tips"]:
        story.append(Paragraph(f"• {tip}", styles["BodyText"]))

    doc.build(story)

    return filename