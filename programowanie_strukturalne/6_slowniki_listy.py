#listy
imiona = ['Julia','Anna','Tomek']
print(type(imiona))
imiona.append('Paweł')
print(len(imiona)) #4

#tuple
nazwiska = ('Nowak','Kowalski')
print(nazwiska)
print(type(nazwiska))
print(len(nazwiska))

#słowniki

osoba = {'imie':'Julia','Nazwisko':'Nowak','wiek':25}
print(osoba)
print(type(osoba))
print(osoba['Nazwisko'])
print(osoba.get('imie','brak danych'))
print(osoba.keys())
