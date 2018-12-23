#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "RLA"

from tkinter import *
from model.Dot import Dot
from model.Vector2D import Vector2D
from view.Helpers import draw_circle
from view.Helpers import draw_dot

# Windows props
master = Tk()
width = 800
height = 600

# Game props
nb_dots = 20
radius = 2
dots = []

canvas = Canvas(master, width=width, height=height)
canvas.pack()

for i in range(0, nb_dots):
    pos = Vector2D(width / 2, height / 2)
    cid = draw_circle(canvas, pos, radius)
    dots.append(Dot(cid, pos, radius))


def step():
    global master
    global canvas
    global dots
    for dot in dots:
        dot.move()
        draw_dot(canvas, dot)

    master.after(30, step)


step()
canvas.mainloop()

