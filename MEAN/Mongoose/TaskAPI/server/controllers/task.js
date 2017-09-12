var mongoose = require('mongoose')
var Task = mongoose.model('task')

module.exports = {
  index: function(req, res){
    var tasks = Task.find({}, function (err,data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
  show: function(req,res){
      var tasks = Task.findOne({id:req.params.id}, function(err,data){
        if (err) {
          res.json (err);
          return;
        }
        res.json(data);
      });
  },
  create: function(req, res){
    var task = new Task(req.query);
    task.save(function (err, data){
      if (err) {
        res.json(err);
        return;
      }
      res.json(data);
    });
  },
  destroy: function(req, res) {
    Task.remove({id:req.params.id}, function(err, data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
  update: function(req, res) {
    Task.update({id:req.params.id}, req.query, function(err, data){
      if (err) {
        res.json (err);
        return;
      }
      res.json(data);
    });
  },
}
