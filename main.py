# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ext_euclid(a,b):
    x0,x1,y0,y1,s = 1,0,0,1,1
    while b!=0:
        r = a % b
        q = a // b
        a = b
        b = r
        x = x1
        y = y1
        x1 = q*x1 + x0
        y1 = q*y1+ y0
        x0,y0= x,y
        s = -s
    x=s*x0
    y=-s*y0
    d,x,y = a,x,y
    return(d,x,y)

def modular_exp(a,k,m):
    res = 1
    a = a % m
    while (k > 0):
        if ((k & 1) == 1):
            res = (res * a) % m
        k = k >> 1
        a = (a * a) % m
    return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(ext_euclid(544,119))
    print(modular_exp(129,96,171))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/