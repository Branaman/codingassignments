from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index(winLose = "", NewGame = False):
    if NewGame is True or len(session) < 1:
        session['randNum'] = random.randrange(0,101)
        hide = "text"
    if NewGame is False:
        status = "Guess?"
        hide = "text"
    else:
        status = "Again?"
        hide = "hidden"
    return render_template("index.html", hide = hide, winLose = winLose, status = status)
@app.route('/process', methods=['POST'])
def guessCheck():
    if request.form['number'].isdigit():
        if len(request.form['number']) > 0:
            session['guess'] = int(request.form['number'])
            if session['guess'] is session['randNum']:
                return index("Nice Guessing!", True)
            if session['guess'] < session['randNum']:
                return index("Guess too Low")
            if session['guess'] > session['randNum']:
                return index("Guess too High")
        else:
            return index("Please insert a valid guess")
    else:
        return index("Please insert a valid guess")
app.run(debug=True) # run our server
