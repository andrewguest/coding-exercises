number_of_test_cases: int = int(input())


for _ in range(0, number_of_test_cases):
    x, y = map(int, input().split())

    if (x + y) > 6:
        print("YES")
    else:
        print("NO")
