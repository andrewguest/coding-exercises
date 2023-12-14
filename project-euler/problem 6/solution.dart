import 'dart:math';

void main() {
  num sumOfSquares = SumOfSquare(1, 100);
  num squareOfSums = SquareOfSums(1, 100);

  print(squareOfSums - sumOfSquares);
}

num SumOfSquare(int startNumber, int endNumber) {
  /*
  Square all of the numbers from startNumber to endNumber then
    sum all the squared numbers together.

  1^2 + 2^2 + 3^2 ...
  */

  num total = 0;

  for (var i = startNumber; i <= endNumber; i++) {
    total += pow(i, 2);
  }

  return total;
}

num SquareOfSums(int startNumber, int endNumber) {
  /*
  Sum all of the numbers from startNumber to endNumber then
    square the summed number.

  (1 + 2 + 3 ...)^2
  */
  num total = 0;

  for (var i = startNumber; i <= endNumber; i++) {
    total += i;
  }

  return pow(total, 2);
}
