function Reverse(arr) {
  temp = [];
  for (var i = arr.length-1; i >= 0; i--) {
    temp.push(arr[i])
  }
  return temp;
}
arr = [1,2,3,4,5,6,7,8]
a = Reverse(arr)
console.log(a)

function Find(arr, arg) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === arg) {
      return i
    }
  }
  return "bariable not found"
}

console.log(Find(arr, 13))

function insert(arr, arg, val) {
  temp = [];
  for (var i = 0; i < arg; i++) {
    temp.push(arr[i])
  }
  temp[arg] = val;
  for (var i = arg; i < arr.length; i++) {
    temp.push(arr[i])
  }
  return temp
}

console.log(insert(arr, 4, 276));
