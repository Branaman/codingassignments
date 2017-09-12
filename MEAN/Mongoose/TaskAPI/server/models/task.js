var mongoose = require('mongoose');

var taskSchema= new mongoose.Schema({
    id:{type: Number},
    title:{type:String},
    description:{type:String},
    completed:{type:Boolean},
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('task', taskSchema);
