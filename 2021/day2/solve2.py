#! /usr/bin/env python

print('hello')

commands = []
with open('input.txt') as f:
	for line in f.readlines():
		print(line)
		if len(line) > 1:
			w,n = line.split()
			print(len(commands))
			commands.append((w,n))

print(commands)

pos, depth, aim = 0,0,0

for w,n in commands:
	n = int(n)
	if w == 'forward':
		pos += n
		depth += aim*n
	elif w == 'down':
		aim += n
	elif w == 'up':
		aim -= n
	else:
		print('unkown command:', w)
		raise Error(w)	

print(pos * depth)
