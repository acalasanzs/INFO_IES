'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.1
'''
cont = 5
while cont >= 1:
    print(cont)
    cont -= 1
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.2
'''
cont = -5
while cont <= 0:
    print(cont)
    cont += 1
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.3
'''
casos = int(input("Quantes paraules vols introduïr? "))
print(casos)
cont = 0
while casos > 0:
    cont += 1
    print(input("Paraula "+str(cont)+" :"))
    casos -= 1
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.4 Factorial d'un nombre (Abans 6.1)
'''
def fact(a):
    progress = 0   #            Els comentaris, si els actives(els pases funcionals) fa una barra de progrés
    count = c = 1
    while count < a:
        count += 1
        c = count * c
        progress = (count/a)*100						#Això ho pots treure si no vols el percentatge de carga
        print(str(progress)+"%", end='\r')				#Això ho pots treure si no vols el percentatge de carga
    return c
print(fact(int(input("Factorial de (enter): "))))
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.4 Factorial d'un nombre (Abans 6.1) AMPLIFICAT
'''
import time
def fact(a):
    f = "Factorial of "+str(a)+".txt"
    file = open(f,"w+")
    done = "The factorial of " + str(a) +" is:\n"
    start = time.time()
    if a > 1:
        progress = 0   #            Els comentaris, si els actives(els pases funcionals) fa una barra de progrés
        count = c = 1
        while count < a:
            count += 1
            c = count * c
            progress = (count/a)*100
            progress = round(progress,2)        # Si no ho aproximo es buggeja
            pro = str(progress) + "%"
            print("Progress:  "+pro, end='\r')
        print()
        end = time.time()
        file.write(done)
        file.write(str(c))
        file.write("\n\nAlbert C.S. made this! Calc in "+str(end-start)+" seconds"+str(len(str(c)))+" digits")     #Final
        result = c
        if len(str(c)) > 50:
            result = str(c)[0:50]+"...\nThe Full Result is in the saved file!(Larger than 50 digits)"
        return result
    elif a == 1:
        result = "El factorial de 1 sempre és 1"
        file.write(result)
        return result
    else:
        file.write("Nombre no vàlid. Error: Menor que 0 o no és enter")
        return "Nombre no vàlid. Error: Menor que 0 o no és enter"
print(fact(int(input("Factorial de (enter): "))))
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
22/3/21 ; Pràctica 6.5
'''
casos = int(input("Quants nombres cal sumar? "))
print(casos," casos, d'acord.")
cont = n = 0
while casos > 0:
    cont += 1
    num = float(input("Nombre "+str(cont)+": "))
    print(num)
    n += num
    casos -= 1

print("Total:",n)



'''
Nota:

el 6.4 l'he fet dos cops: 
el primer és el bàsic i el segon fins i tot et crea un .txt que et diu el temps que ha tardat en calcular-ho junt amb el resultat complert.

Ja sé que no es demanava i sempre faig 1000 de vegades més del que es demana, però em feia il·lusió i m'ho he demanat a mi mateix. Deuries de posar alguna més difícil pq no ampliés tant del que es demana.
'''