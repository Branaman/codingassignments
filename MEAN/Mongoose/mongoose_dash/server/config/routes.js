var mongoose = require('mongoose');
var choopasCrontroller = require('../controllers/choopas.js');
module.exports = (function(app){
  app.get('/', choopasCrontroller.index);
  app.post('/choopas', choopasCrontroller.create);
  app.get('/choopas/new', function(req, res) {
    res.render("form");
  });
  app.get('/choopas/edit/:_id', function(req, res) {
    res.render("edit_form", {id:req.params._id});
  });
  app.post('/choopas/edit/:_id', choopasCrontroller.edit);
  app.get('/choopas/:_id', choopasCrontroller.show);
  app.get('/choopas/destroy/:_id', choopasCrontroller.destroy);
});
