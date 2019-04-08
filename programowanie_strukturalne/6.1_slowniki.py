slownik = {'klucz1' : 'wartost1', 'klucz2' : 'wartosc2'}

pracownik = {
'imie':'marek',
'nazwisko':'kowalski',
'miasto':'poznan',
'wiek':12,
'imionaDzieci':['Anna','Paweł'],
'imionaRodzicow':['marek','halina']
}
print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])

pracownik['wzrost'] = 175
pracownik['waga'] = 75
print(pracownik)

klucz = 'wiek'

if klucz in pracownik:
    del pracownik[klucz]
    print('klucz został usunięty')
else:
    print(f'klucz {klucz}nie został usunieęty')
print(pracownik)



print()
print(pracownik.keys())





print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())

for value in pracownik.values():
    print(value,end=', ')




print()
print()
print()
for value in pracownik.values():
    print(value,end=', ')

for key, value in pracownik.items():
    print(key, value)
