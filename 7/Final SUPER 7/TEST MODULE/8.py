#myobject = Assgn({0: ["jA","metres"],1:"d",2:"aa",3:"ff"},None,[False,True,True],"en")
from assgn import Assgn
def vm():
    inputs = Assgn({0:("distancia","metres"),1:("temps","segons")},None,None,"en")
    res = inputs.llista[0]/inputs.llista[1]
    print("Result = {} m/s".format(res))
def km2ms():
    res = int(input("Introdueix kmh o ms: "))
    while not(res in (1,2)):
        print(mess.err)
        res = int(input("Introdueix kmh o ms: "))
    if res == 1:
        return "Ans = {} m/s".format(float(input("kmh?"))/3.6)
    else:
        return "Ans = {} km/h".format(float(input("ms?"))*3.6)
def ciclista():
    res = Assgn({0:["Distancia","metres"],1:["Velocitat","m/s"]},conj = "en")
def VelocitatSo():
    return "És supersónic" if int(input("Km/h?(Avió)"))*3.6 >= 340 else "No ho és"
def f85():
    dic = Ar2Dict(["Cotxe 1","Cotxe 2"],"km/h")
    dic[2] = ("Temps","hores")
    valors = Assgn(dic,conj="en")
    a = valors.llista[0]*valors.llista[2]
    b = valors.llista[1]*valors.llista[2]
    print("Els separa {} km".format(abs(a-b)))
def Ar2Dict(ar,ma):
    r = []
    for x in ar:
        r.append((x,ma))
    dic = dict((key,r[key]) for key in range(len(ar)))
    return dic
f85()
