'''
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 1.7 AMPLIACIÓ
'''
a = str(input("Paraula 1: "))           #Es demana cada paraula i es passa a string
b = str(input("Paraula 2: "))           
c = str(input("Paraula 3: "))           
d = str(input("Paraula 4: "))           
p = [a,b,c,d]                           #Es fa un array de totes
for x in p:                             #Bucle for per a cada paraula
    lon = len(x)                        #Una variable temporal per la llargada de la paraula x
    print(x," : ",lon)                  #S'imprimeix la paraula x + la seva llargada
print(a,b,c,d,sep=" ")                  #Totes les paraules juntes, separades per un espai
print("Llargada total: ",len(a+b+c+d))  #Es calcula finalment la suma de totes les llargades