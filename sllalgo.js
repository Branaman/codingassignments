function sll(val) {
  next:val
}
function node(val){
  value:val,
  next:null,
}

jim = sll(node(2));
console.log(jim);

function add(sll) {
  curr = sll['next'];
  while (curr.next != null) {
    curr = curr.next;
  }
}
