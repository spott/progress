#!/usr/bin/env python

from __future__ import print_function

import random
import time

from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, PixelBar,
                          ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner,
                              PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie
from progress.colors import bold, blue


def sleep():
    t = 0.01
    t += t * random.uniform(-0.05, 0.05)  # Add some variance
    time.sleep(t)


for bar_cls in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s] (%(iter_value)s)'
    bar = bar_cls(bar_cls.__name__, suffix=suffix, color=62)
    for i in bar.iter(range(200, 400)):
        sleep()

for bar_cls in (IncrementalBar, PixelBar, ShadyBar):
    suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
    with bar_cls(bar_cls.__name__, suffix=suffix, max=200) as bar:
        for i in range(200):
            bar.next()
            sleep()

for bar_cls in (IncrementalBar,):
    suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
    with bar_cls(bar_cls.__name__, suffix=suffix, max=200, disable=True) as bar:
        for i in range(200):
            bar.next()
            sleep()

bar = IncrementalBar(bold('Colored'), color='green')
for i in bar.iter(range(200)):
    sleep()

for spin in (Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner):
    for i in spin(spin.__name__ + ' %(index)d ').iter(range(100)):
        sleep()

for singleton in (Counter, Countdown, Stack, Pie):
    for i in singleton(singleton.__name__ + ' ').iter(range(100)):
        sleep()

bar = IncrementalBar('Random', suffix='%(index)d')
for i in range(100):
    bar.goto(random.randint(0, 100))
    sleep()
bar.finish()


