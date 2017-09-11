var express = require("express");
var app = express();
app.set('view engine', 'ejs');
app.get('/', function(req, res) {
  res.render("index");
})
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);
io.sockets.on('connection', function (socket) {
  socket.on( "clicked_button", function (){
    socket.emit( 'updated_message', {response: "clicked"});
  })
  socket.on( "reset_button", function (){
    io.emit( 'reset_message', {response: "reset"});
  })
})
