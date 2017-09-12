var mongoose = require('mongoose');
var taskCrontroller = require('../controllers/task.js');
module.exports = (function(app){
  app.get('/tasks', taskCrontroller.index);
  app.post('/tasks', taskCrontroller.create);
  app.get('/tasks/:id', taskCrontroller.show);
  app.delete('/tasks/:id', taskCrontroller.destroy);
  app.put('/tasks/:id', taskCrontroller.update);
});
