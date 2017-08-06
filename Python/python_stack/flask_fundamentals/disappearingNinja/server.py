from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/ninja/<color>')
def ninjaFinder(color):
    if color == "red":
        ninjaColor = "raphael.jpg"
    elif color == "blue":
        ninjaColor = "leonardo.jpg"
    elif color == "orange":
        ninjaColor = "michelangelo.jpg"
    elif color == "purple":
        ninjaColor = "donatello.jpg"
    else:
        ninjaColor = "notapril.jpg"
    return render_template("ninjas.html", ninjaColor = ninjaColor)
@app.route('/ninja')
def allninjas():
    ninjaColor = 'tmnt.png'
    return render_template('/ninjas.html', ninjaColor = ninjaColor)
app.run(debug=True)
