var mongoose = require('mongoose')
var Message = mongoose.model('message')

module.exports = {
  index: function(req, res){
    var messages = Message.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.render("index", {messages: data});
    });
  },
  create: function(req, res){
    console.log(req.body);
    var message = new Message(req.body);
    message.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      res.redirect("/");
    });
  },
  comment: function(req, res) {
    Message.findOne({_id: req.params._id}, function(err, message){
      var comment = req.body;
      message.comments.push(comment);
      message.save(function(err){
          if(err) { console.log('Error'); }
          else { res.redirect('/'); }
      });
    });
  },
}
