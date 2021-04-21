'''
________________________________________________________________________________________
Albert CS ; 4tB  
05calasanzalbert@iesperebarnils.cat
3/3/21 ; Pràctica 2.AMPLIACIÓ
'''
def ver(op):																		#Funció que processa el input del operador
    if op == "s":
        op = "+"
    elif op == "r":
        op = "-"
    elif op == "m":
        op = "*"
    elif op == "d":
        op = "/"
    elif op in "+-*/" and len(op) == 1:
        pass   
    else:
        Err()
    return op
def start(p):
    if(p):
        print("Calculadora de dos valors:")
        print("Primer posa els dos valors, després utilitza: r(resta),s(suma),m(mult),d(div) o '-+*/'")
        print("Fet per Albert CS. AMPLIACIÓ 2a Part")
        print("_______________________________________")
    a = float(input("Valor 1: "))
    b = float(input("Valor 2: "))
    op = str(input("Operador: "))
    a=str(a)
    b=str(b)
    print(a+" "+ver(op)+" "+b,eval(a+ver(op)+b),sep=" = ")							#Evaluació del str a una operació matemàtica
    print("""_.-'''''-._
    .'  _     _  '.
   /   (_)   (_)   \
  |  ,           ,  |
  |  \`.       .`/  |
   \  '.`'""'"`.'  /
    '.  `'---'`  .'
      '-._____.-'""")																#SOMRIURE
def Err():
    print("""  ___ _ __ _ __ ___  _ __ 
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |   
 \___|_|  |_|  \___/|_|   """)														#Error en el operador
    start()
start(1)																			#PRESENTACIÓ