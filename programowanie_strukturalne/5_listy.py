programowanie = ['python', 'c#','js','php','java']
print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)
trzyElementy = programowanie[0:3]
print(trzyElementy)
ostatni = programowanie[-1]
print(ostatni)

#dodawanie elementu

programowanie.append('r')
print(programowanie)
#zliczanie elementów listy

ile = programowanie.count('python')
print(ile)

#ilość elementów w liście
iloscElem = len(programowanie)
print(iloscElem)


#polaczenie list


inneJezyki = ['c','c++']
print('polaczenie list:')
programowanie.extend(inneJezyki)
print(programowanie)


#czyszczenie listy

nowa = programowanie
print('lista nowa: ', end='')
print(nowa)




print('Programowanie: ',end='')
print(programowanie)
programowanie.clear()
print('Programowanie: ',end='')
print(programowanie)
