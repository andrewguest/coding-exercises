package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parseInputFile(filename string) []string {
	// Open the given file
	readFile, err := os.Open(filename)

	if err != nil {
		fmt.Println(err)
	}

	// Create a new `Scanner` instance and read the file into the IO buffer
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	// Loop through every line in the `Scanner` instance and append it to the `fileLines` array
	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	// Close the file
	err = readFile.Close()
	if err != nil {
		return []string{}
	}

	return fileLines
}

func part1(inputLines []string) {
	/*
		1. Subtract the smallest value in `left_numbers` from the smallest value in `right_numbers`.
		2. Store the difference in `differences`.
		3. Remove the smallest values from both lists.
		4. Repeat until both lists are empty
	*/

	var difference int
	var leftNumbers []int
	var rightNumbers []int

	// Loop through each line, adding the first number to the `leftNumbers` array and the second number to the
	//	`rightNumbers` array.
	for _, line := range inputLines {
		tempNumbers := strings.Split(line, " ")

		leftInt, _ := strconv.Atoi(tempNumbers[0])
		leftNumbers = append(leftNumbers, leftInt)

		rightInt, _ := strconv.Atoi(tempNumbers[len(tempNumbers)-1])
		rightNumbers = append(rightNumbers, rightInt)
	}

	sort.Ints(leftNumbers)
	sort.Ints(rightNumbers)

	// Subtract the mininum value in `leftNumbers` from the minimum value in `rightNumbers` in a loop, appending
	//	the absolute value of the difference to `differences`, then remove both minimum values after the math operation.
	for _, _ = range leftNumbers {
		diff := math.Abs(float64(rightNumbers[0] - leftNumbers[0]))
		difference += int(diff)

		leftNumbers = leftNumbers[1:]
		rightNumbers = rightNumbers[1:]
	}

	fmt.Printf("Part 1: %v\n", difference)
}

func part2(inputLines []string) {
	similarityTotal := 0
	var leftNumbers []int
	var rightNumbers []int

	for _, line := range inputLines {
		tempNumbers := strings.Split(line, " ")

		leftInt, _ := strconv.Atoi(tempNumbers[0])
		leftNumbers = append(leftNumbers, leftInt)

		rightInt, _ := strconv.Atoi(tempNumbers[len(tempNumbers)-1])
		rightNumbers = append(rightNumbers, rightInt)
	}

	for _, number := range leftNumbers {
		// Count how many times `number` occurs in `rightNumbers`
		count := 0
		for _, n := range rightNumbers {
			if n == number {
				count++
			}
		}

		similarityTotal += number * count
	}

	fmt.Printf("Part 2: %v\n", similarityTotal)
}

func main() {
	lines := parseInputFile("input.txt")
	part1(lines)
	part2(lines)
}
