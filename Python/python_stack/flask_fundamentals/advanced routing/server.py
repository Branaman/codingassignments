from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/route/with/<vararg>')
def handler_function(vararg):
    # here you can use the variable "vararg"
    # if you want to see what our argument looks like
    print vararg
    # we could do other things with this information from this point on such as:
    # use it to retrieve some records from the database
    # render a particular template
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print username
    print id
    return render_template("user.html")
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return render_template('/users.html', username = name, id = email)
app.run(debug=True)
