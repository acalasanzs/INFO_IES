from tkinter import *
root = Tk()
root.overrideredirect(1)
root.geometry('800x250+400+180')
input = Entry(root,fg="white",bg='#1abc9c',relief='flat')
input.pack(side=BOTTOM, anchor="center")
root.mainloop()