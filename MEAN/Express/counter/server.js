var express = require("express");
var app = express();
var session = require('express-session');
var path = require("path");
var bodyParser = require('body-parser');
app.use(session({secret: 'codingdojorocks'}));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.get('/', function(req, res) {
  if (!req.session.count) {
    req.session.count = 0;
  }
  req.session.count++;
  var sescount = req.session.count;
  console.log(req.session.count);
  res.render("index", {"count": sescount});
})
app.get('/2', function(req, res) {
  if (!req.session.count) {
    req.session.count = 0;
  }
  req.session.count+=2;
  var sescount = req.session.count;
  console.log(req.session.count);
  res.render("index", {"count": sescount});
})
app.get('/reset', function(req, res) {
 req.session.count = 0;
 res.redirect('/');
})
app.listen(8000, function() {
 console.log("listening on port 8000");
});
