'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.1
'''
n = int(input("Introdueix un nombre: "))
if n == 20:
    print("És igual a 20")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.2
'''
n = int(input("Introdueix un nombre: "))
if n > 20:
    print("És més gran que 20")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.3
'''
n = int(input("Introdueix un nombre: "))
if n < 20:
    print("És menor que 20")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.4
'''
n = int(input("Introdueix 1r nombre: "))
p = int(input("Introdueix 2n nombre: "))
if n > p:
    print(n)
else:
    print(p)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.5
'''

n = int(input("Introdueix un nombre: "))
if n <= -10 or n>= 10:
    print("El nombre té més d'una xifra")
else:
    print("El nombre té 1 xifra")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.6
'''
def preguntar():
    n = int(input("Introdueix un nombre: "))
    if n >= 0:
        print("És positiu")
    else:
        print("És negatiu")
preguntar()
preguntar()
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 3.7
'''
def preguntar(a):
    n = -1
    while n < 0:
        n = int(input("Introdueix un"+a+" nombre > 0: "))
    if n >= 10 and n <= 99:
        print("Té dues xifres")
    else:
        print("Diferent de dues xifres")
preguntar("")
preguntar(" altre")         #Per cambiar la pregunta


