#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "RLA"


def draw_circle(canvas, pos, radius, color='black'):
    """
    Draws circle on the given canvas, return the id of the item
    :param canvas: canvas
    :param pos: Vector2D representing coordinates of the circle
    :param radius: radius of the circle
    :param color: color of the circle
    :return: id of the circle on the canvas
    """
    return canvas.create_oval(pos.x - radius, pos.y - radius, pos.x + radius, pos.y + radius, fill=color)


def draw_dot(c, dot):
    c.coords(dot.id, dot.pos.x - dot.radius, dot.pos.y - dot.radius, dot.pos.x + dot.radius, dot.pos.y + dot.radius)
