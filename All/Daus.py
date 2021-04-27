from lib import *
import files
import math,time,os,sys,random,numpy                                             #Math per mates, time per controla el temps i os per opcions del sistema(cmd)
def JocDelsDaus():
    daus = []
    partides = []
    PlayerGames = Assgn(Ar2Dict(["Jugadors","Partides"]),rules=[False,False,True])
    print("Every player throws 2 dies, which gets the largest value wins.")
    jugadors = Assgn(IterAr(PlayerGames.llista[0],"el nom del Jugador"),rules="str")
    for i in range(PlayerGames.llista[1]):
        for x in range(PlayerGames.llista[0]):
            daus.append(random.randrange(1,7,1))
        partides.append(daus)
        daus = []
    print(numpy.array(partides))
    col_totals = [sum(x) for x in zip(*partides)]
    print("=")
    print(col_totals)
    indices = [i for i, x in enumerate(col_totals) if x == max(col_totals)]
    guanyadors = []
    for x in indices:
        guanyadors.append(jugadors.llista[x])
    print("Guanya/en els jugadors:",List2list(guanyadors,", "))
JocDelsDaus()
