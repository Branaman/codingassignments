var mongoose = require('mongoose');
var dojosCrontroller = require('../controllers/dojos.js');
var usersCrontroller = require('../controllers/users.js');
//************RESTful routes for users************
module.exports = (function(app){
  app.get('/', function(req,res){
    res.json({key:'value'});
  })
  app.get('/users', usersCrontroller.index);
  app.post('/users', usersCrontroller.create);
  app.get('/users/:_id', usersCrontroller.show);
  app.get('/dojos', dojosCrontroller.index);
  app.post('/dojos', dojosCrontroller.create);
  app.get('/dojos/:_id', dojosCrontroller.show);
  // app.post('/users', Users.create);
  // app.put('/users/:id', Users.update);
  // app.delete('/users/:id', Users.delete);
});
//************END routes for users****************
