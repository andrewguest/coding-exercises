import math

#   l = []
#   for d in str(math.prod(range(1, 101))):
#       l.append(int(d))
#   print(sum(l))
print(sum([int(d) for d in str(math.prod(range(1, 101)))]))
