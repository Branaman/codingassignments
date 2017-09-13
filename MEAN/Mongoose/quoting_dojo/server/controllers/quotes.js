var mongoose = require('mongoose')
var Quote = mongoose.model('quote')

module.exports = {
  index: function(req, res){
    var quotes = Quote.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.render("quotes", {quotes: data});
    });
  },
  create: function(req, res){
    var quote = new Quote(req.body);
    quote.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      res.redirect('/quotes');
    });
  },
}
