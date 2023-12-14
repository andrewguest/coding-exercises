void main(List<String> args) {
  int largestPrimeFactor = primeFactor(600851475143);

  print(largestPrimeFactor);
}

int primeFactor(int number) {
  int largestFactor = 1;
  int c = number;
  int i = 2;

  while (c > 1) {
    if (c % i == 0) {
      largestFactor = i;
      c = (c / i).floor();
    }
    i += 1;
  }

  return largestFactor;
}
