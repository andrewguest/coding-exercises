void main() {
  // Array to contain the numbers that are multiples of 3 or 5
  List<int> multiples = [];

  // Loop through each number 1-999
  for (var i = 1; i < 1000; i++) {
    // If $i is evenly divisible by 3 or 5
    if ((i.remainder(3) == 0) || (i.remainder(5) == 0)) {
      // Append it to the $multiples array
      multiples.add(i);
    }
  }

  // Print the sum of all found multiples
  print(multiples.reduce((a, b) => a + b));
}
