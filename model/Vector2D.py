#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "RLA"


class Vector2D:

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self + other

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"


if __name__ == '__main__':
    a = Vector2D(2, 3)
    b = Vector2D(4, 5)

    print(str(a + b))
    print(str(b + a))
