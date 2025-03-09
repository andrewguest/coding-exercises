sentence = (
    "Never underestimate the willingness of the greedy to throw you under the bus"
)

print(sentence)
print("Becomes:")
# sentence.split(" ")  splits `sentence` into a list of words based on spaces
# [::-1]  slices the list in reverse order [start:stop:step]
#   goes through the given list from start to stop, starting at the end of the list
# " ".join()  join the given list elements with spaces
print(" ".join(sentence.split(" ")[::-1]))
