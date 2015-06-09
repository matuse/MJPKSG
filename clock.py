#!/usr/bin/python

from bootstrap import *
from RGB_Clock_Animation_snip import BlockClock

led.all_off()

# anim = RGBClock(led, 0, 3, 8, 11, 16, 19)

anim = BlockClock(led, 12)

while True:
	anim.step()
	led.update()
	sleep(1)
