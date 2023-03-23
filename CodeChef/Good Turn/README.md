Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

They consider a turn to be good if the sum of the numbers on their dice is greater than 66.
Given that in a particular turn Chef and Chefina got XX and YY on their respective dice, find whether the turn was good.

Input Format
- The first line of input will contain a single integer `T`, denoting the number of test cases.
- Each test case contains two space-separated integers `X` and `Y` — the numbers Chef and Chefina got on their respective dice.

Output Format

For each test case, output on a new line, YES, if the turn was good and NO otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings NO, no, nO, and No will be treated as equivalent.


Sample 1:
|Input|Output|
|---|---|
|4  |NO|
|1 4|NO|
|3 4|NO|
|4 2|YES|
|2 6|YES|

Explanation:

**Test case 11:** The sum of numbers on the dice is 1+4=51+4=5 which is smaller than 66. Thus, the turn is not good.

**Test case 22:** The sum of numbers on the dice is 3+4=73+4=7 which is greater than 66. Thus, the turn is good.

**Test case 33:** The sum of numbers on the dice is 4+2=64+2=6 which is equal to 66. Thus, the turn is not good.

**Test case 44:** The sum of numbers on the dice is 2+6=82+6=8 which is greater than 66. Thus, the turn is good.