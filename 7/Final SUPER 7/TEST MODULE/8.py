#myobject = Assgn({0: ["jA","metres"],1:"d",2:"aa",3:"ff"},None,[False,True,True],"en")
from assgn import *     #Importa la class Assgn del altre document i totes les meves funcions
class eight:
    def vm():
        inputs = Assgn({0:("distancia","metres"),1:("temps","segons")},conj="en")
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
method_list = [method for method in dir(eight) if method.startswith('__') is False]
print(List2list(method_list),",")
