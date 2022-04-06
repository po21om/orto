# -*- coding: utf-8 -*-
import random as r
def slownik(x,y):
    slownik = {}
    with open("slowa.txt", encoding="UTF-8") as fread:
        for line in fread:
            if x in line:
                slownik[line.replace(x, "_").rstrip()] = x
            elif y in line:
                slownik[line.replace(y, "_").rstrip()] = y
    return slownik
slownik_ch = slownik("ch","h")
slownik_rz = slownik("rz","ż")
slownik_u = slownik("u","ó")


def cwiczenia(dict):
    loop = True
    counter_f = 0
    counter_t = 0
    while loop:
        k = list(dict.keys())
        q = r.randint(0,len(k))
        print(len(k), q)
        a = input(f"{k[q]} : ")
        if a == dict[k[q]]:
            print("Dobrze")
            counter_t +=1
        elif a == "stop":
            loop = False
        else:
            print("Źle")
            counter_f += 1
    if counter_t + counter_f == 0:
        print("Nie wykonałeś żadnego przykładu.")
    else:
        print(f"Wykonałeś dobrze {counter_t} przykładów na {counter_f+counter_t} co stanowi {(counter_t/(counter_t+counter_f))*100:.2f}%")

prog = True
while prog:
    choice = input("Wybierz ćwiczenia (1.ch-h, 2.rz-ż, 3.u-ó) lub \"quit\" by wyjść: ")
    if choice == "1":
        cwiczenia(slownik_ch)
    elif choice == "2":
        cwiczenia(slownik_rz)
    elif choice == "3":
        cwiczenia(slownik_u)
    elif choice == "quit":
        prog = False
    else:
        print("Nie ma takiej opcji ;(")
