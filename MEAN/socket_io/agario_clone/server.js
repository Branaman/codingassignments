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
  // socket.on( "user_registered", function(data){
  //   socket.user_name = data.user_name
  //   let clients = io.sockets.sockets;
  //   let response = [];
  //   for (var sockets in clients) {
  //     for (var thingys in clients[sockets]) {
  //       if (thingys === "user_name") {
  //         let objy = {};
  //         if (socket.id === sockets) {
  //           objy.user = true;
  //         }
  //         else {
  //           objy.user = false;
  //         }
  //           objy.id = sockets;
  //         objy.user_name = clients[sockets][thingys];
  //         response.push(objy);
  //       }
  //     }
  //   }
  //   socket.emit('all_sockets', {clients: response});
  //   socket.broadcast.emit('user_joined', {id: socket.id, user_name: data.user_name});
  // })
  // socket.on('disconnect', function() {
  //     io.emit('disconnect_event', {id: socket.id, user_name: socket.user_name});
  //  });
  // socket.on( "sent_msg", function (data){
  //   io.emit( 'new_msg', {msg: data.chat, id: socket.user_name});
  // })
})
