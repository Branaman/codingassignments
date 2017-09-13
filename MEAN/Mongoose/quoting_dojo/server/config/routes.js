var mongoose = require('mongoose');
var quotesCrontroller = require('../controllers/quotes.js');
module.exports = (function(app){
  app.get('/quotes', quotesCrontroller.index);
  app.post('/quotes', quotesCrontroller.create);
  app.get('/', function(req, res) {
    res.render("form");
  });
});
