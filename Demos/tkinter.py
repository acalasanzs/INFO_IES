import tkinter
from tkinter import *
ventana = Tk()
figura = Canvas(ventana, width=400,height=350)
figura.pack()
figura.create_oval(80, 50, 300 , 200)
figura.mainloop()