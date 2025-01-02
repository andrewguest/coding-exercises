package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func parseInput(filename string) []string {
	// Array that will hold each line from the file
	fileLines := []string{}

	// Open the file
	readFile, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}

	// Read the file into the buffer
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	// Append each line to the array of lines
	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	// Close the file
	closeErr := readFile.Close()
	if err != nil {
		fmt.Println(closeErr)
	}

	for _, line := range fileLines {
		fmt.Println(line)
	}

	return fileLines
}

func part1() {
	/*
		Loop through each line of input.txt and combine the first and last digit to form  a single two-digit number.
		Then SUM all of the two-digit numbers together and return the final total.

		For example:
			`1abc2` becomes `12`
			`ab3gt52f4x` becomes `34`
	*/

	//var digits []int
	validNumbers := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
	inputLines := parseInput("input.txt")

	for _, line := range inputLines {
		var localDigits []int32
		for _, char := range line {
			fmt.Printf("%c\n", char) // debug
			if slices.Contains(validNumbers, char) {
				// If `localDigits` is empty then add the element to the array
				if len(localDigits) == 0 {
					charStr := fmt.Sprintf("%c", char)
					localDigits = append(localDigits, charStr)
				} else if len(localDigits) == 1 {
					// If there's only one other element in `localDigits` then append
					localDigits = append(localDigits, char)
				} else {
					localDigits[1] = char
				}
			}
			fmt.Println(localDigits)
		}
	}
}

func main() {
	fmt.Println("Part 1 solution: ")
	part1()
}
