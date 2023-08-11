void main(List<String> args) {
  final factorialOfOneHundred = factorial(100);
  String stringFactorial = factorialOfOneHundred.toString();
  int summedFactorial = 0;

  for (var i = 0; i < stringFactorial.length; i++) {
    summedFactorial += int.parse(stringFactorial[i]);
  }

  print(summedFactorial);
}

BigInt factorial(int n) {
  if (n == 0 || n == 1) {
    return BigInt.one;
  }

  BigInt result = BigInt.from(n);

  for (int i = n - 1; i >= 1; i--) {
    result *= BigInt.from(i);
  }

  return result;
}
