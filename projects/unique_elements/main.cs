using System;
using System.Linq;
using System.Collections.Generic;


class Program
{
    static void Main()
    {
        int[] inputList = [3, 5, 8, 12, 22, 12, 3, 18, 3, 20];

        // Easy
        // Use the built-in Distinct() method
        IEnumerable<int> uniqueList = inputList.Distinct();
        foreach (int number in uniqueList)
        {
            Console.WriteLine(number);
        }


        Console.WriteLine("\n\n");


        // Hard(er)
        // Manually find the unique values
        List<int> uniqueValues = new List<int>();

        for (int i = 0; i < inputList.Length; i++)
        {
            if (uniqueValues.Contains(inputList[i]) == false)
            {
                uniqueValues.Add(inputList[i]);
            }
        }
        for (int i = 0; i < uniqueValues.Count; i++)
        {
            Console.WriteLine(uniqueValues[i]);
        }
    }
}
