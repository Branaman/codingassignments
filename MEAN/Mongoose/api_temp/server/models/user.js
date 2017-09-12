//basic model
var mongoose = require('mongoose');
var validator = require('validator');
var userSchema= new mongoose.Schema({
  name:{type: String, required: [true, 'Name is required']},
  username:{type: String, required: [true, 'userName is required']},
  // email:{type: String, validate: {
  //         validator: validator.isEmail(v),
  //         message: '{VALUE} is not a valid email!'
  //       },
  //       required: [true, 'email is required']
  //     },
  address:{},
  phone:{
        type: String,
        validate: {
          // `isAsync` is not strictly necessary in mongoose 4.x, but relying
          // on 2 argument validators being async is deprecated. Set the
          // `isAsync` option to `true` to make deprecation warnings go away.
          isAsync: true,
          validator: function(v, cb) {
            setTimeout(function() {
              var phoneRegex = /\d{3}-\d{3}-\d{4}/;
              var msg = v + ' is not a valid phone number!';
              // First argument is a boolean, whether validator succeeded
              // 2nd argument is an optional error message override
              cb(phoneRegex.test(v), msg);
            }, 5);
          },
          // Default error message, overridden by 2nd argument to `cb()` above
          message: 'Default error message'
        },
        required: [true, 'User phone number required']
      },
  website:String,
  company:{},
  posts:Array,
  accountHistory:{},
}, { timestamps: { createdAt: 'created_at', updatedAt: 'updated_at' } });

mongoose.model('users', userSchema);
/*
types:
var schema = new Schema({
  name:    String,
  binary:  Buffer,
  living:  Boolean,
  updated: { type: Date, default: Date.now },
  age:     { type: Number, min: 18, max: 65 },
  mixed:   Schema.Types.Mixed,
  _someId: Schema.Types.ObjectId,
  array:      [],
  ofString:   [String],
  ofNumber:   [Number],
  ofDates:    [Date],
  ofBuffer:   [Buffer],
  ofBoolean:  [Boolean],
  ofMixed:    [Schema.Types.Mixed],
  ofObjectId: [Schema.Types.ObjectId],
  nested: {
    stuff: { type: String, lowercase: true, trim: true }
  }
})
required validator examples:
var s = new Schema({ born: { type: Date, required: true })
var s = new Schema({ born: { type: Date, required: 'Born is required!' })
custom validation:
(for more see http://mongoosejs.com/docs/validation.html)
function validator (val) {
  return val == 'something';
}
new Schema({ name: { type: String, validate: validator }});
// with a custom error message
var custom = [validator, 'Uh oh, {PATH} does not equal "something".']
new Schema({ name: { type: String, validate: custom }});
// adding many validators at a time
var many = [
  { validator: validator, msg: 'uh oh' }
, { validator: anotherValidator, msg: 'failed' }
]
new Schema({ name: { type: String, validate: many }});
unique:
var s = new Schema({ name: { type: Date, unique: true })
returns an E11000 error not validation error
customize return using get:
function obfuscate (cc) {
  return '****-****-****-' + cc.slice(cc.length-4, cc.length);
}
var AccountSchema = new Schema({
  creditCardNumber: { type: String, get: obfuscate }
});
*/
