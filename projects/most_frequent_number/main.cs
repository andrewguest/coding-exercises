using System.Collections.Generic;
using System.Linq;


int[] randomNumbers = { 5, 2, 8, 5, 1, 2, 9, 3, 8, 4 };
Dictionary<int, int> numbersFrequency = new Dictionary<int, int>();

foreach (int num in randomNumbers.Distinct())
{
    int currentCount = randomNumbers.Count(n => n == num);
    numbersFrequency[num] = currentCount;
}

// Max frequency
int maxFrequency = numbersFrequency.Values.Max();

// Get all keys from numbersFrequency where their value equals maxFrequency
List<int> keys = numbersFrequency.Where(kv => kv.Value == maxFrequency).Select(kv => kv.Key).ToList();
// Sort the keys in ascending order
keys.Sort();

Console.WriteLine("Most frequent number(s): " + string.Join(", ", keys));
Console.WriteLine("Frequency: " + maxFrequency);
