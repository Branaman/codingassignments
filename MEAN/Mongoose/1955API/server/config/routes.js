var mongoose = require('mongoose');
var fiftyfiverCrontroller = require('../controllers/fiftyfiver.js');
module.exports = (function(app){
  app.get('/', fiftyfiverCrontroller.index);
  app.get('/new/:name', fiftyfiverCrontroller.create);
  app.get('/:name', fiftyfiverCrontroller.show);
  app.get('/remove/:name', fiftyfiverCrontroller.destroy);
});
