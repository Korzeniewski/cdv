print("CDV")
print(24)

#potęgowanie

potega = 2 ** 10

print(potega)

#pobieranie danych z klawiatury

imie = input()

#konkatenacja +

print("twoje imie podane z klawiatury: "+imie)

nazwisko = input("podaj nazwisko:")

print("twoje nazwisko podane z klawiatury: "+nazwisko)
print()

#twoje imie: ... , twoje nazwisko: ...
print("twoje imie:" + imie + ", twoje nazwisko:" + nazwisko)

# użytkownik podaje z klawiatury swój wiek, wyśietl dane w formacie
# twój wiek: ... lat

print("podaj swój wiek: ",end="")
wiek = input()
print("twój wiek: ",wiek," lat")

wiek1 = 20
print("twój wiek: ", wiek1 ," lat")

#jak jest konkatenacja (czyli +) to ze stringami moze byc problem

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

dlugosz = len(nazwisko)
print(dlugosz)

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int
y = 4
print(type(y))

y = y/2

print(type(y))

print(y)

nazwisko = "kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #KOW
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowalsk
print(nazwisko[:-2:2]) #Kwl





print()
