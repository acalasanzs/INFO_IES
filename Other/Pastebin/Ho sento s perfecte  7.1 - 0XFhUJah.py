'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 7.1 Càlcul de volums
'''
import math
listo = []
xyz = {
    0: "x",
    1:"y",
    2:"z",
    3:"radi",
    4:"alçada",
}
err = "\033[4;35m"+"No has introduït un nombre vàlid"+"\033[0;m!"
def XYZ(am,off):
    for x in range(am):
        listo.append(0)
    for i in range(am):
        while True:
            try:
                tr = -1
                while not(tr > 0):
                    #val = [x[0] for x in listo]
                    tr = float(input(str(i+1)+". Introdueix "+xyz[i+off]+" en metres: "))
                    if tr <= 0:
                        print(err)
                    else:
                        listo[i] = tr
                        print(listo)
            except ValueError:
                print(err)
                continue
            break
    result = ""
    for l,x in enumerate(listo):
        result += xyz[l]+" = "+str(listo[l])+"; "
    print(result)
    

# OPCIONS
def Cub():
    XYZ(3,0)
    res = 1
    for i,item in enumerate(listo):
        res *= listo[i]
    res = "Volum del cub: "+str(res)+" m^3"
    print("___________________________________\n")
    print(res)
def Cilindre():
    XYZ(2,3)
    res = ((math.pi)*listo[0]**2)*listo[1]
    print("___________________________________\n")
    print("Volum del cilindre: "+str(res)+" m^3")
def Con():
    XYZ(2,3)
    res = (((math.pi)*listo[0]**2)*listo[1])/3
    print("___________________________________\n")
    print("Volum del cilindre: "+str(res)+" m^3")
def Esfera():
    XYZ(1,3)
    res = (math.pi)*(3/4)*(listo[0]**3)
    print("___________________________________\n")
    print("Volum del cilindre: "+str(res)+" m^3")







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
print("Opcions disponibles en el paquet: \n"+List2list(Dic2List(options))+"\n")
while not(a in options):
    try:
        a = int(input("Què vols calcular, número?: "))
        if not(a in options):
            print("\n\033[1;33mHas d'introduïr dintre de:\n"+List2list(Dic2List(options))+"!\033[0;m\n")
    except ValueError:
        print("Posa un número!")
print("Has triat:",Dic2List(options)[a-1])
globals()[options[a]]()