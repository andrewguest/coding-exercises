var number = 7826
var reverseNum = 0

print("Original Number-", number)

while(number != 0) {
    reverseNum = reverseNum * 10
    reverseNum = reverseNum + number % 10
    number = number/10
}

print("Reverse Number-", reverseNum)
