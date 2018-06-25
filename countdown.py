#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from datetime import timedelta, datetime, tzinfo

# the_end = datetime(2072, 10, 31, 16, 30)
# the_end = datetime(2018, 11, 23, 16, 30)
the_end = datetime(2018, 06, 21, 16, 30)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, rotate=0)


def draw(msg):
    global device
    with canvas(device) as drawobj:
        text(drawobj, (1, 1), msg[::-1], fill="white")

draw("DONE")
device.contrast(30)
while (1):
    delta = the_end - datetime.now()
    weeks = delta.days 
    print(weeks)
    #draw(str(weeks))
    time.sleep(60)

