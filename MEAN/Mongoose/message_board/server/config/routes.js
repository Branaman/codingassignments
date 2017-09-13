var mongoose = require('mongoose');
var messagesCrontroller = require('../controllers/messages.js');
module.exports = (function(app){
  app.get('/', messagesCrontroller.index);
  app.post('/messages', messagesCrontroller.create);
  app.post('/messages/:_id', messagesCrontroller.comment);
});
