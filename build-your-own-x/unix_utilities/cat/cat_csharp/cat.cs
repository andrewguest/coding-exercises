using System;

class Cat
{
    public static void Main()
    {
        Console.WriteLine();
        //  Invoke this sample with an arbitrary set of command line arguments.
        string[] arguments = Environment.GetCommandLineArgs();
        Console.WriteLine("GetCommandLineArgs: {0}", string.Join(", ", arguments));
    }
}
