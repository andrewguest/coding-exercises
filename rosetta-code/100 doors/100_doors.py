# False = closed
# True = open


# Keep track of open doors
open_doors = []

# Initially every door is closed (False)
doors = [False] * 100

for i in range(100):
    for j in range(i, 100, i + 1):
        doors[j] = not doors[j]
    open_doors.append(i + 1) if doors[i] else None

print(open_doors)
