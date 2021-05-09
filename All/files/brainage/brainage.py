import random, time, time, math, pycrypt
import assgn

def brainage():
    # 1.levels són els ranges de nivel fàcil,m,difícil
    global levels
    level = assgn.Assgn(['Nivell (cada nivell té 2 intents més)'],rules=[False,False,True]).llista[0]
    #2.Assigna un color per a cada un
    sem = {
        "Easy": assgn.color.b.green,
        "Medium": assgn.color.b.yellow,
        "Hard": assgn.color.b.red,
        "Very Hard": assgn.color.b.red,
        "Insane": assgn.color.b.purple
    }
    #3.Per evitar l'error undefined
    levels = ()
    def ran():
        #4.Funcio que assigna la dificulta segons els nivells que es seleccionen en modes
        rang = "Easy" if level < levels[0] else "Medium" if level < levels[1] else "Hard" if level < levels[2] else "Insane" if level > levels[3] else "Very Hard"
        print(sem[rang],rang,assgn.color.end)


    class modes:
        def multiplicacio():
            global levels
            #Array que recopila tots el nums
            nums = []
            #Assigna els nivells
            levels = (3,7,15,25)
            #print el nivell
            print("Level {}".format(level))
            #print 4. la dificultat
            ran()
            #Per el doble de vegades que el nivel es mostraran nombres
            for x in range(level*2):
                #Randrange pel nivell
                num = random.randrange(1,level*2+5)
                #Mostra el num per 1.5 segons
                print(num,end="\r")
                nums.append(num)
                time.sleep(1.5)
            #Ho multiplica tot
            res = math.prod(nums)
            #Els vals són el res
            resultat = assgn.Assgn(["Multiplicacio de tots"],vals=[res])
            print("Well Done! Level {} passed".format(level))
        def suma():
            global levels
            levels = (5,12,20,40)
            print("Level {}".format(level))
            ran()
            nums = []
            #Per el doble de vegades que el nivel es mostraran nombres
            for x in range(level*2):
                #Randrange pel nivell
                num = random.randrange(1,level*2+5)
                #Mostra el num per 1.5 segons
                print(num,end="\r")
                nums.append(num)
                time.sleep(1.5)
            #Els vals són el res                        #Ho suma tot
            resultat = assgn.Assgn(["Suma de tots"],vals=[sum(nums)])
            print("Well Done! Level {} passed".format(level))
        def divisio():
            global levels
            levels = (5,12,20,40)
            print("Level {}".format(level))
            ran()
            nums = []
            #Per el doble de vegades que el nivel es mostraran nombres
            #Randrange pel nivell
            for i in range(level*2):
                num = random.randrange(1,level*2+5)
                divisor = random.randrange(1,level*2+5)
                x = num*divisor
                res = 0
                print(f"Pregunta {i+1} de {max(range(level*2))+1}:")
                while res != divisor:
                    try:
                        res = int(input(f"{x}/{num} = "))
                    except:
                        continue
                #Mostra el num per 0.2 segons
                time.sleep(0.2)
            #Els vals són el res                        #Ho suma tot
            print("Well Done! Level {} passed".format(level))
    #5.Es crida un method en modes
    metodes = [method for method in dir(modes) if method.startswith('__') is False]
    getattr(modes,assgn.Assgn([f'Modes: {metodes}'],rules="str",vals=metodes ).llista[0])()

if __name__ == "__main__":
    brainage()