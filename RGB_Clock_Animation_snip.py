import time
from color import *
import timecolors


class BaseAnimation(object):

    def __init__(self, led, start, end):
        self._led = led
        self._start = start
        self._end = end
        if self._end == 0 or self._end > self._led.lastIndex:
            self._end = self._led.lastIndex

        self._size = self._end - self._start + 1
        self._step = 0

        self._timeRef = 0

    def __msTime(self):
        return time.time() * 1000.0

    def step(self, amt=1):
        raise RuntimeError("Base class step() called. This shouldn't happen")

    def run(self, amt=1, sleep=None, max_steps=0):
        self._step = 0
        cur_step = 0
        while max_steps == 0 or cur_step < max_steps:
            self._timeRef = self.__msTime()
            self.step(amt)
            self._led.update()
            if sleep:
                diff = (self.__msTime() - self._timeRef)
                t = max(0, (sleep - diff) / 1000.0)
                if t == 0:
                    print("Timeout of %dms is less than the minimum of %d!" % (sleep, diff))
                time.sleep(t)
            cur_step += 1


class RGBClock(BaseAnimation):

    """RGB Clock done with RGB LED strip(s)"""

    def __init__(self, led, hStart, hEnd, mStart, mEnd, sStart, sEnd):
        super(RGBClock, self).__init__(led, 0, 0)
        if hEnd < hStart:
            hEnd = hStart + 1
        if mEnd < mStart:
            mEnd = mStart + 1
        if sEnd < sStart:
            sEnd = sStart + 1
        self._hStart = hStart
        self._hEnd = hEnd
        self._mStart = mStart
        self._mEnd = mEnd
        self._sStart = sStart
        self._sEnd = sEnd

    def step(self, amt=1):
        t = time.localtime()

        r, g, b = timecolors._hourColors[t.tm_hour]
        self._led.fillRGB(r, g, b, self._hStart, self._hEnd)

        r, g, b = timecolors._minSecColors[t.tm_min]
        self._led.fillRGB(r, g, b, self._mStart, self._mEnd)

        r, g, b = timecolors._minSecColors[t.tm_sec]
        self._led.fillRGB(r, g, b, self._sStart, self._sEnd)

        self._step = 0
