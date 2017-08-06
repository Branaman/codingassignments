from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    DojoLocation = request.form['DojoLocation']
    favLang = request.form['favLang']
    comments = request.form['comments']
    # redirects back to the '/' route
    return render_template('/result.html', username = name, userDojo = DojoLocation, userFavLang = favLang, comments = comments)
app.run(debug=True)
