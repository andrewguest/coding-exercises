class Solution {
  List<int> twoSum(List<int> nums, int target) {
    var seen = Map<int, int>();

    for (int i = 0; i < nums.length; i++) {
      int remaining = target - nums[i];

      if (seen.keys.contains(remaining)) {
        return [i, seen[remaining] ?? 0];
      }

      seen[nums[i]] = i;
    }

    return [];
  }
}

void main() {
  var s = Solution();

  print(s.twoSum([1, 2, 3, 4], 7));
}
