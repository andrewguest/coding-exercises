import csv


def compute(list_of_names: list[str]):
    ans = sum(
        (i + 1) * (ord(c) - ord("A") + 1)
        for (i, name) in enumerate(sorted(list_of_names))
        for c in name
    )
    return str(ans)


# read the names.txt file into a list of strings
with open("./names.txt", "r") as names_file:
    names_list: list[str] = list(csv.reader(names_file, delimiter=","))[0]


print(compute(names_list))
