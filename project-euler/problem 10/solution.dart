void main(List<String> args) {
  List<int> primeNumbers = [];
  int number = 2;

  while (number < 2000000) {
    if (isPrime(number)) {
      primeNumbers.add(number);
    }
    number += 1;
  }

  int sumOfPrimes =
      primeNumbers.fold(0, (previousValue, element) => previousValue + element);
  print(sumOfPrimes);
}

bool isPrime(int number) {
  for (var i = 2; i <= number / i; i++) {
    if (number % i == 0) {
      return false;
    }
  }

  return true;
}
