BigInt customPow(int base, int exponent) {
  /*
  Implement a custom function that raises a number (base) to a
    value (exponent) and returns the result.
  */
  BigInt result = BigInt.one;

  for (int i = 0; i < exponent; i++) {
    result *= BigInt.from(base);
  }

  return result;
}

main(List<String> args) {
  int a = 2;
  List<BigInt> multiples = [];

  while (a <= 100) {
    for (var i = 2; i <= 100; i++) {
      BigInt result = customPow(a, i);

      if (multiples.contains(result) == false) {
        multiples.add(result);
      }
    }
    a += 1;
  }

  print(multiples.length);
}
