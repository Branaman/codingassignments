var express=require('express'),
app = express(),
path = require('path');
var bodyparser = require('body-parser');

app.use(bodyparser.urlencoded({extended:true}));
app.use(bodyparser.json());
app.set('views', path.join(__dirname, './server/views'));
app.set('view engine', 'ejs');

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);

app.listen(8000, function() {});
