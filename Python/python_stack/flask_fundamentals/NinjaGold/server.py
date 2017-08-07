from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if "gold" not in session.keys():
        session["gold"] = 0
    if "log" not in session.keys():
        session["log"] = ""
    return render_template("index.html", act_logs=session["log"], gold=session["gold"])
@app.route('/process', methods=['POST'])
def getGold():
    keys = request.form["type"]
    gold = {
        "house": randint(2, 5),
        "cave": randint(5, 10),
        "farm": randint(10, 20),
        "casino": randint(-50, 50)
    }

    logs= "You visisted the " + keys + " and "

    if gold[keys] > 0:
        logs+= "Earned "
    else:
        logs += "lost "
    logs += str(gold[keys]) + " Gold at " + str(datetime.datetime.now()) +". <br>"
    session["log"] += logs
    session["gold"] += gold[keys]
    return redirect("/")

@app.route("/reset", methods =['POST'])
def reset():
    session.clear()
    return redirect("/")
app.run(debug=True) # run our server
