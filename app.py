from flask import Flask, render_template, request, send_file
from handler import process_message, process_url
from pdf_generator import generate_pdf

app = Flask(__name__)

history = []
latest_result = None

stats = {
    "total": 0,
    "high": 0,
    "medium": 0,
    "low": 0
}


@app.route("/", methods=["GET", "POST"])
def home():

    global latest_result

    result = None

    if request.method == "POST":

        mode = request.form.get("mode", "message")

        if mode == "url":
            user_input = request.form["message"]
            result = process_url(user_input)

        else:
            user_input = request.form["message"]
            result = process_message(user_input)

        # Save latest result
        latest_result = result

        # Update dashboard statistics
        stats["total"] += 1

        if result["risk"] == "High":
            stats["high"] += 1

        elif result["risk"] == "Medium":
            stats["medium"] += 1

        else:
            stats["low"] += 1

        # Save history
        history.insert(0, {
            "type": result["type"],
            "risk": result["risk"],
            "score": result["score"]
        })

        if len(history) > 5:
            history.pop()

    return render_template(
        "index.html",
        result=result,
        history=history,
        stats=stats
    )


@app.route("/download")
def download():

    global latest_result

    if latest_result is None:
        return "No report available."

    filename = generate_pdf(latest_result)

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)