void main() {
  int largestPalindrome = 0;
  int number = 100;

  // `number` is the first number to multiply
  // `i` is the second number to multiply
  while (number <= 999) {
    for (var i = 100; i < 1000; i++) {
      // Convert the integer to a String and reverse it to check if it's a palindrome
      if ((number * i) > largestPalindrome &&
          (number * i).toString().split("").reversed.join() ==
              (number * i).toString()) {
        largestPalindrome = number * i;
      }
    }

    // Increment `number` by 1
    number += 1;
  }

  print(largestPalindrome);
}
