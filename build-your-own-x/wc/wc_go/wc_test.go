package main

import (
	"testing"
)

func TestGetBytesCount(t *testing.T) {
	// Test that the getBytesCount() function returns 342190

	actualBytesCount := getBytesCount("test.txt")
	expectedBytesCount := int64(342190)

	if actualBytesCount != expectedBytesCount {
		t.Errorf("actualBytesCount: %d, expectedBytesCount: %d", actualBytesCount, expectedBytesCount)
	}
}

func TestGetLinesCount(t *testing.T) {
	// Test that the getLinesCount() function returns 7145

	actualLinesCount := getLinesCount("test.txt")
	expectedLinesCount := int64(7145)

	if actualLinesCount != expectedLinesCount {
		t.Errorf("actualLinesCount: %d, expectedLinesCount: %d", actualLinesCount, expectedLinesCount)
	}
}

func TestGetWordsCount(t *testing.T) {
	// Test that the getWordsCount() function returns 58164

	actualWordsCount := getWordsCount("test.txt")
	expectedWordsCount := int64(58164)

	if actualWordsCount != expectedWordsCount {
		t.Errorf("actualWordsCount: %d, expectedWordsCount: %d", actualWordsCount, expectedWordsCount)
	}
}

func TestGetCharactersCount(t *testing.T) {
	// Test that the getWordsCount() function returns 58164

	actualCharacterCount := getCharactersCount("test.txt")
	expectedCharacterCount := int64(339292)

	if actualCharacterCount != expectedCharacterCount {
		t.Errorf("actualCharacterCount: %d, expectedCharacterCount: %d", actualCharacterCount, expectedCharacterCount)
	}
}
