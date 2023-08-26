class Solution {
  String addBinary(String a, String b) {
    String sum = "";
    int i = a.length - 1, j = b.length - 1, c = 0;
    while (i >= 0 || j >= 0 || c > 0) {
      if (i >= 0) c += int.parse(a[i--]);
      if (j >= 0) c += int.parse(b[j--]);
      sum = (c % 2).toString() + sum;
      c = c ~/ 2;
    }

    return sum;
  }
}
