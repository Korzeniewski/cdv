'''
import math

def div(x,y):
    try:
        wynik = gora / dol
        print(wynik)
    except:
        print('chciałeś podzielić przez 0')

#zadanie pierwsze
print('podaj a:')
x = input()

print('podaj b:')
y = input()
a = float(x)
b = float(y)

gora = (a**2) + b
dol = (a**2) + (2*a*b) + (b**2)
div(gora,dol)
'''
'''
#zadanie 2 
def zadd(a,b,c):
        try:
            if c > 0:
                print( a**2 + b )
            elif c<0:
                print(a - b**2)
            else:
                print(1/(a-b))
        except:
            print('chciałeś podzielić przez 0')

            
print('podaj a')
a = input()
print('podaj b')
b = input()
print('podaj c')
c = input()



a = float(a)
b = float(b)
c = float(c)

zadd(a,b,c)
'''
#zad3 

print('podaj a')
a = input()
print('podaj b')
b = input()

a = float(a)
b = float(b)

def nwd(a, b):
    while b:
        a, b = b, a%b
    return a