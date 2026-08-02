from flask import Flask, render_template, request
from handler import process_message, process_url

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        mode = request.form.get("mode", "message")

        if mode == "url":

            url = request.form["message"]

            result = process_url(url)

        else:

            message = request.form["message"]

            result = process_message(message)

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
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)