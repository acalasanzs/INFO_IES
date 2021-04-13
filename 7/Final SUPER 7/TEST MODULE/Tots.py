#myobject = Assgn({0: ["jA","metres"],1:"d",2:"aa",3:"ff"},None,[False,True,True],"en")
from assgn import *     #Importa la class Assgn del altre document i totes les meves funcions
import math
class Tots_Els_Apartats:
    class Set_1:
        def cub():
            ask = Assgn(Ar2Dict(["x","y","z"],"metres"),conj="en")
            res = 1
            for i in ask.llista: res *= i
            return "{} m^3".format(res)
        def cilindre():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return "{} m^3".format(((math.pi)*ask.llista[0]**2)*ask.llista[1])
        def con():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return ""(((math.pi)*ask.llista[0]**2)*ask.llista[1])/3
        def esfera():
            ask = Assgn(Ar2Dict(["radi"],"metres"),conj="en")
            return (math.pi)*(3/4)*(ask.llista[0]**3)
    class Vuit_1:
        def vm():
            inputs = Assgn({0:("distancia","metres"),1:("temps","segons")},conj="en")
            res = inputs.llista[0]/inputs.llista[1]
            return "Result = {} m/s".format(res)
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
            return "Els separa {} km".format(abs(a-b))



def optionsinclass(cls):
    method_list = [method for method in dir(cls) if method.startswith('__') is False]
    print("Options in {}: {}{} {}".format(cls.__name__,color.b.blue,List2list(method_list,", "),color.end))
    if len(method_list) < 1: mess.Empty()
    res = int(input("Index? "))
    while not(res in range(len(method_list))):
        print(mess.err)
        res = int(input("Index? "))
    return getattr(cls,method_list[res])
def classMehtod(cls):
    print(optionsinclass(cls)())
classMehtod(optionsinclass(Tots_Els_Apartats))