package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func getBytesCount(filePath string) int64 {
	fileInfo, err := os.Stat(filePath)

	// Handle errors
	if err != nil {
		fmt.Println("Error:", err)
	}

	fileSize := fileInfo.Size()
	return fileSize
}

func getLinesCount(filePath string) int64 {
	file, err := os.Open(filePath)

	// Handle errors
	if err != nil {
		fmt.Println("Error:", err)
	}

	// Wait to close the file until after the rest of the code is complete
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			fmt.Println("Error:", err)
		}
	}(file)

	lineCount := int64(0)

	// Create a scanner to read the file
	scanner := bufio.NewScanner(file)

	// Loop through each line in the file, increment the `lineCount`
	for scanner.Scan() {
		lineCount++
	}

	return lineCount
}

func getWordsCount(filePath string) int64 {
	file, err := os.Open(filePath)

	// Handle errors
	if err != nil {
		fmt.Println("Error:", err)
	}

	// Wait to close the file until after the rest of the code is complete
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			fmt.Println("Error:", err)
		}
	}(file)

	wordCount := int64(0)

	// Create a scanner to read the file
	scanner := bufio.NewScanner(file)

	// Loop through each line in the file, counting the number of words in each line
	for scanner.Scan() {
		line := scanner.Text()
		words := strings.Fields(line)
		wordCount += int64(len(words))
	}

	return wordCount
}

func getCharactersCount(filePath string) int64 {
	characterCount := int64(0)

	// Open the file
	data, err := os.ReadFile("test.txt")

	// Log any error that is thrown while opening the file
	if err != nil {
		log.Fatal(err)
	}

	// data is now a byte slice containing the file's contents
	// You can convert it to a string if needed
	text := string(data)
	characterCount = int64(len(text))

	return characterCount
}

func main() {
	// bytes count
	shortBytesCount := flag.Bool("c", false, "Print the count of bytes")
	longBytesCount := flag.Bool("bytes", false, "Print the count of bytes")

	// lines count
	shortLinesCount := flag.Bool("l", false, "Print the count of lines in each file")
	longLinesCount := flag.Bool("lines", false, "Print the count of lines in each file")

	// word count
	shortWordsCount := flag.Bool("w", false, "Print the count of words in each file")
	longWordsCount := flag.Bool("words", false, "Print the count of words in each file")

	// character count
	shortCharacterCount := flag.Bool("m", false, "Print the count of characters in each file")
	longCharacterCount := flag.Bool("chars", false, "Print the count of characters in each file")

	// Get the flag arguments
	flag.Parse()

	// Get the remaining positional argument(s)
	filename := flag.Arg(0)

	var result int64
	if *shortBytesCount == true || *longBytesCount == true {
		result = getBytesCount(filename)
	} else if *shortLinesCount == true || *longLinesCount == true {
		result = getLinesCount(filename)
	} else if *shortWordsCount == true || *longWordsCount == true {
		result = getWordsCount(filename)
	} else if *shortCharacterCount == true || *longCharacterCount == true {
		result = getCharactersCount(filename)
	}

	fmt.Printf("%d %s\n", result, filename)
}
