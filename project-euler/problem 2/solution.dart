void main() {
  // All Fibonacci numbers
  List<int> fibonacciNumbers = [1, 2];
  // Even Fibonacci numbers
  List<int> evenFibonacciNumbers = [];

  // Find the Fibonacci numbers equal to or less than 4,000,000
  while ((fibonacciNumbers[fibonacciNumbers.length - 1] +
          fibonacciNumbers[fibonacciNumbers.length - 2]) <=
      4000000) {
    // Add the new Fibonacci number to the existing sequence
    fibonacciNumbers.add(fibonacciNumbers[fibonacciNumbers.length - 1] +
        fibonacciNumbers[fibonacciNumbers.length - 2]);
  }

  // Filter out the odd Fibonacci numbers
  for (var i = 0; i < fibonacciNumbers.length; i++) {
    if (fibonacciNumbers[i].remainder(2) == 0) {
      evenFibonacciNumbers.add(fibonacciNumbers[i]);
    }
  }

  print(evenFibonacciNumbers.reduce((a, b) => a + b));
}
