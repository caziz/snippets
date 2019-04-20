#! /usr/bin/env python3

# Simulates Conway's Game of Life in the terminal by using braille unicode characters.

# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# https://en.wikipedia.org/wiki/Braille_Patterns

import time
import random

fps = 15

class Game:
	# init a game state randomly
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.state = [[bool(random.getrandbits(1)) for i in range(self.w)] for i in range(self.h)]

	# run the game indefinitely
	def run(self):
		while True:
			self.tick()
			time.sleep(1/fps)

	# directions that count as neighbors
	dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	# display and update state each tick
	def tick(self):
		self.display()
		new_state = [[False for i in range(self.w)] for i in range(self.h)]
		for x in range(0, self.w):
			for y in range(0, self.h):
				neighbors = 0
				for (dx, dy) in self.dirs:
					xp = x + dx
					yp = y + dy
					if (xp >= 0 and xp < self.w and
						yp >= 0 and yp < self.h and
						self.state[yp][xp]):
							neighbors += 1
				new_state[y][x] = ((neighbors == 2 and self.state[y][x]) or neighbors == 3)
		self.state = new_state

	# print state using braille characters
	def display(self):
		pixels = [[0x2800 for w in range(-(-self.w // 2))] for h in range(-(-self.h // 4))]
		vals = [[0x1,  0x2,  0x4, 0x40], [0x8, 0x10, 0x20, 0x80]]
		for h in range(0, self.h):
			for w in range(0, self.w):
				pixels[h // 4][w // 2] += self.state[h][w] * vals[w % 2][h % 4]
		for row in pixels:
			print(chr(0x2551), end="")
			for pixel in row:
				print(chr(pixel), end="")
			print(chr(0x2551))
		print(chr(0x2560) + (chr(0x2550) * (-(-self.w // 2))) + chr(0x2563))

class GameState(Game):
	# init the game with a particular state
	def __init__(self, state):
		self.w = len(state[0])
		self.h = len(state)
		self.state = state

pulsar = [
	[False] * 17,
	[False] * 17,
    [False] * 4 + [True] * 3 + [False] * 3 + [True] * 3 + [False] * 4,
	[False] * 17,
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False], 
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False], 
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False],
	[False] * 4 + [True] * 3 + [False] * 3 + [True] * 3 + [False] * 4,
	[False] * 17,
	[False] * 4 + [True] * 3 + [False] * 3 + [True] * 3 + [False] * 4,
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False], 
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False], 
	[False, False, True] + [False] * 4 + [True, False, True] + [False] * 4 + [True, False, False],
	[False] * 17,
	[False] * 4 + [True] * 3 + [False] * 3 + [True] * 3 + [False] * 4,
	[False] * 17,
	[False] * 17
]

column = \
	[[False] * 18] * 4 + \
	[[False] * 5 + [True] * 8 + [False] * 5] + \
	[[False] * 5 + [True, False] + [True] * 4 + [False, True] + [False] * 5] + \
	[[False] * 5 + [True] * 8 + [False] * 5] + \
	[[False] * 18] * 4

gun = \
	[[False] * 25] * 2 + \
	[[False] * 3 + [True, True] + [False] * 20] * 2 + \
	[[False] * 25] * 9 + \
	[[False, True, True] + [False] * 3 + [True, True] + [False] * 17] + \
	[[False] * 25] + \
	[[False, False, True] + [False] * 3 + [True] + [False] * 18] + \
	[[False] * 3 + [True] * 3 + [False] * 19] * 2 + \
	[[False] * 25] * 2 + \
	[[False] * 6 + [True] + [False] * 18] + \
	[[False] * 5 + [True] * 3 + [False] * 17] + \
	[[False] * 4 + [True] + [False] * 3 + [True] + [False] * 16] + \
	[[False] * 6 + [True] + [False] * 18] + \
	[[False] * 3 + [True] + [False] * 5 + [True] + [False] * 15] * 2 + \
	[[False] * 4 + [True] + [False] * 3 + [True] + [False] * 16] + \
	[[False] * 5 + [True] * 3 + [False] * 17] + \
	[[False] * 25] * 8 + \
	[[False] * 5 + [True, True] + [False] * 18] * 2 + \
	[[False] * 25]



# game = Game(80, 50)
# game = GameState([[True, True], [True, True], [False, False]])
# game = GameState(pulsar)
# game = GameState(column)
game = GameState(gun)
game.run()


