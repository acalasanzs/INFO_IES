'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.1
'''
for x in range(6):
    print("El meu primer llaç",x+1)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.2
'''
for x in [1,2,3,4,5,6]:
    print("El meu primer llaç",x)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.3
'''
r = 0
for x in range(10):
    r = (x+1) + r
print(r)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.4
'''
for i in range(3):
    for j in range(3):
        print(i+j)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.5
'''
def prnt(p):
    a = int(input(p))
    print(a+1)
prnt("Introdueix un nombre: ")
prnt("Introdueix un 2n nombre: ")
prnt("Introdueix un 3r nombre: ")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 4.6
'''
def prnt():
    a = int(input("Introdueix valor 1: "))
    b = int(input("Introdueix valor 2: "))
    print(a+b)
for x in range(5):
    print(str(x+1)+". Introdueix dos valors")
    print("_______________________________")
    prnt()