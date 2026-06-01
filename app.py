from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = []


@app.route("/")
def index():
    return render_template("index.html", questions=questions)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        questions.append({
            "question": request.form["question"],
            "answer": request.form["answer"],
        })
        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
