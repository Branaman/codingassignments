function bDaycountdown(daysUntilMyBirthday) {
  var string1;
  if (daysUntilMyBirthday > 30) {
    string1 = daysUntilMyBirthday+" days until your birthday.... no gifts anytime soon...";
  }else if (daysUntilMyBirthday < 30, daysUntilMyBirthday > 5) {
    string1 = daysUntilMyBirthday+" days until your birthday.... its coming up pretty quick...";
  }else if (daysUntilMyBirthday < 5, daysUntilMyBirthday != 0) {
    string1 = daysUntilMyBirthday+" days until your birthday. ALMOST TIME FOR SOME CAKE!!";
  }else if (daysUntilMyBirthday === 0) {
    string1 = "ITS YOUR FRICKING BIRTHDAY!!!!!!";
  }
  return string1;
}
