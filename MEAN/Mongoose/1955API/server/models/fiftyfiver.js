var mongoose = require('mongoose');

var fiftyfiverSchema= new mongoose.Schema({
    name:{type:String},
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('fiftyfiver', fiftyfiverSchema);
