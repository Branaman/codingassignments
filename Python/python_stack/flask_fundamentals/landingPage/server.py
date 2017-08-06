from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")
@app.route('/dojos')
def dojos():
    return render_template("dojos.html")
app.run(debug=True)
