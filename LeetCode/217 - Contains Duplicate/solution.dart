void main(List<String> args) {
  bool result = containsDuplicate([1, 2, 3]);

  print(result);
}

bool containsDuplicate(List<int> nums) {
  /*
    Check the length of `nums` as a list to the length of `nums` as a set.
    If there's a difference that means there were duplicates in the list
      version and we return the opposite boolean, because duplicates are
      a good thing in this problem.
  */
  bool result = nums.length == nums.toSet().length;

  return !result;
}
