#! /usr/bin/env python

# https://www.youtube.com/watch?v=Wim9WJeDTHQ
# What's special about 277777788888899? - Numberphile

def per(n):
  chars = str(n)
  if len(chars) == 1:
    return 0
  nums = map((lambda x: int(x)), chars)
  prod = reduce((lambda x, y: x * y), nums)
  return 1 + per(prod)

max = -1
num = 0
while True:
  size = per(num)
  if size > max:
    max = size
    print(str(num) + " => " + str(size))
  num += 1
