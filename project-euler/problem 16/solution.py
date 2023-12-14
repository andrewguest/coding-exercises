#   l = []
#   for d in str(2 ** 1000):
#       l.append(int(d))
#   print(sum(l))

print(sum([int(d) for d in str(2**1000)]))
