#zasięg zmiennych, zmnienne lokalne i globalne


#precyzja liczby (zaokroglenie do 3 miejst po przecinku)

x = "{0:.3f}".format(5)
print(x)

def plsToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(f'ilosc CHF: {iloscChf}')

plsToChf(400)


# zadanie funkcja ile euro za złotówki
print('################## ZADANIE ##################')
x1 = float(input('ile masz zloty ?\n'))
def plnToEuro(value):
    kursEuro = 4.2847
    iloscEuro = value / kursEuro
    iloscEuro = "{0:.4f}".format(iloscEuro)
    return iloscEuro

print(plnToEuro(x1))

print()
print()
print('################ ZMNIENNE GLOBALNA ################')


kursUSD = 3.7899
print(kursUSD)

def plnToUSD(value):
    iloscUSD = value / kursUSD
    iloscUSD = "{0:.4f}".format(iloscUSD)
    return iloscUSD

print(f'kurs dolara:{kursUSD}')
pln = float(input('podaj pln na usd\n'))
print(plnToUSD(pln))

zmniennaGlobalna = 10
print(f'\nwartosc zmnienna globalna {zmniennaGlobalna}')
print(f'\nwartosc zmnienna globalna {id(zmniennaGlobalna)}')


def spr():
    global zmniennaGlobalna
    zmniennaGlobalna = 20
    print(f'/nwartość zmniennej globalnej wewnątrz funkcji:{zmniennaGlobalna}')
    print(f'/nwartość ID zmniennej globalnej wewnątrz funkcji:{id(zmniennaGlobalna)}')

    spr()















