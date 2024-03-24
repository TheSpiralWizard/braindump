from flask import Flask, redirect, url_for, render_template, request, session
from backend import Gemini_model

app = Flask(__name__)
app.secret_key = "very_secret"

@app.route("/")
def default():
    return redirect(url_for("signup"))

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        topic = request.form["topic"]

        session["name"] = name
        session["topic"] = topic
        return redirect(url_for("timeline"))
    else:
        if "name" in session or "topic" in session:
            return redirect(url_for("timeline"))
        else:
            return render_template("signup.html")


@app.route("/timeline", methods=["POST", "GET"])
def timeline():
    if request.method == "POST":
        session.pop("name", None)
        session.pop("topic", None)

        return redirect(url_for("default"))
        
    if "name" in session or "topic" in session:
        name = session["name"]
        topic = session["topic"]

        parentList = Gemini_model.process(topic)

        name = parentList[0][0]
        description = parentList[1][0]
        numStages = parentList[5]
        stageNames = parentList[2]
        stageDescriptions = parentList[3]

        return render_template("timeline.html", name=name, projectDesc=description, num=numStages, stageNms=stageNames, stageDesc=stageDescriptions)
    else:
        return redirect(url_for("default"))

if __name__ == "__main__":
    app.run(debug=True)
