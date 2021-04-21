'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
17/3/21 ; Pràctica 7.2 Quadrat o Rectangle
'''
llista = []
valname = {
    0: "base",
    1:"altura",
}
end = "\033[0;m"
err = "\n\u001b[41m"+"No has introduït un nombre vàlid"+"!\033[0;m"
chose = None
def Assign(am,off):
    for x in range(am):
        llista.append(0)
    for i in range(am):
        while True:
            try:
                ans = -1
                while not(ans > 0):
                    #val = [x[0] for x in llista]
                    ans = float(input(str(i+1)+". Introdueix "+valname[i+off]+" en metres: "))
                    if ans <= 0:
                        print(err)
                    else:
                        llista[i] = ans
                        print(llista)
            except ValueError:
                print(err)
                continue
            break
    result = ""
    for l,x in enumerate(llista):
        result += valname[l]+" = "+str(llista[l])+"; "
    print(result)
Assign(2,0)
if llista[0] == llista[1]:
    print("És un quadrat")
else:
    print("És un rectangle")