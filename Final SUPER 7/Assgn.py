def List(list,load):                                     #Converteix un array en un string
    value = [x[1] for x in Dic2List(load)]
    temp = color.b.blue
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
class color:
    class t:
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
    class b:
        red = "\u001b[41m"
        blue = "\u001b[44m"
    end = "\033[0;m"
class mess:
    err = f"{color.b.red}No has introduït un nombre vàlid{color.end}"
    def Valerr():
        print(f"{color.b.red}An error ocurred when NaN/Invalid entry was given{color.end}")                    #Els valors d'abans no eren números
        quit()
    def DictErr():
        print(f"{color.b.red}An error ocurred when checking if dict{color.end}")         
        quit()
    def Dict2ListErr():
        print(f"{color.b.red}An error ocurred in Dic2List{color.end}")
        quit()
    def InvalidOpt():
        print(f"{color.b.red}Srry sir, there ins't that option{color.end}")
        quit()
    def optionAsks():
        print(f"{color.b.red}Dict not found{color.end}")
        quit()

class Assgn():
    "Makes n inputs and stores them into object list. Rules [A0,A-,OInt] or 'str'"
    def __init__(self,load=None,rang=None,rules=None,conj=""):
        self.AllowStr = False
        self.value = []
        self.ans = None
        self.rules = rules
     # Comprovar les rules
        self.conj = "" if type(conj) is not str else conj
"""         if type(conj) is not str: 
            self.conj = ""
        else:
            self.conj = conj """
        if rules is None:
            self.rules = [False,False,False]
        elif (type(rules) is list) and (len(rules) == 3):
            if all(i in(True,False) for i in rules):
                pass
            else:
                print("Error on rules")
                mess.Valerr()
        elif rules == "str":
            self.rules = [False,False,False]
            self.AllowStr = True
        else:
            print(color.b.red+"Error in rules input\nAll will become false"+color.end)
        # Comprovar les rules
        self.ln = False
        if load is None: self.ln = True
        if not(type(load) is dict) and not(self.ln):                                 #Verificar si load is dict
            print("Line 98")
            mess.DictErr()
        else:
            self.load = load
            if type(load) is dict:
                for x in load:
                    if not(type(x) is tuple):
                        print(mess.DictErr+"Must be tuple")
            elif type(load) is list:
                self.load = dict.fromkeys(load,"")                                  # Si el dict és llista passa a dict
        #---------------------------------------------------------------------------------------
        if isinstance(rang,range):
            if not(len([x for x in rang]) > 0):
                mess.Valerr()
            else:
                self.rang = rang
            if self.ln:
                self.llista = ["" for x in self.rang] if self.AllowStr else [0 for x in self.rang]
        elif rang is None and (len(load)>0):
            self.rang = range(len(load))
            self.llista = [0 for x in self.rang]
        else:
            mess.Valerr()
        self.input()
    def input(self):
        # HEADER
        print(color.t.OKGREEN+"Set of {} questions".format(len(self.llista))+"\nAllow 0:{},Allow Negative:{},Allow String:{},Only Int: {}".format(self.Allow0,self.AllowNegative,self.AllowStr,self.OnlyInt)+color.end)
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
                        if not(self.ln):
                            self.value = [x[1] for x in Dic2List(self.load)]
                            b = self.value[i][1]
                            a = self.value[i][0]
                        if len(self.conj) > 0: magn = " "+self.conj+" "+str(b)+":"
                        if self.AllowStr:
                            ans = str(input(str(i+1)+". Introdueix "+str(a)+magn))
                            self.llista[i] = ans
                            result = self.llista
                            if not(self.ln):
                                result = List(self.llista,self.load)
                            print(result)
                        else:
                            if self.OnlyInt:
                                ans = int(input(str(i+1)+". Introdueix "+str(a)+magn))
                            else:
                                ans = float(input(str(i+1)+". Introdueix "+str(a)+magn)) #He convertit el dictionary loaded en un array de tuples: value[i+offset] i+ofsset és l'index del array de tuples => [0] o [1] és per establir si el primer valor del tuple o el segon.
                            if ans <= 0 and not(self.Allow0) and not(self.AllowNegative):                    #És negatiu, però gràcies al while True reiterarem la pregunta quant faci falta.
                                print(mess.err)
                            elif ans < 0 and not(self.AllowNegative) and self.Allow0:
                                print(mess.err)
                            else:
                                self.llista[i] = ans
                                result = self.llista
                                if not(self.ln):
                                    result = List(self.llista,self.load)
                                print(result)
                    except ValueError:
                        print(mess.err)
                        continue
                    break
                self.ans = ans
            print(self.rules)
            if self.rules is None:
                self.ans = None
                while self.ans is None:
                    whilefunct()
            else:
                if self.AllowStr:
                    self.ans = ""
                    while not(len(self.ans)>0):
                        whilefunct()
                else:
                    if not(self.AllowNegative) and self.Allow0:
                        self.ans = -1                            #Hem de verificar si és negatiu
                        while not(self.ans > 0): whilefunct()
                    elif not(self.Allow0) and self.AllowNegative:
                        self.ans = 0
                        while not(self.ans >= 0): whilefunct()
    def dispValues(self):
        for i,j in enumerate(self.llista):
            if not(self.ln):
                self.value = [x[1] for x in Dic2List(self.load)]
                b = self.value[i][1]
                a = self.value[i][0]
                print(a,j,b)
            else:
                print("Valor",i,"=",j,";","Type: {}".format(type(j).__name__))
    def __str__(self):
        conj = self.conj
        if conj == "": conj = "<None>"
        return color.t.OKCYAN+"Rules\nA0{},A-{},AStr{},OnlInt{}".format(self.Allow0,self.AllowNegative,self.AllowStr,self.OnlyInt)+"\n"+color.end+"\nconj: {},\nrang: {},\n\nquestions: {},\n\nInputs: {}".format(conj,self.rang,self.value,self.llista)
myobject = Assgn(None,range(5),[False,True,True])