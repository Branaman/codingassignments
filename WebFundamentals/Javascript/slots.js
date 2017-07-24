// Let's play the slots!
//
// Make a function that takes a number of quarters (1 quarter = 1 game).
//
// There is a 1 in 100 chance to win the slot machine (which will give you between 50 - 100 quarters -- use Math.random and Math.floor to pick a random number of coins).
//
// While the user still has quarters, use Math.random to determine if they won.
//
// If they ever win, return the number of quarters (ex: they had 50 remaining quarters and won 90, so it should return 140).
//
// Return 0 if all the quarters were wasted.
//
// Bonus (Only If You Have Time):
//
// Let the user pass the number they are willing to leave with
// (ex: If they won the lottery and still have 40 coins, they will keep playing until they have collected 200 coins)
function rdx() {
  var result = 0;
  result = Math.floor(Math.random()*100);
  return result
}
function winner(output) {
  var winnings = 0;
  if (output===7) {
    winnings = (Math.floor(Math.random()*50)+50);
    console.log("JACKPOT!!!");
    console.log(winnings+" quarters pour out of the machine...")
    return winnings
}
  console.log("Not this time :()");
  return 0
}
function slots(quarters, min, max) {
  var cashout=0;
  for (var i = quarters; i>min; i--) {
    console.log(i+" quarters remaining");
    console.log("Insert 1 quarter and pull the lever.")
    i = i+winner(rdx());
    if (i>max){
      break;
    }
  }
  return "You left with "+i+" quarters.";
}
