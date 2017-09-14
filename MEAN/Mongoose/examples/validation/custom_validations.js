// require express and path
var express = require("express");
var path = require("path");
// create the express app
var app = express();
// require bodyParser since we need to handle post data for adding a user
var bodyParser = require("body-parser");
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/validation');
var QuoteSchema = new mongoose.Schema({
  name: {
    first: {
      type: String,
      required: [true, "this is for something else"],
      trim: true,
    },
    last: {
      type: String,
      required: true,
      trim: true
    },
  },
  phone: {
    type: String,
    validate: [{
      validator: function( number ) {
        return /\d{3}-\d{3}-\d{4}/.test( number );
      },
      message: "{ VALUE } is not a valid phone number"
    },
  ],
    required: [true, "Customer phone number required"]
  },
  gender: {
    type: String,
    enum: ['MALE', 'FEMALE'],
    uppercase: true,
    trim: true,
    default: "MALE"
  },
  age: {
    type: Number,
    min: [18, "Maybe you need to be a little older"],
    max: [85, "You might want to be enjoying your retirement rather than using this site"],
    required: true
  },
  password: {
    type: String,
    required: true,
    minlength: 8,
    maxlength: 32,
    validate: {
      validator: function( value ) {
        return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,32}/.test( value );
      },
      message: "Password failed validation, you must have at least 1 number, uppercase and special character"
    }
  },
  pets: {
    type: [{
      type: mongoose.Schema.Types.ObjectId,
      ref: "Pet"
    }],
    default: []
  }
  }, {
  timestamps: {
    createdAt: 'created_at',
    updatedAt: 'updated_at'
  }
});
var Quote = mongoose.model('Quote', QuoteSchema);
app.use(bodyParser.urlencoded({ extended: true }));
// static content
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view
app.get('/', function(req, res) {
  res.render("index");
})
app.post('/quotes', function(req,res){
  var quote = new Quote(req.query);
  quote.save(function(err) {
    if(err){
      console.log("something went wrong:"+err);
      res.json(err);
    } else {
      res.redirect('/main');
    }
  })
})
app.get('/main', function (req, res) {
  Quote.find({}, function (err, quotes){
    res.render('main', {quotes:quotes});
  });
})
// tell the express app to listen on port 8000
app.listen(8000, function() {
  console.log("listening on port 8000");
})
