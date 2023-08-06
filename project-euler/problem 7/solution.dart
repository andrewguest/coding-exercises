import 'dart:math';

void main() {
  // Number of primes found
  int count = 1;

  // Most recently found prime number
  int lastPrimeFound = 2;

  while (count < 10001) {
    lastPrimeFound += 1;

    if (isPrime(lastPrimeFound)) {
      count += 1;
    }
  }

  print("The 10,001st prime is: $lastPrimeFound");
}

bool isPrime(int number) {
  for (var i = 2; i <= number / i; i++) {
    if (number % i == 0) {
      return false;
    }
  }

  return true;
}
