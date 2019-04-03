import random

# monte carlo simulation to generate pi

# generate random points in the range [0, 1)
points = [(random.random(), random.random()) for i in range(0, 100000)]

in_circle = 0
for point in points:
  x, y = point
  dist = (((x - 0.5) ** 2) + ((y - 0.5) ** 2)) ** 0.5
  if dist < 0.5:
    in_circle += 1

area = in_circle / len(points)
pie = area / (0.5 ** 2)

print('pie =', pie)
