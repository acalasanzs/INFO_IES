from assgn import *
def optionsinclass(cls):
    #Indexa totes les dir d'un objecte i les passa per triar una per després retornarla amb getattr com un attr válid.
    method_list = [method for method in dir(cls) if method.startswith('__') is False]
    print("Options in {}: {}{} {}".format(cls.__name__,color.b.purple,List2list(method_list,", "),color.end))
    if len(method_list) < 1: mess.Empty()
    while True:
        try:
            res = int(input("Index? "))
        except:
            print(mess.err)
            continue
        break
    while not(res in range(len(method_list))):      #Mentres no sigui un valor dintre l'index no serà válid.
        if res == -1:
            return getattr(cls,method_list[-1])
        else:
            print(mess.err)
            res = int(input("Index? "))
    return getattr(cls,method_list[res])
def classMehtod(cls):
    a = ": "
    if cls.__doc__ != None: a += cls.__doc__
    print(color.b.blue,cls.__name__,a,color.end)
    optionsinclass(cls)()
def options(cls,num=1):
    repeat = True
    while repeat:
        res = ""
        if num > 1:
            for x in range(num):
                res += "classMethod("
            else:
                res += "optionsinclass(cls)"
        else:
            classMehtod(cls)
        os.system("pause")
        repeat =  False if input("Repeat?(Anything,n)") == "n" else True