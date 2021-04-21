import os
os.system("")

'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.ampliació
'''
# Comentari del script:
# Aquest script realitza el demanat amb un disseny del terminal i efectivitat impresionants
# Si em demaneu per l'autovaloració: 9999/10

# Bé, el que fa aixó básicament és realitzar 5 vegades => demanar 5 vegades un nombre per sumar-ho tot plegat
# És a dir, dos iteracions
# Un cop es finalitza l'Iteracio1 s'imprimeix un resum de tot(EXTRA)
mem = 0                             #Memoria de resultats (EXTRA)
memx = ""                           #Memoria de la suma string(EXTRA)
memr = []                           #Memoria dels resultats + string(EXTRA)

Iteracio1 = range(5)                    #He dividit el range del for en aquesta variable, per que TU puguis cambiar-ho desde aquí i afectar a tot el progama
Iteracio2 = range(5)                    #He dividit el range del for en aquesta variable, per que TU puguis cambiar-ho desde aquí i afectar a tot el progama
I1=str((Iteracio1[-1])+1)               #Això és per saber el número final del range
I2=str((Iteracio2[-1])+1)               #Això és per saber el número final del range
for x in Iteracio1:
    l=""
    if x == 0:
        print("\033[1;32;40mIteració configurada a "+I1+"\033[0m")  #Com he dit abans, aquí imprimeix el range configurat en la variable Iteracio1
    if x > 0:
        l=" + "                                                     #Si la iteració current és major que 0, afegir un signe + al string
        print("______________________________")
    print(str(x+1)+" de "+I1+". Introduir "+str((Iteracio2[-1])+1)+" valors: ")
    b = []
    for x in Iteracio2:
        inp = "Introdueix valor "+str(x+1)+": "
        a = int(input(inp))
        b.append(a)
    else:
        x = ""
        for i,j in enumerate(b):                                    #Així pots puc fer una llista
            if i < Iteracio2[-1]:
                x=x+str(b[i])+" + "
            else:
                x=x+str(b[i])
        else:
            res = x+" = "+str(sum(b))
            memr.append(res)
            print(res)
            mem = sum(b) + mem
            memx = memx +l+ x
else:
    print("\033[1;32;40m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(""" /$$$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$
| $$_____/| $$  / $$|__  $$__/| $$__  $$ /$$__  $$| $$
| $$      |  $$/ $$/   | $$   | $$  \ $$| $$  \ $$| $$
| $$$$$    \  $$$$/    | $$   | $$$$$$$/| $$$$$$$$| $$
| $$__/     >$$  $$    | $$   | $$__  $$| $$__  $$|__/
| $$       /$$/\  $$   | $$   | $$  \ $$| $$  | $$    
| $$$$$$$$| $$  \ $$   | $$   | $$  | $$| $$  | $$ /$$
|________/|__/  |__/   |__/   |__/  |__/|__/  |__/|__/
                                                      \033[0m""")
                                                      
    print("Total del tot els valors introduits: ")
    print(memx,mem,sep=" = ", end="""
    ::::::::::::::::::::::::::::::::::::::::::::
        
        """)
    print("Resum de totes les iteracions: "+"(Iteracio 1: \033[1;32;40m"+I1+"\033[0m,Iteració 2: \033[1;32;40m"+I2+"\033[0m)")
    for i,j in enumerate(memr):
        sa = "\033[2;30;47m"+str(i+1)+": \033[0m"
        print("""        """+sa+str(j))
#Seria massa escriure documentar tot el script, quina mandra...