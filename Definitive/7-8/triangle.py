from tkinter import *

def draw(a, b, c):
    # determine corner points of triangle with sides a, b, c
    A = (0, 0)
    B = (c, 0)
    hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
    dx = (b**2 - hc**2)**0.5
    if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx # dx has two solutions
    C = (dx, hc)

    # move away from topleft, scale up a bit, convert to int
    coords = [int((x + 1) * 75) for x in A+B+C]

    # draw using Tkinter
    root = Tk()
    canvas = Canvas(root, width=500, height=300)
    canvas.create_polygon(*coords)
    canvas.pack()
    root.mainloop()

draw(1, 1, 1)