products: list[int] = []
total = 0


# CASE 1. (a - 2-digit) and (b - 3-digit)
max_a: int = 98
max_b: int = 987

for a in range(10, max_a + 1):
    for b in range(100, max_b + 1):
        c = a * b

        if len(str(c)) > 5:
            break

        all_digits = sorted(str(c)+str(a)+str(b))

        if all_digits == list("123456789"):
            if c not in products:
                products += [c]
                total += c


# CASE 2. (a - 1-digit) and (b - 4-digit)
max_a: int = 9
max_b: int = 9876

for a in range(1, max_a + 1):
    for b in range(987, max_b + 1):
        c = a * b

        if len(str(c)) > 5:
            break

        all_digits = sorted(str(c)+str(a)+str(b))

        if all_digits == list("123456789") :
            if c not in products:
                products += [c]
                total += c

print(total)
