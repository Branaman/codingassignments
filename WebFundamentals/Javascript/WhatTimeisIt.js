function telltime(HOUR, MINUTE, PERIOD) {
  var String1
  if (PERIOD=='AM') {
    String1 = "in the morning";
  }
    else if (PERIOD=='PM') {
      String1 = "in the evening";
    }
      else {
        String1 = "not sure if its day or night";
  }
  return HOUR + ':' + MINUTE + String1;
}
