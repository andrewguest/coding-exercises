using System;

public class Program
{
    public static void Main()
    {
        // Starting string that will be reversed
        string sentence = "Never underestimate the willingness of the greedy to throw you under the bus";

        // Split the sentence into words based on the space character
        string[] words = sentence.Split(' ');

        // Reverse the order of the list of words
        Array.Reverse(words);

        // Create an empty string as a placeholder for the reversed string
        string reversedSentence = "";

        // Loop through each word in the reversed list of words
        foreach (string word in words)
        {
            // Append a space and the current word to the placeholder reversed string
            reversedSentence += " " + word;
        }

        // Trim any leading or trailing spaces from the reversed string
        reversedSentence = reversedSentence.Trim();

        // Print the results
        Console.WriteLine(sentence);
        Console.WriteLine("Becomes:");
        Console.WriteLine(reversedSentence);

    }
}