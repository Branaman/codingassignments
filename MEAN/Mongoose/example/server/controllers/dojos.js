var mongoose = require('mongoose')
var Dojo = mongoose.model('dojo')

module.exports = {
  index: function(req, res){
    var dojos = Dojo.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
  show: function(req,res){
      var dojos = Dojo.findOne({_id:req.params.id}, function(err,data){
        if (err) {
          res.json (err);
          return;
        }
        res.json(data);
      });
  },
  create: function(req, res){
    var dojo = new Dojo(req.body);
    dojo.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      res.json(data);
    });
  }
}
