from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, highlightbackground="#ffffff")
        self.parent = master
root = Tk()
#root.iconbitmap('icon.ico')
root.overrideredirect(1)
root.geometry('800x250+500+100')
app = Application(root)
app.parent.configure(background = '#1abc9c')
root.resizable(width=False, height=False)
count = 0
def do():
    global count
    w = Label(root,text=count)
    w.pack()
    but['text'] = "Tornar-hi"
    but['fg'] = "#8e44ad"
    count += 1
exit = Button(root, 
                bg='#ffffff',
                fg='#1abc9c',
                relief='flat',
                text='Tancar',
                width=8,
                font=('Roboto',18),
                command=root.destroy)
but = Button(root, 
                bg='#ffffff',
                fg='#1abc9c',
                relief='flat',
                text='Intentar',
                width=8,
                font=('Roboto',15),
                command=do,)
but.pack(side=BOTTOM)
exit.pack(side=RIGHT,anchor="ne")
etiqueta = Label(root,text="Apartat 10 ex AMPLIACIO",fg="#1abc9c",font=('Roboto',28))
etiqueta.pack(side=TOP,fill=X)


root.mainloop()
""" import tkinter
class window:
    def __init__(self,title="Nothing")
        root = tkinter.Tk()
        root.iconbitmap('icon.ico')
        root.geometry("400x300")
        etiqueta = tkinter.Label(root,text="",fg="#2980b9")
        etiqueta.pack(side=tkinter.TOP,fill=tkinter.X)
        root.mainloop() """