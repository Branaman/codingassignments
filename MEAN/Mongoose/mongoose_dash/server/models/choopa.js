var mongoose = require('mongoose');

var choopaSchema= new mongoose.Schema({
    name:{type:String},
    fav_color:{type:String},
    fur:{type:String},
    spikes:{type:Number},
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('choopa', choopaSchema);
