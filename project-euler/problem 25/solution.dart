void main(List<String> args) {
  List<BigInt> fibonacciSequence = [BigInt.from(1), BigInt.from(1)];

  while (fibonacciSequence.last.toString().length != 1000) {
    fibonacciSequence.add(fibonacciSequence[fibonacciSequence.length - 1] +
        fibonacciSequence[fibonacciSequence.length - 2]);
  }

  print(fibonacciSequence.length);
}
