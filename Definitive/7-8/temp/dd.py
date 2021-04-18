import tkinter
from assgn import *
def Triangles():
    global seen
    global A,B,C
    print("Torna el tipus de triangle segons els seus costats i els seus angles respectius (A,B,C)")
    ask = Assgn(rang=range(3))
    seen = []
    c = 1
    for x in ask.llista:
        if x in seen:
            c += 1
        seen.append(x)
    if c == 1:
        print("Escalé")
    elif c == 2:
        print("Isosceles")
    elif c == 3:
        print("Equilater")
    a,b,c = seen
    try:
        """ alpha.SetValue(180 * Math.acos((b * b + c * c - a * a) / (2 * b * c)) / Math.PI);
            beta.SetValue(180 * Math.acos((a * a + c * c - b * b) / (2 * a * c)) / Math.PI);
            gamma.SetValue(180 * Math.acos((a * a + b * b - c * c) / (2 * a * b)) / Math.PI); """
        A = math.acos((b * b + c * c - a * a) / (2 * b * c))                                                #Alpha
        B = math.acos((a * a + c * c - b * b) / (2 * a * c))                                                #Beta
        C = math.acos((a * a + b * b - c * c) / (2 * a * b))                                                #Gamma
        for i in [A,B,C]:
            print(namestr(i,locals())[0],"=",str(math.degrees(i))+"º","radians:",i)
        return ""
    except:
        print(color.b.red,"Aquest triangle no existeix XD",color.end)
        Triangles()
    def xy(ad,an):
        x = math.cos(math.radians(an))*ad
        y = math.sin(math.radians(an))*ad
        return (x,y)
    a = xy(a,A)
    print(a)
    b = xy(b,B)
    c = xy(c,C)
Triangles()
top = tkinter.Tk()
Can = tkinter.Canvas(top, bg="white", height=300, width=300)
Can.create_line(55, 85, 155, 85, 105, 180, 55, 85)
Can.pack()
top.mainloop()