.. role:: strike

Cartesian
=======================

This presents an extended documentation regarding the cartesian library. and the


**Quickstart: Importing and using Cartesian**

Here is one way of importing the `Cartesian` class so you can use it as
the name ``Plane``:

.. code-block:: python

    from displayio_cartesian import Cartesian as Plane

Now you can create a plane at pixel position x=20, y=30 using:

.. code-block:: python

    my_plane=Plane(x=20, y=30) # instance the plane at x=20, y=30

Once you setup your display, you can now add ``my_plane`` to your display using:

.. code-block:: python

    display.show(my_plane) # add the group to the display

If you want to have multiple display elements, you can create a group and then
append the plane and the other elements to the group.  Then, you can add the full
group to the display as in this example:

.. code-block:: python

    my_plane= Plane(20, 30) # instance the plane at x=20, y=30
    my_group = displayio.Group(max_size=10) # make a group that can hold 10 items
    my_group.append(my_plane) # Add my_plane to the group

    #
    # Append other display elements to the group
    #

    display.show(my_group) # add the group to the display


**Summary: Cartesian Features and input variables**

The `Cartesian` widget has some options for controlling its position, visible appearance,
and scale through a collection of input variables:

- **position**: :attr:`x`, :attr:`~Widget.y`, :attr:`~Widget.anchor_point`,
  :attr:`~Widget.anchored_position` and
  :attr:`nudge_x`, :attr:`nudge_y`. Nudge parameters are used to account for the float and int
  conversions required to display different ranges and values. Conversion are required
  as displays work in integers and not floats

- **size**: :attr:`width` and :attr:`height`

- **color**: :attr:`axes_color`, :attr:`font_color`, :attr:`tick_color`, :attr:`pointer_color`

- **background color**: :attr:`background_color`

- **linewidths**: :attr:`axes_stroke` and :attr:`major_tick_stroke`

- **range**: :attr:`xrange` and :attr:`yrange` This is the range in absolute units.
  For example, when using (20-90), the X axis will start at 20 finishing at 90.
  However the height of the graph is given by the height parameter. The scale
  is handled internal to provide a 1:1 experience when you update the graph.


.. figure:: cartesian.gif
   :scale: 100 %
   :figwidth: 50%
   :align: center
   :alt: Diagram of the cartesian widget with the pointer in motion.

   This is a diagram of a cartesian widget with the pointer moving in the
   plot area.

.. figure:: cartesian_zones.png
   :scale: 100 %
   :figwidth: 50%
   :align: center
   :alt: Diagram of the cartesian widget zones.

   This is a diagram of a cartesian widget showing the different zones.

.. figure:: cartesian_explanation.png
   :scale: 100 %
   :figwidth: 50%
   :align: center
   :alt: Diagram of the cartesian widget localisation.

   This is a diagram of a cartesian widget showing localisation scheme.
