var mongoose = require('mongoose');

var quoteSchema= new mongoose.Schema({
    name:{type:String},
    quote:{type:String},
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('quote', quoteSchema);
