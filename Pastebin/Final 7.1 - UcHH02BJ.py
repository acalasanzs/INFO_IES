'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 7.1 Càlcul de volums
'''
import math
llista = []
valname = {
    0: "x",
    1:"y",
    2:"z",
    3:"radi",
    4:"alçada",
}
end = "\033[0;m"
err = "\n\u001b[41m"+"No has introduït un nombre vàlid"+"!\033[0;m"
chose = None
def Assign(am,off):
    for x in range(am):
        llista.append(0)
    for i in range(am):
        while True:
            try:
                ans = -1
                while not(ans > 0):
                    #val = [x[0] for x in llista]
                    ans = float(input(str(i+1)+". Introdueix "+valname[i+off]+" en metres: "))
                    if ans <= 0:
                        print(err)
                    else:
                        llista[i] = ans
                        print(llista)
            except ValueError:
                print(err)
                continue
            break
    result = ""
    for l,x in enumerate(llista):
        result += valname[l]+" = "+str(llista[l])+"; "
    print(result)
    

# OPCIONS
def Cub():
    Assign(3,0)
    res = 1
    for i,item in enumerate(llista):
        res *= llista[i]
    ResultP(res)
def Cilindre():
    Assign(2,3)
    res = ((math.pi)*llista[0]**2)*llista[1]
    ResultP(res)
def Con():
    Assign(2,3)
    res = (((math.pi)*llista[0]**2)*llista[1])/3
    ResultP(res)
def Esfera():
    Assign(1,3)
    res = (math.pi)*(3/4)*(llista[0]**3)
    ResultP(res)


def ResultP(res):
    print("___________________________________\n")
    print("Volum del "+str(chose)+": "+str(res)+" m^3")






a = 0
options = {
    1: "Cub",
    2: "Cilindre",
    3: "Con",
    4: "Esfera"
}
def Dic2List(dict):
    dictlist = []
    for key, value in dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist
def List2list(list):
    t = [x[0] for x in list]
    z = [x[1] for x in list]
    temp = ""
    for i,j in enumerate(list):
        temp += "( "+str(t[i])+": "+str(z[i])+" )"
    return temp
print("\033[95mOpcions disponibles en el paquet: \n"+List2list(Dic2List(options))+"\n"+end)
while not(a in options):
    try:
        a = int(input("\u001b[44mQuè vols calcular, número paquet?: "+end))
        if not(a in options):
            print("\u001b[43mHas d'introduïr dintre de:\n"+List2list(Dic2List(options))+"!\033[0;m\n")
    except ValueError:
        print("Posa un número!")
print("\u001b[42mHas triat:"+str(Dic2List(options)[a-1])+end)
chose = Dic2List(options)[a-1][1]
globals()[options[a]]()

# He pensat en fer un class per classificar totes les def de formules, però ja en tinc prou