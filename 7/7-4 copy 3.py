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
    Dictionary to array
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
llista = []
valname = {
    0: ("la distància que recorres","metres"),
    1:("el temps que tardes en recorre aquesta distància","segons"),    #Un dictionary de tuples, meravellós.
    2:("radi de la roda","cm")
}
end = "\033[0;m"
err = "\n\u001b[41m"+"No has introduït un nombre vàlid"+"!\033[0;m"
chose = None
fvalue = None
def Assign(amount,load,offset,conj=""):
    try:                                                                #Verificar si els pàrametres són vàlids
        if float(offset).is_integer() and float(amount).is_integer():   #Primer es verificar si el valors són enters
            print("All working OK")
        else:
            print("Float was given, so it has become int")              #Sinó pasen a enters igualment:
        offset = int(offset)
        amount = int(amount)
        conj = str(conj)
        try:                                                            #Comprovem si el objecte donat és un dictionary
            for element in load.values():
                if isinstance(element, dict):
                    print("An error ocurred when checking if dict")     #No ho és
                    quit()
        except:
            print("An error ocurred when checking if dict")             #No ho és amb error
            quit()
    except ValueError:
        print("An error ocurred when NaN/Invalid entry was given")                    #Els valors d'abans no eren números
        quit()
    for x in range(amount):                                     #Ara ja està tot a punt, comença l'Assign
        llista.append(0)                                #Creem un lloc per a cada variable segons la quantitat demanada en l'array
    for i in range(amount):
        while True:
            try:
                ans = -1                            #Hem de verificar si és negatiu
                while not(ans > 0):
                    try:                        #Aquest try el faig per si de cas load fos None, que no és iterable
                        value = [x[1] for x in Dic2List(load)]
                    except:
                        print("An error ocurred in Dic2List")
                        quit()
                    magn = ":"  
                    if len(conj) > 0:
                        magn = " "+conj+" "+str(value[i+offset][1])+":"
                    ans = float(input(str(i+1)+". Introdueix "+str(value[i+offset][0])+magn)) #He convertit el dictionary loaded en un array de tuples: value[i+offset] i+ofsset és l'index del array de tuples => [0] o [1] és per establir si el primer valor del tuple o el segon.
                    if ans <= 0:                    #És negatiu, però gràcies al while True reiterarem la pregunta quant faci falta.
                        print(err)
                    else:
                        llista[i] = ans
                        print(List(llista,load))         #Convertim la llista en una string amb una funció local
            except ValueError:
                print(err)
                continue                            #No s'ha introduït un número, continuem 
            break               #Finalment, tot s'ha fet exitosament, trenquem el while.
"""    result = ""
    for l,x in enumerate(llista):
        result += valname[l]+" = "+str(llista[l])+"; "
    print(result)"""

def List(list,load):                                     #Converteix un array en un string
    value = [x[1] for x in Dic2List(load)]
    temp = "\u001b[44m"
    for i,j in enumerate(list):
        y = " "+end
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
def OddEven():
    inputs = {
        0: ("des d'ón","enter"),
        1: ("fins ón","enter")
    }
    Assign(2,inputs,0)
    odd = []
    even = []
    print("\n")
    for i in range(int(llista[0]),int(llista[1]+1)):
        if(i%2!=0):
            odd.append(i)
        else:
            even.append(i)
    def suma(list):
        t = 0
        for i in list:
            t += i
        return t
    print("\u001b[1m\u001b[4m\u001b[7mParells ("+str(len(even))+"):"+end)
    time.sleep(1)
    print(List2list(even))
    print(color.OKBLUE,"=",suma(even),end)
    time.sleep(1.4)
    print("\u001b[1m\u001b[4m\u001b[7mImparells ("+str(len(odd))+"):"+end)
    time.sleep(1)
    print(List2list(odd))
    print(color.OKGREEN,"=",suma(odd),end)
    time.sleep(1)
    print("Total:","(","des de:",int(llista[0]),";fins a:",int(llista[1]),")","\nImparells =",suma(odd),"Parells =",suma(even))
def write(name,b):
    f = "Factorial of "+str(a)+".txt"
    file = open(f,"w+")
def cotxe():                                            #I aquí l'interfaç de la màquina. Els paràmetres.
    cotxe = """                          ░░            ▓▓▓▓▓▓                  
                          ▒▒            ▓▓  ▓▓▓▓                
                        ▒▒▒▒            ▓▓    ▓▓▓▓              
                        ▒▒              ▓▓      ▓▓▓▓            
      ░░░░░░░░░░░░░░░░▒▒▒▒              ▓▓        ▓▓      ████  
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒██▓▓  
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒██▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒██▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒████  
▒▒▓▓████████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒██████▒▒▓▓▓▓        
▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██▓▓▓▓▓▓██▒▒▓▓        
██▓▓▓▓▒▒▒▒▓▓████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██▓▓▓▓▒▒▓▓▓▓██          
██▓▓▒▒▒▒▒▒▓▓████    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ██▓▓▒▒▒▒▒▒▓▓██          
██▓▓▓▓▒▒▒▒▓▓████                        ██▓▓▓▓▒▒▓▓▓▓██          
▓▓██▓▓▓▓▓▓▓▓██                            ██▓▓▓▓▓▓██            
  ▓▓████████                                ██████              
"""
    print("""
########  ####  ######  ########    ###    ##    ##  ######  ####    ###         ####       ######## ######## ##     ## ########   ######  
##     ##  ##  ##    ##    ##      ## ##   ###   ## ##    ##  ##    ## ##       ##  ##         ##    ##       ###   ### ##     ## ##    ## 
##     ##  ##  ##          ##     ##   ##  ####  ## ##        ##   ##   ##       ####          ##    ##       #### #### ##     ## ##       
##     ##  ##   ######     ##    ##     ## ## ## ## ##        ##  ##     ##     ####           ##    ######   ## ### ## ########   ######  
##     ##  ##        ##    ##    ######### ##  #### ##        ##  #########    ##  ## ##       ##    ##       ##     ## ##              ## 
##     ##  ##  ##    ##    ##    ##     ## ##   ### ##    ##  ##  ##     ##    ##   ##         ##    ##       ##     ## ##        ##    ## 
########  ####  ######     ##    ##     ## ##    ##  ######  #### ##     ##     ####  ##       ##    ######## ##     ## ##         ######  
""",end="")
    fvalue = [x[1] for x in Dic2List(valname)]
    Assign(3,valname,0,"en")
    dis = llista[0]
    temps = llista[1]
    rad = llista[2]/100
    velAng = dis/temps
    velAngR = (dis/2*math.pi)/temps
    VelAngRPM = (dis/(rad*math.pi))/(temps*60)
    VelHZ = (dis/(rad*math.pi))/(temps)
    print("\u001b[1m\u001b[4m\u001b[7m ")
    time.sleep(2)
    print(cotxe)
    time.sleep(4)
    print("Una roda de "+str(rad)+" "+str(fvalue[0][1])+" | "+str(rad*100)+" "+str(fvalue[2][1])+" de radi")
    time.sleep(.1)
    print("Una distància de: "+str(dis)+" "+str(fvalue[0][1]))
    time.sleep(.7)
    print("Tot això en "+str(temps)+" "+str(fvalue[1][1])+end)
    time.sleep(2)
    print("\nDona un total de:")
    results = [velAng,velAngR,VelAngRPM,VelHZ]
    for i in range(len(results)):
        value = namestr(results[i],locals())
        print(value[0]," = ",results[i])
OddEven()#START!
