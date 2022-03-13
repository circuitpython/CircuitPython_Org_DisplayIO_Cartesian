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
raw_data = []
data = []
MAX_DICE_SIDE = 20
NUMBER_OF_DICE = 10
NUMBER_OF_ROLLS = 500

for _ in range(NUMBER_OF_ROLLS):
    # Simulate equivalent dice rolls
    sum_random = 0
    for _ in range(NUMBER_OF_DICE):
        sum_random += random.uniform(1, MAX_DICE_SIDE)
    average_random = sum_random // NUMBER_OF_DICE
    raw_data.append(average_random)

# Calculate the number of each roll result and pair with itself
y_upper_bound = 0
for value in range(MAX_DICE_SIDE + 1):
    value_count = raw_data.count(value) / 10
    data.append((value, value_count))
    y_upper_bound = max(y_upper_bound, value_count)

# pybadge display:  160x128
# Create a Cartesian widget
# https://circuitpython.readthedocs.io/projects/displayio-layout/en/latest/api.html#module-adafruit_displayio_layout.widgets.cartesian
my_plane = Cartesian(
    x=20,  # x position for the plane
    y=2,  # y plane position
    width=135,  # display width
    height=105,  # display height
    xrange=(0, MAX_DICE_SIDE),  # x range
    yrange=(0, y_upper_bound),  # y range
    fill_area=True,
)

my_group = displayio.Group()
my_group.append(my_plane)
display.show(my_group)  # add high level Group to the display

print("examples/displayio_layout_cartesian_fillarea.py")

for x, y in data:
    my_plane.add_plot_line(x, y)
    time.sleep(0.1)

while True:
    pass
