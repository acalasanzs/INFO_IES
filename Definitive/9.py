# 9.1
def sumarcinc(num): 
    return num +5
print(sumarcinc(float(input("Número"))))
#9.2
def f(num):
    print(num)
f(float(input("Introdueix un número: ")))
#9.3
def su(*args):
    print(sum(args))
n1 = float(input("Num1: "))
n2 = float(input("Num 2: "))
su(n1,n2)
#9.4
def su(*args):
    return sum(args)
n1 = float(input("Num1: "))
n2 = float(input("Num 2: "))
print(su(n1,n2))
