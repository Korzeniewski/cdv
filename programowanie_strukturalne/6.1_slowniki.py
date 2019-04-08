slownik = {'klucz1' : 'wartost1', 'klucz2' : 'wartosc2'}

pracownik = {
'imie':'marek',
'nazwisko':'kowalski',
'miasto':'poznan',
'wiek':12,
'imionaDzieci':['Anna','Paweł'],
'imionaRodzicow':['marek','halina']}
print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])

pracownik['wzrost'] = 175
pracownik['waga'] = 75
print(pracownik)
