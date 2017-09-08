module.exports = {
    add: function(num1, num2) {
         console.log(num1 + num2);
    },
    multiply: function(num1, num2) {
         console.log(num1 * num2);
    },
    square: function(num) {
         console.log(num*num);
    },
    random: function(num1, num2) {
         console.log(Math.floor((num2 - num1 + 1) * Math.random())+num1);
    }
}
