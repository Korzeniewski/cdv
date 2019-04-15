import os
#print('kanapka')
#input()
#os.system('cls')

def wyswietl(number1, number2):
    print(f'Liczba1: {number1}')
    print(f'Liczba2: {number2}')

wyswietl(2,3)


################################# *args #################


def wyswietlArgs(number1, *args):
    print(f'\nPierwszy element: {number1}')
    for i in args:
        print(f'następny element: {i}')


wyswietlArgs(2,3,4,6,7,878,5456)

imiona = ['Anna','Maciej']
wyswietlArgs(imiona)
wyswietlArgs(*imiona)
