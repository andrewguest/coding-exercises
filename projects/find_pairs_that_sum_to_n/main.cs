using System.Collections.Generic;
using System.Linq;


int[] exampleList = [1, 2, 6, 8, 9, 11, 13, 14, 23, 26];
int exampleN = 15;


static List<Tuple<int, int>> findPairs(int[] inputList, int n)
{
    // Used to keep track of numbers we've iterated over
    List<int> seenNumbers = [];

    // List of 2 numbers that add up to `n`
    List<Tuple<int, int>> resultPairs = [];

    for (int i = 0; i < inputList.Length; i++)
    {
        int number = inputList[i];

        // Subtract the current number from `n` and save the difference
        int remainingValue = n - number;

        /*
        Check if the difference is in `seenNumbers` and if it is then these two numbers are a pair and
        should be added to `resultPairs` as a Tuple.
        */
        if (seenNumbers.Contains(remainingValue))
        {
            resultPairs.Add(Tuple.Create(number, remainingValue));
        }

        seenNumbers.Add(number);
    }

    return resultPairs;
}

// Get the results for the given list and given N
List<Tuple<int, int>> pairs = findPairs(exampleList, exampleN);

// Print the results
foreach (Tuple<int, int> pair in pairs)
{
    Console.WriteLine(pair.ToString());
}
