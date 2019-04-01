tekst = "Anna, paweł, JulIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
print(imie1) #Anna

imieDuze = imie1.upper()
imieMale = imie1.lower()
print(imieDuze)
print(imieMale) #anna



#sprawdzenie zawartości
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true or false

nazwisko = ""
print(nazwisko.isalpha()) #False


text1 = "\nJulia\n"
text2 = " Nowak"
print(text1 + text2)

text1 = text1.rstrip()

print(text1 + text2)

#wyświetlanie łancucha znaków

#wszyskie wersje pythona

text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje pythona > 2.6
text2 = "{1}, Java i {0}".format("PHP","Python")
print(text2)

#help(text.replace)

new = text.replace("PHP","C#")
print(new)

#wypisanie danych

rok = 2019
miesiac = "kwiecień"
dzien = 1


print("\nData: ",end="")
print(dzien, miesiac, rok)

print("\nData: ",end="")
print(dzien, miesiac, rok, sep="-")


