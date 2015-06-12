#!/usr/bin/python
import threading
import time
from bootstrap import *

#setup colors to loop through for fade
#colors = [
#	(255.0,0.0,0.0),
#	(0.0,255.0,0.0),
#	(0.0,0.0,255.0),
#	(255.0,255.0,255.0),
#]

#step = 0.01

#animations - each animation method moves the animation forward one step on each call
#after each step, call update() to push it to the LED strip

#evenly distributed rainbow
try:
        while True:
                #anim = RainbowCycle(led)
                #for i in range(384*2):
                #        anim.step()
                #        led.update()

                anim = Rainbow(led)
                for i in range(384):
                        anim.step()
                        led.update()
			sleep(0.05)

except KeyboardInterrupt:
        led.fillOff()



