fib_seq = [1, 2]

while max(fib_seq) <= 4000000:
    next_value = fib_seq[-1] + fib_seq[-2]

    if next_value <= 4000000:
        fib_seq.append(next_value)
    else:
        break

# use filter() to create a list of only the even numbers
# use sum() the new evens-only list that was created by the filter() method
print(sum(filter(lambda x: x % 2 == 0, fib_seq)))
