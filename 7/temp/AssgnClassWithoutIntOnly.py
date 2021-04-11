import os
os.system("")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 7.4 Suma els números parells i imparells PROOF
'''
"""
TODO:
    Default args in Assign DONE
    Classes
"""
import math                             #Així podem tindre la constant pi
import time
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    end = "\033[0;m"
    err = "\n\u001b[41m"
class mess:
    err = "\n\u001b[41m"+"No has introduït un nombre vàlid"+"!\033[0;m"
    def Valerr():
        print("An error ocurred when NaN/Invalid entry was given")                    #Els valors d'abans no eren números
        quit()
    def DictErr():
        print("An error ocurred when checking if dict")         
        quit()
    def Dict2ListErr():
        print("An error ocurred in Dic2List")
        quit()
valname = {
    0: ("la distància que recorres","metres"),
    1:("el temps que tardes en recorre aquesta distància","segons"),    #Un dictionary de tuples, meravellós.
    2:("radi de la roda","cm")
}
""" chose = None
fvalue = None """

print("\n\n___________________________________________")
# Functions
def List(list,load):                                     #Converteix un array en un string
    value = [x[1] for x in Dic2List(load)]
    temp = "\u001b[44m"
    for i,j in enumerate(list):
        y = " "+color.end
        if i < len(load)-1:
            y = " i "
        temp += str(j) +" "+ str(value[i][1]) + y
    return temp
def Dic2List(dict):                                 #Aquesta funció converteix un dictionary en una array personalitzada
    dictlist = []
    for key, value in dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
def List2list(list):
    temp = ""
    for i,item in enumerate(list):
        conj = " + "
        if(i>=len(list)-1):
            conj = ""
        temp += str(list[i])+conj
    return temp



class Assgn():
    "Makes n inputs and stores them into object list"
    def __init__(self,load=None,rang=None,conj="",rules=None):
        global ln
        self.AllowNegative = False
        self.Allow0 = False
        self.AllowStr = False
        #self.OnlyInt = False
        self.value = []
        self.ans = None
        if conj is None: conj = ""
        if rules is None:
            pass
        elif (type(rules) is list) and (len(rules) == 3):
            print(len(rules))
            if all(i in(True,False) for i in rules):
                self.Allow0 = rules[0]
                self.AllowNegative = rules[1]
                self.AllowStr = rules[2]
                if self.AllowStr:
                    self.AllowNegative = False
                    self.Allow0 = False
            else:
                print("Error on rules")
                mess.Valerr()
        else:
            print(color.err+"Error in rules input")
            print("All will become false"+color.end)
        ln = False
        if load is None: ln = True
        if not(type(load) is dict) and not(ln):                                 #Verificar si load is dict
            mess.DictErr()
        else:
            self.load = load
            if type(load) is dict:
                for x in load:
                    if not(type(x) is tuple):
                        print(mess.DictErr+"Must be tuple")
            elif type(load) is list:
                self.load = dict.fromkeys(load,"")
        #---------------------------------------------------------------------------------------
        if isinstance(rang,range):
            if not(len([x for x in rang]) > 0):
                mess.Valerr()
            else:
                self.rang = rang
            if ln: self.llista = [0 for x in self.rang]
        elif rang is None and (len(load)>0):
            self.rang = range(len(load))
            self.llista = [0 for x in self.rang]
        else:
            mess.Valerr()
        try:                                                                #Verificar si els pàrametres són vàlids
            self.conj = str(conj)
        except ValueError:
            mess.Valerr()
        self.input()
    def input(self):
        print(color.OKGREEN+"Set of {} questions".format(len(self.llista))+"\nAllow 0:{},Allow Negative:{},Allow String:{}".format(self.Allow0,self.AllowNegative,self.AllowStr)+color.end)
        for i in self.rang:
            if i < 0:
                mess.Valerr()
            def whilefunct():
                while True:
                    try:
                        global ans
                        magn = ":" 
                        a = "valor "+str(i+1)
                        b = " "
                        self.value = [x+1 for x in self.rang]
                        if not(ln):
                            self.value = [x[1] for x in Dic2List(self.load)]
                            b = self.value[i][1]
                            a = self.value[i][0]
                        if len(self.conj) > 0: magn = " "+self.conj+" "+str(b)+":"
                        if self.AllowStr:
                            ans = str(input(str(i+1)+". Introdueix "+str(a)+magn))
                            self.llista[i] = ans
                            result = self.llista
                            if not(ln):
                                result = List(self.llista,self.load)
                            print(result)
                        else:
                            ans = float(input(str(i+1)+". Introdueix "+str(a)+magn)) #He convertit el dictionary loaded en un array de tuples: value[i+offset] i+ofsset és l'index del array de tuples => [0] o [1] és per establir si el primer valor del tuple o el segon.
                            if ans <= 0 and not(self.Allow0) and not(self.AllowNegative):                    #És negatiu, però gràcies al while True reiterarem la pregunta quant faci falta.
                                print(mess.err)
                            elif ans < 0 and not(self.AllowNegative) and self.Allow0:
                                print(mess.err)
                            else:
                                self.llista[i] = ans
                                result = self.llista
                                if not(ln):
                                    result = List(self.llista,self.load)
                                print(result)
                    except ValueError:
                        print(mess.err)
                        continue
                    break
                self.ans = ans
            if not(self.AllowNegative) and self.Allow0 and not(self.AllowStr):
                print("Not negative and 0")
                self.ans = -1                            #Hem de verificar si és negatiu
                while not(self.ans > 0): whilefunct()
            elif not(self.Allow0) and self.AllowNegative and not(self.AllowStr):
                self.ans = 0
                while not(self.ans >= 0): whilefunct()
            elif self.AllowStr:
                self.ans = ""
                while not(len(self.ans)>0):
                    whilefunct()
            else:
                self.ans = None
                while (self.ans == None):
                    whilefunct()
    def dispValues(self):
        for i,j in enumerate(self.llista):
            if not(ln):
                self.value = [x[1] for x in Dic2List(self.load)]
                b = self.value[i][1]
                a = self.value[i][0]
                print(a,j,b)
            else:
                print("Valor",i,"=",j,";","Type: {}".format(type(j).__name__))
    def __str__(self):
        return "Assign set: Allow 0:{},Allow Negative:{},Allow String:{}".format(self.Allow0,self.AllowNegative,self.AllowStr)+"\n__________________________________________"+"\nconj: {},\nrang: {},\n\nquestions: {},\n\nllista: {}".format(self.conj,self.rang,self.value,self.llista)
cube = Assgn(None,range(2),None,[True,False,True])
cube.dispValues()
class Polygon(Assgn):
    def __init__(self,sides,operation="self.llista[0]*self.llista[1]*self.llista[2]"):
        Assgn.__init__(self,None,range(sides),None,[False,False])
        Assgn.input()
        print(eval(operation))