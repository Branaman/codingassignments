from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    session['count'] += 1
    return render_template("index.html", counter = session['count'])
app.run(debug=True) # run our server
