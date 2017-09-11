var express = require("express");
var app = express();
var path = require("path");
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// Have the server render views/index.ejs that has the form for the user to fill out
app.get('/', function(req, res) {
  res.render("survey");
})
// The user fills out the form and submits
app.post('/results', function(req, res){
  console.log("POST DATA", req.body);
  res.render("results", req.body)
})
// The form information is EMITTED to the server with the event name "posting_form"
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);
// The server listens for an event 'posting_form' and when this event gets triggered, organizes all the emitted information to form a single message and sends this single message with the event called 'updated_message'. It also EMITs an event called 'random_number' with random number between 1-1000.
io.sockets.on('connection', function (socket) {
  console.log("Client/socket is connected!");
  console.log("Client/socket id is: ", socket.id);
  socket.on( "posting_form", function (data){
    rando = Math.floor(Math.random()*1001);
    socket.emit( 'updated_message', {response:  'You emitted the following information: Name: '  + data.name + ' Location: '  + data.location+ ' fav_lang: '  + data.fav_lang+ ' Comments: '  + data.comments + " Your Lucky number is! "+ rando});
  })
})
// The client listens for an event called 'random_number' and when this event gets triggered, shows the number in the HTML.
// The client listens for an event called 'updated_message' and when this event gets triggered, displays the message somewhere in the HTML
