var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var messageSchema= new mongoose.Schema({
    name:{type:String},
    message: {type: String, required: true },
    comments: [{
        name:{type:String},
        comment: {type: String, required: true },
      }],
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('message', messageSchema);
