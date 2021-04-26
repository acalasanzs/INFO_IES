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
def facto():
    print(fact(int(input("Factorial de (enter): "))))
if __name__ == "__main__":
    facto()