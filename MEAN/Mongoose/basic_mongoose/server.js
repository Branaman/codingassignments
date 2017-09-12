// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/basic_mongoose');
var UserSchema = new mongoose.Schema({
    first_name:  { type: String, required: true, minlength: 6},
    last_name: { type: String, required: true, maxlength: 20 },
    age: { type: Number, min: 1, max: 150 },
    email: { type: String, required: true }
}, {timestamps: true });
mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
var User = mongoose.model('User') // We are retrieving this Schema from our Models, named 'User'
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request
// The root route -- we want to get all of the users from the database and then render the index view passing it all of the users
app.get('/', function(req, res) {
  User.find({}, function(err, users) {
    // This is the method that finds all of the users from the database
    // Notice how the first parameter is the options for what to find and the second is the
    //   callback function that has an error (if any) and all of the users
    // Keep in mind that everything you want to do AFTER you get the users from the database must
    //   happen inside of this callback for it to be synchronous
    // Make sure you handle the case when there is an error, as well as the case when there is no error
  })
})
// Add User Request
mongoose.Promise = global.Promise;
app.post('/users', function(req, res) {
  console.log("POST DATA", req.body);
  // create a new User with the name and age corresponding to those from req.body
  var user = new User({name: req.body.name, age: req.body.age});
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  user.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err){
        res.render('index', {title: 'you have errors!', errors: user.errors})
    }
    else {
        res.redirect('/users');
    }
  })
})
// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
