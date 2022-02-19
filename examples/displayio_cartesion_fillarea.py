# SPDX-FileCopyrightText: 2021 Stefan Krüger
#
# SPDX-License-Identifier: MIT
#############################
"""
This is a basic demonstration of a Cartesian widget for line-ploting
"""

import time
import board
import displayio
import random
from displayio_cartesian import Cartesian

# create the display on the PyPortal or Clue or PyBadge(for example)
display = board.DISPLAY
# otherwise change this to setup the display
# for display chip driver and pinout you have (e.g. ILI9341)

# Generate data - here we'll make a normal distribution
X_LOWER_BOUND = 0
X_UPPER_BOUND = 10
raw_data = []
data = []

for _ in range(100):
    data_point = int(10 * random.random(X_LOWER_BOUND, X_UPPER_BOUND + 1))
    raw_data.append(data_point)

y_upper_bound = 0
for value in range(len(X_UPPER_BOUND + 1)):
    value_count = raw_data.count(value)
    data.append(value_count)
    y_upper_bound = max(y_upper_bound, value_count)

# pybadge display:  160x128
# Create a Cartesian widget
# https://circuitpython.readthedocs.io/projects/displayio-layout/en/latest/api.html#module-adafruit_displayio_layout.widgets.cartesian
my_plane = Cartesian(
    x=15,  # x position for the plane
    y=2,  # y plane position
    width=140,  # display width
    height=105,  # display height
    xrange=(X_LOWER_BOUND, X_UPPER_BOUND),  # x range
    yrange=(0, y_upper_bound),  # y range
    fill_area=True,
)

my_group = displayio.Group()
my_group.append(my_plane)
display.show(my_group)  # add high level Group to the display

print("examples/displayio_layout_cartesian_fillarea.py")

for x, y in data:
    my_plane.add_plot_line(x, y)
    time.sleep(0.5)

while True:
    pass
