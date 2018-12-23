#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "RLA"

from model.Vector2D import Vector2D
from random import randint


class Dot:

    def move(self, speed=10):
        x_direction = randint(0, 1)
        y_direction = randint(0, 1)

        print(str(x_direction))
        print(str(y_direction))
        if x_direction == 0:
            x_speed = speed
        else:
            x_speed = -speed

        if y_direction == 0:
            y_speed = speed
        else:
            y_speed = -speed

        if self.generation == 0:
            movement = Vector2D(x_speed, y_speed)

        # Move Dot
        self.pos = self.pos + movement

        # Add new movement to list of movements
        self.movements.append(movement)

    def __init__(self, cid, pos, radius, parent=None, generation=0):
        self.id = cid
        self.pos = pos
        self.radius = radius
        self.generation = generation
        if parent is not None:
            self.movements = parent.movements
        else:
            self.movements = []


