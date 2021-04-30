from tkinter import *
import random,time
lletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ttk():
    def lose():
        print("YOU LOSE")
        los = Label(root,text="YOU lose!",font=("Montserrat",40),fg="red")
        los.pack(side=BOTTOM,anchor="center",pady=20,padx=20,expand=1)
        but.pack_forget()
        cur.place_forget()
    def win():
        print("YOU WIN")
        wi = Label(root,text="YOU WIN!",font=("Montserrat",40),fg="green")
        wi.pack(side=BOTTOM,anchor="center",pady=20,padx=20,expand=1)
        but.pack_forget()
        cur.place_forget()
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
    global p,temp,intents
    clletres = lletres
    p = "jk"
    temp = "-"
    intents = 0
    def do():
        global p,temp,intents
        but['text'] = "Tornar-hi ({})".format(intents)
        but['fg'] = "#8e44ad"
        app['background'] = '#8e44ad'
        print("Intent nº{}:".format(intents))
        try:
            if intents <= 10:
                intents += 1
                assert "-" in temp
                a = random.choice(clletres)
                matches.append(a)
                clletres.remove(a)
                current = p
                abec = "abdefghijklmnñopqrstuvwxyz"
                for i in matches:
                    abec = abec.translate({ord(i): "-"})
                for x in abec:
                    p = p.translate({ord(x): "-"})
                print(p,"|",abec)
                temp = p
                cur['text'] = temp+"\n"+abec
                p = current
            else:
                lose()
                but.configure(text="YOU LOSE",
                            fg="red",
                            padx=20,
                            command=lose)
        except:
            win()
            but.configure(text="YOU WIN",
                            fg="green",
                            padx=20,
                            command=win)
    exit = Button(root, 
                    bg='#ffffff',
                    fg='#1abc9c',
                    relief='flat',
                    text='Tancar',
                    width=8,
                    font=('Roboto',18),
                    command=root.destroy)
    input = Entry(root,fg="white",bg='#2abc9c',relief='flat',font=("Montserrat",30))
    input.place(relx=0.5,rely=0.5,anchor='center')
    def get():
        global p
        p = input.get().lower()
        print(p)
        input.place_forget()
        cur.place(relx=0.5,rely=0.5,anchor='center')
        do()
        but['command'] = do
    but = Button(root, 
                    bg='#ffffff',
                    fg='#1abc9c',
                    relief='flat',
                    width=50,
                    text='Intentar',
                    font=('Roboto',15),
                    command=get,)
    cur = Label(root,fg="white",bg='#2abc9c',relief='flat',font=("Montserrat",30))
    etiqueta = Label(root,text="Apartat 10 @ 10 Intents",fg="#1abc9c",font=('Roboto',28))
    but.pack(side=BOTTOM)
    exit.pack(side=RIGHT,anchor="ne")
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
    ttk()
#pyinstaller --onefile -w --icon=icon.ico --name="AMPLIACIO" tkdemo.py