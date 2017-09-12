var mongoose = require('mongoose')
var Fiftyfiver = mongoose.model('fiftyfiver')

module.exports = {
  index: function(req, res){
    var fiftyfivers = Fiftyfiver.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
  show: function(req,res){
      var fiftyfivers = Fiftyfiver.findOne({name:req.params.name}, function(err,data){
        if (err) {
          res.json (err);
          return;
        }
        res.json(data);
      });
  },
  create: function(req, res){
    var fiftyfiver = new Fiftyfiver({name:req.params.name});
    fiftyfiver.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      res.json(data);
    });
  },
  destroy: function(req, res) {
    Fiftyfiver.remove({name:req.params.name}, function(err, data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
}
