# echo.py

import shlex
import sys

def kea(a,b):
    c = a%b
    while (b%c!=0):
        a = b
        b = c
        c = a%b

    print(c)

def decimalToBinary(n):
    return "{0:b}".format(int(n))

#Valami elcsúszott
def gyorshatvanyozas(kitevo,hatvany, modulo):
    numbers = []
    binary = decimalToBinary(hatvany)
    needed_numbers = []
    result = 1

    for i in range(len(binary)):
        x = pow(kitevo,pow(2,i))%modulo
        numbers.append(x)

    for y in range(len(binary)):
        if binary[y] == '1':
            needed_numbers.append(numbers[y])

    for z in range(len(needed_numbers)):
        result *= needed_numbers[z]
        result %= modulo
    
    print(result)

def modular_exp(a,k,m):
    res = 1
    a = a % m
    while (k > 0):
        if ((k & 1) == 1):
            res = (res * a) % m
        k = k >> 1
        a = (a * a) % m
    return res 


def millerrabin(p,a):
    original = p
    p -= 1
    s = 1
    d = 0
    osszetett = False

    while((p/2)%2 == 0):
        s += 1
        p /= 2

    d = (original-1)/(pow(2,s))

    #Teszt 1
    if(modular_exp(a,int(d),original) == 1):
        return "A szam primszam"
    
    #Teszt 2
    for i in range(0,int(s)):
        if(modular_exp(pow(a,pow(2,i)*int(d)),int(d),original) == 561):
            osszetett = True

    if osszetett:
        return "A szam primszam"
    else:
        return "A szam osszetett szam"

def kinaimaradek(rel_primek,rand_egeszek):

def main() -> int:
    #kea(845,68)
    #gyorshatvanyozas(6, 73, 100)
    print(millerrabin(561,2))
    kinaimaradek(rel_primek,rand_egeszek)

    return 0

if __name__ == '__main__':
    sys.exit(main())