void main() {
  List<int> listOfDigits = [];

  BigInt raisedNumber = BigInt.from(2).pow(1000);
  String raisedNumberString = raisedNumber.toString();

  for (var digit in raisedNumberString.split('')) {
    listOfDigits.add(int.parse(digit));
  }

  int sumOfDigits = listOfDigits.reduce((a, b) => a + b);
  print(sumOfDigits);
}
