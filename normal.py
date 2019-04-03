import random
from collections import Counter

# creates a normal distribution of coin flips
positions = []
# 5000 samples
for i in range(1, 5000):
  pos = 0
  # 1000 moves
  for round in range(1, 1000):
    if random.random() < 0.5:
      pos += 1 
    else:
      pos -= 1
  positions.append(pos)

# count the samples
counts = Counter(positions)
keys =counts.keys()
vals = list(counts.values())

# print the distribution in ASCII
for y in range(max(vals), min(vals) + 1, -1):
  for x in range(min(keys), max(keys) + 1):
    if y <= counts[x]:
      print('X', end='')
    else:
      print(' ', end='')
  print('')
