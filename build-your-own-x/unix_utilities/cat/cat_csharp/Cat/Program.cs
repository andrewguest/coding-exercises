// See https://aka.ms/new-console-template for more information
using System;
using System.IO;


class Cat
{
    public static void Main()
    {
        // Get all command line arguments
        string[] arguments = Environment.GetCommandLineArgs();

        // If no filename was passed in as a command line argument, then print a message
        if (arguments.Length < 2)
        {
            // Throw a custom exception if no command line arguments were provided.
            throw new NoFileNameProvidedException();
        }
        else
        {
            string filename = arguments[1];

            // If `filename` is a valid file
            if (File.Exists(filename))
            {
                try
                {
                    using (StreamReader sr = new StreamReader(filename))
                    {
                        string line;
                        while ((line = sr.ReadLine()) != null)
                        {
                            // Print each line
                            Console.WriteLine(line);
                        }
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    throw;
                }
            }
            // If `filename` is NOT a valid file
            else
            {
                throw new InvalidFileNameException(filename);
            }
            
        }
    }
}


class InvalidFileNameException : Exception
{
    public InvalidFileNameException()
    {
    }

    public InvalidFileNameException(string filename) : base($"Invalid file: {filename}") {}
}


class NoFileNameProvidedException : Exception
{
    public NoFileNameProvidedException() : base("No filename provided")
    {
    }
}