// Students and Instructors
// Part I
//
// Given the following array of objects:
//
// var students = [
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
// ]
// Create a program that outputs:
//
// Michael Jordan
// John Rosales
// Mark Guillen
// KB Tonel
// Part II (Optional)
//
// Now, given the following dictionary:
//
// var users = {
//  'Students': [
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
//   ],
//  'Instructors': [
//      {first_name : 'Michael', last_name : 'Choi'},
//      {first_name : 'Martin', last_name : 'Puryear'}
//   ]
//  }
// Create a program that prints  the following format (including the number of characters in each combined name):
//
// Students
// 1 - MICHAEL JORDAN - 13
// 2 - JOHN ROSALES - 11
// 3 - MARK GUILLEN - 11
// 4 - KB TONEL - 7
// Instructors
// 1 - MICHAEL CHOI - 11
// 2 - MARTIN PURYEAR - 13

var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]
for (var i = 0; i < students.length; i++) {
  console.log(students[i].first_name+" "+students[i].last_name);
}
var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
for (var key in users) {
  var userType = key;
  console.log(userType.toUpperCase());
  var userList = users[userType];
  for (var i = 0; i < userList.length; i++) {
    var peep = userList[i];
    var num = i+1;
    var name = peep.first_name + ' ' + peep.last_name;
    var namelength = name.length - 1;
    console.log(num+' - '+name+' - '+namelength);
  }
}
