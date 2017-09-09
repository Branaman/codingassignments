var express = require("express");
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');
app.use(session({secret: 'codingdojorocks'}));  /
app.use(bodyParser.urlencoded({extended: true}));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.static(__dirname + "/static"));
app.listen(8000, function(){
  console.log("listening on port 8000!");
})
app.get("/users", function (request, response){
    var users_array = [
        {name: "Michael", email: "michael@codingdojo.com"},
        {name: "Jay", email: "jay@codingdojo.com"},
        {name: "Brendan", email: "brendan@codingdojo.com"},
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    response.render('users', {users: users_array});
})
app.get('/', function (req, res){
  res.render('index', {title: "my Express project"});
});
// route to process new user form data:
app.post('/users', function (req, res){
    req.session.name = req.body.name;
    console.log(req.session.name);
    console.log("POST DATA \n\n", req.body)
    //code to add user to db goes here!
    // redirect the user back to the root route.
    res.redirect('/')
});
app.get("/users/:id", function (req, res){
    console.log("The user id requested is:", req.params.id);
    // just to illustrate that req.params is usable here:
    res.send("You requested the user with id: " + req.params.id);
    // code to get user from db goes here, etc...
});
