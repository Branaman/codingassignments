var mongoose = require('mongoose')
var Choopa = mongoose.model('choopa')

module.exports = {
  index: function(req, res){
    var choopas = Choopa.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.render("choopas", {choopas: data});
    });
  },
  show: function(req,res){
      var choopas = Choopa.findOne({_id:req.params._id}, function(err,data){
        if (err) {
          res.json (err);
          return;
        }
        res.json(data);
      });
  },
  create: function(req, res){
    console.log(req.body);
    var choopa = new Choopa(req.body);
    choopa.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      // res.json(data);
      res.render("success");
    });
  },
  destroy: function(req, res) {
    Choopa.remove({_id:req.params._id}, function(err, data){
      if (err) {
        res.json (err);
        return;
      }
      res.redirect('/');
    });
  },
  edit: function(req, res) {
    Choopa.update({_id:req.params._id}, req.body, function(err, data){
      if (err) {
        res.json (err);
        return;
      }
      res.redirect('/');
    });
  },
}
