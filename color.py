#!/usr/bin/python

from bootstrap import *

colors = [
	(255.0,0.0,0.0),
	(0.0,255.0,0.0),
	(0.0,0.0,255.0),
	(255.0,255.0,255.0),
]

#step = 0.01
#for c in range(4):
#	r, g, b = colors[c]
#	level = 0.01
#	dir = step
#	while level >= 0.0:
#		led.fill(Color(r, g, b, level))
#		led.update()
#		if(level >= 0.99):
#			dir = -step
#		level += dir
#		#sleep(0.005)


r, g, b = colors[3]
level = 0.75
led.fill(Color(r, g, b, level))
led.update()
