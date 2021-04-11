# Aquest Paste recopila tots els scripts de Python de la primera part
# Per tant, s'haurá de copiar exercici per exercici per a verificar el seu funcionament. (Està tot junt)



'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.1
'''

num = float(input("Número: "))
if (num%1)==0:
   print(num)
else:
    print('No és enter ')


'''
________________________________________________________________________________________
Albert Calasanz ; 4tB
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Practica 1.2
'''
num = float(input("Digues un número real: "))
a = " és enter"										# Assigna la resposta a
c = " no és enter"									# Assigna la resposta c
# b= str(num)+a	Resposta Completa
if (num%1)==0:
    b= str(num)+a									# Assigna resposta del a al b
    print (b)
else:
    b= str(num)+c									# Assigna resposta del c al b
    print (b)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.3
'''
T = 0												#S'assigna 0 per donar a terme el while
while T == 0:               						#No admeteix 0
    T = len(input("Introdueix més de 0 caràcters: "))
if (T==1):											#Si es 0 torna un text
    print('Has posat un caràcter')
else:
    print('Has posat un text de ',T,' caràcters')
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.4
'''
print("Introdueix 0/1:")                            #Pregunta inicial
a = input()
while not(a.isdigit()):                             #Amb la funció .isdigit() s'evita l'error del float, el while es per reiterar la pregunta fins que s'obtingui un valor válid
    a = input("Introdueix un número!")              #No s'ha introduit cap valor float
if not(float(a) in (1,0)):
    while not(float(a) in (1,0)):
        a = input("Introdueix 0/1 d'una vegada!")   #S'ha introduit un número(float), però no és 1 o 0
if float(a) == 1 or float(a) == 0:
    if float(a):
        print(True)
    else:
        print(False)                                # Finalment s'ha introduit un valor válid (1,0)

#Disculpeu per si el códig era innecessari, però volia que reiterès la pregunta fins a resoldre's. XD. P.D: Això pot comptar com ampliació

'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.5
'''
a = float(input("Número a: "))
b = float(input("Número b: "))
c = float(input("Número c: "))
num = [a,b,c]

print(max(num))										#amb la funció max() m'estalvio tot els if
# Què minimalista, veritat?
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.6
'''
a = str(input("Paraula 1: "))						#Passem el input a string
b = str(input("Paraula 2: "))
p = [a,b]											#Fem un array
l = max(p,key=len)									#Assignem la més llarga
if len(a) == len(b):								#Però en el cas que totes dues siguin igual de llarges, mostrem la primera.
    l = "Totes paraules són iguals, 1a: " + a
else:
    l = "La paraula més llarga és: " + l
print(l)											#Finalment s'imprimeix el resultat final.