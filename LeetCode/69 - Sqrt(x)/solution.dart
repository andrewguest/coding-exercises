class Solution {
  int mySqrt(int x) {
    var left = 0;
    var right = x;

    while (left <= right) {
      var mid = ((left + right) / 2).floor();

      if ((mid * mid) <= x) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return left - 1;
  }
}
