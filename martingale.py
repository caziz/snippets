#!/usr/bin/env python

import random

# https://en.wikipedia.org/wiki/Martingale_(betting_system)

winrate = 0.02
winpayout = 2
bet = 100
roundno = 1
credit = 0

print("win rate: " + str(winrate))
print("starting bet: " + str(bet))
print("============")

while True:
  print("round: " + str(roundno))
  print("betting: " + str(bet))
  credit -= bet
  print("credit: " + str(credit))
  roundno += 1
  rand = random.random()
  if rand < winrate:
    print("\tyou won!")
    credit += winpayout * bet
    print("total winnings: " + str(credit))
    break
  else:
    print("\tyou lost")
    bet *= 2
