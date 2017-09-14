var mongoose = require('mongoose');

var dojoSchema= new mongoose.Schema({
    location:{type:String}
  }, { timestamps: { createdAt: 'created_at', updatedAt:'updated_at'}
});
mongoose.model('dojo', dojoSchema);
