var world = [
  [2,2,2,2,2,2,2,2,2,2,2,2,2],
  [2,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,1,1,3,1,1,1,1,1,1,1,1,2],
  [2,1,1,1,1,1,2,2,2,2,2,1,2],
  [2,1,1,2,2,2,2,1,1,1,1,1,2],
  [2,1,1,1,1,1,2,2,2,2,2,1,2],
  [2,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2]

]
function displayWorld() {
  var output = '';
  for(var i=0; i<world.length;i++){
    for (var j = 0; j < world[i].length; j++) {
      if(world[i][j] == 2)
        output += "\n\t<div class='brick'></div>";
      if(world[i][j] == 1)
        output += "\n\t<div class='coin'></div>";
      if(world[i][j] == 3)
        output += "\n\t<div class='poro'></div>";
        output = output + world[i][j];
    }
    output += "\n</div>";
  }
  console.log(output);
  document.getElementById('world').innerHTML = output;
}
