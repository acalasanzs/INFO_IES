'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5.1 Operacions amb cadenes: Assignació
'''
paraula = "Aprèn "
p = str(input("Digues una paraula: "))
paraula = paraula+p
print(paraula)
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5.2. Operacions amb cadenes: Concatenació
'''
p = str(input("Paraula 1: "))
n = str(input("Paraula n: "))
print(p,n,sep=" ")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5.3. Operacions amb cadenes: Cerca
'''
p = str(input("Paraula: "))
print("Posició de 'a': "+str(p.find('a')+1))
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5.4. Operacions amb cadenes: Extracció
'''
p = str(input("Paraula: "))
print("Des de 3 fins a 8: "+p[3:8])
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5.5. Operacions amb cadenes: Comparació
'''
p = str(input("Paraula 1: "))
n = str(input("Paraula 2: "))
if p == n:
    print(p,n,"SÍ són iguals", sep=" - ")
else:
    print(p,n,"NO són iguals", sep=" - ")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5 AMPLIACIÓ
'''
def compt(a):
    t = 0
    for c in p:
       if c == a:
           t += 1
    else:
        return str(t)
p = str(input("Escriu una frase: "))
a = str(input("Quina lletra hi vols buscar? "))
print("N'hi ha ",compt(a)," ",a,"(s).")
'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 5 AMPLIACIÓ 2: SUPRIMIR UNA LLETRA
'''
p = str(input("Escriu una frase: "))
a = ""
while not(len(a) == 1):
    a = str(input("Quina lletra hi vols SUPRIMIR? "))
p = p.translate({ord(a): None})
print(p)