from lib import *
import files
import math,time,os,sys,random                                             #Math per mates, time per controla el temps i os per opcions del sistema(cmd)
__doc__ = "Apartats 7, 8 i 9 AMPLIACIÓ I AMPLIACIÓ DE L'AMPLIACIÓ by Albert CS"
os.system("title "+__doc__)
os.system("mode 155,42")                                        #Assegurar la compatibilitat d'ASCII ART
time.sleep(0.1)                                                 #Bugfix
"""
TODO:
1. Documentar aquest, ampliacio,py i assgn.py.
"""
class Tots_Els_Apartats:                                        #Class que engloba tots els exercicis classificats
    class quatre:
        def ampliacio():
            files.cotxe()
        def ampliacio4():
            files.main()
    class cinc:
        def E51():
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
        def E52():
            '''
            ________________________________________________________________________________________
            Albert CS ; 4tB  
            05calasanzalbert@iesperebarnils.cat
            17/3/21 ; Pràctica 5.2. Operacions amb cadenes: Concatenació
            '''
            p = str(input("Paraula 1: "))
            n = str(input("Paraula n: "))
            print(p,n,sep=" ")
        def E53():
            '''
            ________________________________________________________________________________________
            Albert CS ; 4tB  
            05calasanzalbert@iesperebarnils.cat
            17/3/21 ; Pràctica 5.3. Operacions amb cadenes: Cerca
            '''
            p = str(input("Paraula: "))
            print("Posició de 'a': "+str(p.find('a')+1))
        def E54():
            '''
            ________________________________________________________________________________________
            Albert CS ; 4tB  
            05calasanzalbert@iesperebarnils.cat
            17/3/21 ; Pràctica 5.4. Operacions amb cadenes: Extracció
            '''
            p = str(input("Paraula: "))
            print("Des de 3 fins a 8: "+p[3:8])
        def E55():
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
        def Amp():
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
        def Amp2():
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
            p = p.translate({ord(a): " "})
            print(p)
        def E56():
            res = input("Introdueix un frase: ")
            print("Té {} paraules".format(len(res.split())))
            print("Té {} cáractes".format(len(res)))
    class sis:
        def Factorial_Dun_Nombre():
            files.facto()
        def a63():
            casos = int(input("Quantes paraules vols introduïr? "))
            print(casos)
            cont = 0
            while casos > 0:
                cont += 1
                print(input("Paraula "+str(cont)+" :"))
                casos -= 1
        def a65AMP():
            res = input("Digues números: ")
            a = res.split()
            total = 0
            for x in a:
                total += int(x)
            return total
        def a65():
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
    class Set_1:
        """El primer exercici del set només"""
        def cub():
            ask = Assgn(Ar2Dict(["x","y","z"],"metres"),conj="en")
            res = 1
            for i in ask.llista: res *= i
            return "{} m^3".format(res)
        def cilindre():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return "{} m^3".format(((math.pi)*ask.llista[0]**2)*ask.llista[1])
        def con():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return "{} m^3".format((((math.pi)*ask.llista[0]**2)*ask.llista[1])/3)
        def esfera():
            ask = Assgn(Ar2Dict(["radi"],"metres"),conj="en")
            return "{} m^3".format((math.pi)*(3/4)*(ask.llista[0]**3))
    class Set_2:
        "La resta del set excepte el primer"
        def Set_2_DifQuadRect():
            obj = Assgn(rang=range(2))
            if obj.llista[0] == obj.llista[1]:
                return "Quadrat"
            else:
                return "Rectangle"
        def Set_3_roda():
            roda = """                          ██████████████                              #Una Roda             
                      ████▒▒▒▒▒▒▓▓▒▒▒▒▒▒████              
                  ████▒▒▒▒██████▒▒██████▒▒▒▒████          
                ██▒▒▒▒████    ██▒▒██    ████▒▒▒▒██        
              ██▒▒████        ██▒▒██        ████▒▒██      
            ██▒▒██▒▒██        ██▒▒██        ██▒▒██▒▒██    
            ██▒▒████▒▒██      ██▒▒██      ██▒▒████▒▒██    
          ██▒▒████████▒▒██    ██▒▒██    ██▒▒████████▒▒██  
          ██▒▒██████  ██▒▒██  ██▒▒██  ██▒▒██  ██████▒▒██  
        ██▒▒████████    ██▒▒████▒▒████▒▒██    ████████▒▒██
        ██▒▒████████████████▒▒██▓▓██▒▒████████████████▒▒██
        ██▒▒██████████████████▓▓▓▓▓▓██████████████████▒▒██
        ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██
        ██▒▒██████████████████▓▓▓▓▓▓██████████████████▒▒██
        ██▒▒██            ██▒▒██▓▓██▒▒██            ██▒▒██
        ██▒▒██          ██▒▒████▒▒████▒▒██          ██▒▒██
          ██▒▒██      ██▒▒██  ██▒▒██  ██▒▒██      ██▒▒██  
          ██▒▒██    ██▒▒████  ██▒▒██  ████▒▒██    ██▒▒██  
            ██▒▒████▒▒██  ██████████████  ██▒▒████▒▒██    
            ██▒▒██▒▒██      ██████████      ██▒▒██▒▒██    
              ██▒▒████        ██▒▒██        ████▒▒██      
                ██▒▒▒▒████    ██▒▒██    ████▒▒▒▒██        
                  ████▒▒▒▒██████▒▒██████▒▒▒▒████          
                      ████▒▒▒▒▒▒▓▓▒▒▒▒▒▒████              
                          ██████████████                  
        """
            obj = Assgn({0: ("Radi","metres"),1:("Les voltes que dona","voltes")})                              #Preguntes
            circ = obj.llista[0]*math.pi                                                                        #Long circumferencia
            print("\u001b[1m\u001b[4m\u001b[7m ")
            print(roda)
            print("Una roda de "+str(obj.llista[0])+" metres de radi")
            print("recorre "+str(circ*obj.llista[1])+" m\u001b[0m CADA "+str(objs[1])+" voltes que dona")
            return "FET"
        def Set_3_Ampliacio():
            cotxe()                                                                                             #Funció de ampliacio.py
        def Set_4_OddEven():
            inputs = {
                0: ("des d'ón","enter"),
                1: ("fins ón","enter")
            }
            obj = Assgn(inputs)
            llista = obj.llista
            odd = []
            even = []
            print("\n")
            for i in range(int(llista[0]),int(llista[1]+1)):
                if(i%2!=0):
                    odd.append(i)
                else:
                    even.append(i)
            def suma(list):
                t = 0
                for i in list:
                    t += i
                return t
            print("\u001b[1m\u001b[4m\u001b[7mParells ("+str(len(even))+"):"+color.end)
            time.sleep(1)
            print(List2list(even))
            print(color.t.OKBLUE,"=",suma(even),color.end)
            time.sleep(1.4)
            print("\u001b[1m\u001b[4m\u001b[7mImparells ("+str(len(odd))+"):"+color.end)
            time.sleep(1)
            print(List2list(odd))
            print(color.t.OKGREEN,"=",suma(odd),color.end)
            time.sleep(1)
            print("Total:","(","des de:",int(llista[0]),";fins a:",int(llista[1]),")","\nImparells =",suma(odd),"Parells =",suma(even))
            return ""
        def Set_5_Triangles():
            print("Torna el tipus de triangle segons els seus costats i els seus angles respectius (A,B,C)")
            ask = Assgn(rang=range(3))
            seen = []
            c = 1
            for x in ask.llista:
                if x in seen:
                    c += 1
                seen.append(x)
            if c == 1:
                print("Escalé")
            elif c == 2:
                print("Isosceles")
            elif c == 3:
                print("Equilater")
            a,b,c = seen
            try:
                """ alpha.SetValue(180 * Math.acos((b * b + c * c - a * a) / (2 * b * c)) / Math.PI);
				    beta.SetValue(180 * Math.acos((a * a + c * c - b * b) / (2 * a * c)) / Math.PI);
					gamma.SetValue(180 * Math.acos((a * a + b * b - c * c) / (2 * a * b)) / Math.PI); """
                A = math.acos((b * b + c * c - a * a) / (2 * b * c))                                                #Alpha
                B = math.acos((a * a + c * c - b * b) / (2 * a * c))                                                #Beta
                C = math.acos((a * a + b * b - c * c) / (2 * a * b))                                                #Gamma
                for i in [A,B,C]:
                    print(namestr(i,locals())[0],"=",str(math.degrees(i))+"º","radians:",i)
            except:
                print(color.b.red,"Aquest triangle no existeix XD",color.end)
                Tots_Els_Apartats.Set_2.Set_5_Triangles()
            draw(a, b, c)
    class Vuit_1:
        "Exercicis del 8 del primer document"
        def VelocitatMitjana():
            inputs = Assgn({0:("distancia","metres"),1:("temps","segons")},conj="en")
            res = inputs.llista[0]/inputs.llista[1]
            return "Result = {} m/s".format(res)
        def km2ms():
            res = 0
            while not(res in (1,2)):
                while True:
                    try:
                        res = int(input("Introdueix kmh o ms: "))
                    except:
                        print(mess.err)
                        continue
                    break
            if res == 1:
                while True:
                    try:
                        return "Ans = {} m/s".format(float(input("kmh?"))/3.6)
                    except:
                        print(mess.err)
                        continue
                    break
            else:
                while True:
                    try:
                        return "Ans = {} km/h".format(float(input("ms?"))*3.6)
                    except:
                        print(mess.err)
                        continue
                    break
        def VelocitatMitjanaCiclista():
            res = Assgn({0:["Distancia","metres"],1:["Velocitat","m/s"]},conj = "en")
        def VelocitatSo():
            return "És supersónic" if int(input("Km/h?(Avió)"))*3.6 >= 340 else "No ho és"
        def DistQueSeparaDosCotxes():
            dic = Ar2Dict(["Cotxe 1","Cotxe 2"],"km/h")
            dic[2] = ("Temps","hores")
            valors = Assgn(dic,conj="en")
            a = valors.llista[0]*valors.llista[2]
            b = valors.llista[1]*valors.llista[2]
            return "Els separa {} km".format(abs(a-b))
    class Vuit_2:
        "Exercicis del 8 del segon document"
        def MagnitudsDunCircuitElectric():
            dic = {
                0: ("Resitencia","Ohms"),
                1:  ("Intensitat","Ampers"),
                2: ("Tensió","Volts"),
                3: ("Energia","Joules")
            }
            ask = Assgn(dic,conj="en")
        def LleiDOhm():
            intensitat = float(input("Intensitat en milampers: "))
            while not(intensitat in range(1,1001)):
                print(mess.err)
                intensitat = float(input("Intensitat en milampers: "))
            tensio = float(input("Tensió en volts: "))
            while not(tensio in range(2,231)):
                print(mess.err)
                tensio = float(input("Tensió en volts: "))
            return "{} Ohms".format(intensitat/tensio)
        def ResitenciesEnSerie():
            # Resistencies en serie, progamet.
            valors = []                                                                 #Array de tots els casos
            i = 0                                                                       #Comptador de la iteració
            while True:                                                                 #While True, per parar-ho quan vulgui
                i += 1
                res = input("Resitencia {}: ".format(i))
                if not(res):                                                            #Si el input és buit, trenca el while y passa al còdig de baix
                    print("Casos Finalitzat!")
                    break
                else:
                    try:
                        res = float(res)                                                #Si no, passa a comprovar si es pot passar a float
                        if res == 0:
                            print(mess.err)
                            i-= 1
                            continue
                        else:
                            valors.append(abs(res))
                            print(color.t.OKBLUE,List2list(valors,", "),color.end)
                    except:
                        print(mess.err)                                                 #Si no bloquejem la iteració al mateix punt fins que sigui válid
                        i-= 1
                        continue
            #Preguntem què es vol calcular
            ask = input("En paral·lel o en serie?")
            while ask not in ("0","1"):
                print(mess.err)                                                         #mess.err És un missatge d'error
                ask = input("En paral·lel o en serie?")
            if ask == "0":
                resultat = 0
                for i in valors:
                    resultat += 1/i
                resultat = 1/resultat
                return "En paral·lel dona un total de {} Ohms".format(resultat)
            else:
                return "En serie dona un total de {} Ohms".format(sum(valors))
        def BaixConsum():
            obj = Assgn({0:("Intensitat","Ampers"),1:("Consum","Joules")},conj="en")
            res = obj.llista[0]*obj.llista[1]
            if res >= 1000:
                res /= 1000
                return "{} KWh".format(res)
            else:
                return "{} Wh".format(res)
    class Nou_Ampliació:
        def Ampliacio():
            def C(temp,res):
                print(res,"A Celsius")
                if res == "F":
                    #(0 °C × 9 / 5) + 32
                    return "{}º{}".format((temp)*(9/5) + 32,res)
                elif res == "K":
                    return "{}º{}".format(temp + 273.15,res)
            def F(temp,res):
                print(res,"A Farenheight")
                if res == "C":
                    #(32 °F − 32) × 5 / 9 = 0 °C
                    return "{}º{}".format((temp-32)*(5/9),res)
                elif res == "K":
                    #(32 °F − 32) × 5 / 9 + 273,15 = 273,15 K
                    return "{}º{}".format((temp-32)*(5/9) + 273.15,res)
            def K(temp,res):
                print(res,"A Kelvin")
                if res == "F":
                    return "{}º{}".format((temp-32)*(5 / 9) + 273.15,res)
                elif res == "C":
                    return "{}º{}".format(temp + 273.15,res)
            def ask():
                while True:
                    try:
                        temp = float(input("Temperatura? "))
                    except:
                        print(mess.err)
                        continue
                    break
                return temp
            temp = ask()
            res = input("En què està (F,C,K)? ")
            while res not in ["F","C","K"]:
                print(mess.err)
                res = input("En què està (F,C,K)? ")
            if res == "C":
                if temp < 273.15:
                    print(mess.err)
                    temp = ask()
            elif res == "K":
                if temp < 0:
                    print(mess.err)
                    temp = ask()
            elif res == "F":
                if temp < -459.67:
                    print(mess.err)
                    temp = ask()
            print(color.b.green,"{}º{}".format(temp,res),color.end)
            target = input("A què vols (F,C,K)? ")
            while target not in ["F","C","K"]:
                print(mess.err)
                target = input("A què vols (F,C,K)? ")
            print(color.b.green,"{}º{}".format("to: ",target),color.end)
            if target == res:
                print(res,"A",res)
                print(color.b.green,str(temp)+res,color.end)
            else:
                print(color.b.green,locals()[target](temp,res),color.end)
    class Deu():
        def Dau():
            tirades = Assgn(["Quantes tirades?"],vals=range(3,11))
            print(color.b.yellow,tirades.llista[0],"Tirades seleccionat.",color.end)
            ask = Assgn(rang=range(int(tirades.llista[0])))
            rand = random.randrange(1,6,1)
            if rand in ask.llista:
                jugador = [int(x) for x in ask.llista if x == rand]
                print("Ha guanyat el jugador nº",ask.llista.index(jugador[0])+1)
def main():
    #sys.argv = ['file.py','cinc','Amp2']
    if sys.argv[1:]:
        def check_class(tot):
            total = []
            mat = sys.argv
            mat[0] = "Tots_Els_Apartats"
            cls = ""
            for idx,x in enumerate(mat):
                cls += "." + x if not x == mat[0] else mat[0]
                try:
                    assert mat[idx+1] in opt.opts(eval(cls))
                except:
                    return eval(cls),(tot-int(cls.count(".")))
        cla = check_class(2)
        print(cla)
        opt.options(cla[0],cla[1])
    else:
        opt.options(Tots_Els_Apartats,2)
if __name__ == "__main__":
    main()
#pyinstaller --onefile --icon=C:\Users\07cal\Downloads\pp.ico --name="Tots" main.py