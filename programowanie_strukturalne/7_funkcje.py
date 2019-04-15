def witaj():
    print('witaj',end='')
    print(' Janusz!')
witaj()

def wyswietlWiek(wiek):
    print('Masz', wiek , 'lat')

wyswietlWiek('23')

print()

def iloczyn(a,b):
    return a * b

print(iloczyn(3,4))

print()

def iloraz(a,b):
    return a/b

print(iloraz(4,3))
print(iloraz(b=3,a=4))




def car():
    samochud = {
        'marka':input("marka "),
        'model':input("model "),
        'pojemnosc':input("pojemnosc "),
        'predkoscMax':input("predkosc maksymalna ")
               }
    wyswietl(samochud)






def wyswietl(x):
    print(x)
car()
