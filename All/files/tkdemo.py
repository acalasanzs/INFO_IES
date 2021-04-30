from tkinter import *
import random
lletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main():
    class Application(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master, highlightbackground="#ffffff")
            self.parent = master
    root = Tk()
    root.overrideredirect(1)
    root.geometry('800x250+400+180')
    app = Application(root)
    app.parent.configure(background = '#1abc9c')
    root.resizable(width=False, height=False)
    matches = []
    global p
    p = "adsdds"
    clletres = lletres
    def do():
        global p
        but['text'] = "Tornar-hi"
        but['fg'] = "#8e44ad"
        app['background'] = '#8e44ad'
        #print("Intent nº{}".format(count))
        try:
            a = random.choice(clletres)
            matches.append(a)
            clletres.remove(a)
        except:
            print("You Win")
        current = p
        abec = "abdefghijklmnñopqrstuvwxyz"
        for i in matches:
            abec = abec.translate({ord(i): "-"})
        for x in abec:
            p = p.translate({ord(x): "-"})
        print(p,"|",abec)
        temp = p
        p = current
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
    main = Label(root,text="")

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
if __name__ == "__main__":
    main()