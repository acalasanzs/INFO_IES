from tkinter import *
import math

class App:
    def __init__(self, master):
        self.w = Canvas(width=800, height=600, bg='black')
        self.w.draw_regular_polygon((400,400), 100, 5, 0, outline='green')
        self.w.draw_regular_polygon((400,400), 100, 5, math.pi/5, outline='red')
        self.w.grid(row=0, column=0)
    def _draw_regular_polygon(self, center, radius, n, angle, **kwargs):
        angle -= (math.pi/n)
        coord_list = [[center[0] + radius * math.sin((2*math.pi/n) * i - angle),
            center[1] + radius * math.cos((2*math.pi/n) * i - angle)] for i in range(n)]
        return self.create_polygon(coord_list, **kwargs)
    Canvas.draw_regular_polygon = _draw_regular_polygon
root = Tk()
app = App(root)
root.mainloop()