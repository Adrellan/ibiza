from miller_rabin import is_prime_mr
from chinese_rem import chinese_rem
from math import gcd 
from main import modular_exp
import random

def relativprime(a, b):
    return gcd(a, b) == 1

def kibovitett_euk_alg(a, b):
    if a == 0 :
        return b,0,1
         
    gcd,x1,y1 = kibovitett_euk_alg(b%a, a)
     
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def kulcsgeneralas():
    #Számot eredetileg generálni kéne, de most lusta vagyok hozzá
    
    #1
    p = 1429
    q = 457 
    if (is_prime_mr(p) and is_prime_mr(q)):
        #2
        n = p*q

        #3
        fiN = (p-1)*(q-1)
        print("fiN: ",fiN)

        #4
        e = random.randint(1,fiN)
        while(relativprime(e, fiN)!=True):
            e = random.randint(1,fiN)
        
        print("e: ",e)

        #5
        g, x, y = kibovitett_euk_alg(fiN,e)
        print("")
        print("x: ",x)
        print("y: ",y)

        if(y<=0):
            y+=fiN

        d = y
        
        print("d: ",d)
        
        m=34
        S = alairas(q,p,d,m)
        if ellenorzes(S,e,n,m):
            print("Sikeres ellenorzes")
        else:
            print("Sikertelen ellenorzes")

def alairas(q,p,d,m):
    S = chinese_rem(m,q,p,d,p*q)
    #print("S: ",S)
    return S

def ellenorzes(S,e,n,m):
    szam = pow(S, e)
    if(modular_exp(S,e,n) == m):
        return True
    return False


if __name__ == '__main__':
    kulcsgeneralas()
    