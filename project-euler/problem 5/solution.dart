void main() {
  var smallestMultiple = 1;

  for (var i = 1; i < 21; i++) {
    smallestMultiple *= (i / i.gcd(smallestMultiple)).floor();
  }

  print(smallestMultiple);
}
