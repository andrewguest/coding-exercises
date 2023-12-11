import copy

inp = []
with open("input.txt", "r") as f:
    inp = f.readlines()
box_stack = [[] for _ in range(9)]

for i in range(8):
    row = inp[i].split(" ")
    row_simplified = []
    j = 0
    while j < len(row):
        if row[j] == "":
            j += 4
            row_simplified.append("")
        else:
            row_simplified.append(row[j][1])
            j += 1
    for i, box in enumerate(row_simplified):
        if box:
            box_stack[i].insert(0, box)


def part_1() -> str:
    _box_stack = copy.deepcopy(box_stack)

    for i in range(10, len(inp)):
        _, num, _, source, _, dest = inp[i].split()
        num, source, dest = [int(x) for x in [num, source, dest]]

        for _ in range(num):
            _box_stack[dest - 1].append(_box_stack[source - 1].pop())

    return "".join([x[-1] for x in _box_stack])


def part_2() -> str:
    _box_stack = copy.deepcopy(box_stack)
    for i in range(10, len(inp)):
        _, num, _, source, _, dest = inp[i].split()
        num, source, dest = [int(x) for x in [num, source, dest]]

        _box_stack[dest - 1].extend(_box_stack[source - 1][-num:])
        _box_stack[source - 1] = _box_stack[source - 1][:-num]

    return "".join([x[-1] for x in _box_stack])


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
