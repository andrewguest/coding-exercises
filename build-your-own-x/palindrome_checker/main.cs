using System.Collections.Generic;
using System.Linq;


string exampleInput = "racecar";

static bool isPalindrome(string inputWord)
{
    return inputWord == String.Join("", inputWord.Reverse());
}


if (isPalindrome(exampleInput))
{
    Console.WriteLine($"{exampleInput} is a palindrome");
}
else
{
    Console.WriteLine($"{exampleInput} is NOT a palindrome");
}
