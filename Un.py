'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 7.3 Distància recorreguda per una roda
'''
'''
TODO:
    Càlculs de velocitat angular en cotxe()
'''
import math                             #Així podem tindre la constant pi
llista = []
valname = {
    0: ("la distància que recorres","metres"),
    1:("el temps que tardes en recorre aquesta distància","segons"),    #Un dictionary de tuples, meravellós.
    2:("radi de la roda","cm")
}
end = "\033[0;m"
err = "\n\u001b[41m"+"No has introduït un nombre vàlid"+"!\033[0;m"
chose = None
def Assign(amount,load,offset):
    try:                                                                #Verificar si els pàrametres són vàlids
        if float(offset).is_integer() and float(amount).is_integer():   #Primer es verificar si el valors són enters
            print("All working OK")
        else:
            print("Float was given, so it has become int")              #Sinó pasen a enters igualment:
        offset = int(offset)
        amount = int(amount)
        try:                                                            #Comprovem si el objecte donat és un dictionary
            for element in load.values():
                if isinstance(element, dict):
                    print("An error ocurred when checking if dict")     #No ho és
                    quit()
        except:
            print("An error ocurred when checking if dict")             #No ho és amb error
            quit()
    except ValueError:
        print("An error ocurred when NaN was given")                    #Els valors d'abans no eren números
        quit()
    for x in range(amount):                                     #Ara ja està tot a punt, comença l'Assign
        llista.append(0)                                #Creem un lloc per a cada variable segons la quantitat demanada en l'array
    for i in range(amount):
        while True:
            try:
                ans = -1                            #Hem de verificar si és negatiu
                while not(ans > 0):
                    value = [x[1] for x in Dic2List(load)]
                    ans = float(input(str(i+1)+". Introdueix "+str(value[i+offset][0])+" en "+str(value[i+offset][1])+":")) #He convertit el dictionary loaded en un array de tuples: value[i+offset] i+ofsset és l'index del array de tuples => [0] o [1] és per establir si el primer valor del tuple o el segon.
                    if ans <= 0:                    #És negatiu, però gràcies al while True reiterarem la pregunta quant faci falta.
                        print(err)
                    else:
                        llista[i] = ans
                        print(List(llista))         #Convertim la llista en una string amb una funció local
            except ValueError:
                print(err)
                continue                            #No s'ha introduït un número, continuem
            break               #Finalment, tot s'ha fet exitosament, trenquem el while.
"""    result = ""
    for l,x in enumerate(llista):
        result += valname[l]+" = "+str(llista[l])+"; "
    print(result)"""

def List(list):                                     #Converteix un array en un string
    value = [x[1] for x in Dic2List(valname)]
    temp = "\u001b[44m"
    for i,j in enumerate(list):
        y = " "+end
        if i < 2:
            y = " i "
        temp += str(j) +" "+ str(value[i][1]) + y
    return temp
def Dic2List(dict):                                 #Aquesta funció converteix un dictionary en una array personalitzada
    dictlist = []
    for key, value in dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return 


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
    Assign(3,valname,0)
    dis = llista[0]
    temps = llista[1]
    velAng = dis/temps
    velAngR = (dis/2*math.pi)/temps
    # 
    print("\u001b[1m\u001b[4m\u001b[7m ")
    print(cotxe)
    print("Una roda de "+str(llista[0])+" metres de radi")
    print("recorre "+str(circ*llista[1])+" m\u001b[0m CADA "+str(llista[1])+" voltes que dona")
cotxe()                                                                                         #START!