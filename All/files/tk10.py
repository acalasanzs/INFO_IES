"""
Joc de l'ampliació de l'apartat 10

Albert Calasanz | acsstudios
Python > 3.5
"""
from tkinter import *
import random
def ttk():
    lletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  #Abecedari

    #Funcio de perdre

    def lose():
        print("YOU LOSE")
        los = Label(root,text="YOU lose!",font=("Montserrat",40),fg="red")
        los.pack(side=BOTTOM,anchor="center",pady=20,padx=20,expand=1)
        but.pack_forget()
        cur.place_forget()
    
    #Funcio de guanyar

    def win():
        print("YOU WIN")
        wi = Label(root,text="YOU WIN!",font=("Montserrat",40),fg="green")
        wi.pack(side=BOTTOM,anchor="center",pady=20,padx=20,expand=1)
        but.pack_forget()
        cur.place_forget()

    # Crea un frame WPF personalitzat
    class Application(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master, highlightbackground="#1abc9c")
            self.parent = master

    #Es crea un Tk
    root = Tk()
    root.overrideredirect(1)                                                            #Si es 1 treu la finestra clasica però si es 0 és classic. Prova de canviar-ho!
    root.geometry('800x250+400+180')                                                    #Apareix a: (400,180) de la pantalla amb forma de 800x250
    #Configurar fons
    app = Application(root)
    app.parent.configure(background = '#1abc9c')
    #Prevent resize
    root.resizable(width=False, height=False)

    # matches es una variable que conserva totes les lletres seleccionades, pero tindre memoria del que s'ha triat
    matches = []
    #Poso a global p,temp,intents,a,max per la funció do()
    global p,temp,intents,a,max
    #Intents maxims en el que es perd o es guanya
    max = 10
    #Lletra current
    a = "-"
    #Abecedari modificat, clletres es una copia per anar esborrant de l'espectre d'elecció random
    clletres = lletres
    temp = "-"
    #Comptador
    intents = 0
    def do():
        #global per tindre el namespace global
        global p,temp,intents,a,max
        #Cambiar fons del botó
        but['fg'] = "#8e44ad"

        #Si els intents no supera el max:
        if intents < max:
            intents += 1
            #Seleccionar una lletra de l'abecedari i afegirla a matches, per després elimanrla de clletres(No repetir la mateixa elecció)
            a = random.choice(clletres)
            matches.append(a)
            clletres.remove(a)
            #Cambiar el botó per mostar-hi els intents
            but['text'] = "Tornar-hi ({}) lletra: {}".format(intents,a)
            #Current es una copia de 'p', que es la paraula entrada
            current = p
            #Una mostra visual de l'abecedari
            abec = "abdefghijklmnñopqrstuvwxyz"
            #convertir en '-' tot el no sigui seleccionat
            for i in matches:
                abec = abec.translate({ord(i): "-"})
            #convertir en '-' l'abecedari visual (No s'utilitza en el progama)
            for x in abec:
                p = p.translate({ord(x): "-"})
            #imprimir per consola y cambiar el Label central
            print(p,"|",abec)
            temp = p
            cur['text'] = temp+"\n"+abec
            p = current
            #Si s'ha acabat la paraula
            if not("-" in temp):
                win()

        else:
            #Si no ho aconseguit
            lose()
            but.configure(text="YOU LOSE",
                        fg="red",
                        padx=20,
                        command=lose)
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
    inputf = Label(root,fg="white",text="Enter a word:",bg='#1abc9c',relief='flat',font=("Helvetica",15))
    inputf.place(relx=0.5,rely=0.35,anchor="center")
    def get():
        global p
        p = input.get().lower()
        print(p)
        input.place_forget()
        inputf.place_forget()
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
    but.pack(side=BOTTOM,fill=X)
    exit.pack(side=RIGHT,anchor="ne")
    etiqueta.pack(side=TOP,fill=X)
    main = Label(root,text="")

    root.mainloop()
if __name__ == "__main__":
    ttk()