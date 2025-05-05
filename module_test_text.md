====================================
The Module_test_mod Module
====================================

This module includes functions to help you calculate
the areas of different shapes. To use
it in your code you will first need to import
it into your source file:

    >>> import module_test

###### Triangles ######

The triangle function has two parameters - the
base and height of the triangle whose area
needs to be calculated. It returns the area of
that triangle. It can be invoked in this
manner, and the correct value will be returned
in floating point format.

    >>> module_test.triangle(4, 9)
    18.0

###### Rectangles ######

The rectangle function has two parameters - the
length and breadth of the rectangle whose area
needs to be calculated. It returns the area of
that rectangle and its invocation is done as
specified below. This will return an integer or
a floating point value depending on the
arguments passed.

    >>> module_test.rectangle(3, 9)
    27

###### Square ######

The square function has a single parameters -
the length of the square's edge. The value
returned is the square area of the square which
can be a integer or a floating point value. An
example invocation is given below.

    >>> module_test.square(7)
    49