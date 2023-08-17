import 'package:more/collection.dart';

const list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const index = 1000000;

void main() {
  final permutation = list.permutations().elementAt(index - 1).join();

  print(permutation);
}
