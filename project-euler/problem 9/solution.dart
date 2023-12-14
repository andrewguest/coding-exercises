void main() {
  for (var a = 1; a < 1000; a++) {
    for (var b = 1; b < 1000; b++) {
      for (var c = 1; c < 1000; c++) {
        /*
        Once we have an iteration of a, b, and c
        Determine if it fits the criteria of a+b+c==1000 and
          a^2 + b^2 == c^2
        Test a+b+c first because it is a faster test.  Takes ~half the time
        */
        if (a + b + c == 1000) {
          if ((a * a) + (b * b) == (c * c)) {
            print(a * b * c);
          }
        }
      }
    }
  }
}
