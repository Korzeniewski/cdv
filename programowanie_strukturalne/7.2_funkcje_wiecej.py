#przekazywanie argumentów przez referencje
def show(name):
    print(f'Przed modyfikacją: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacją: {name}')
    print(f'ID Po modyfikacją: {id(name)}')

data = ['Anna','Agnieszka','Andrzej']
print(f'Przed wywołaniem funkcji show: {data}')
print(f'ID przed wywołaniem funkcji modyfikacją: {id(data)}')
print()


show(data)
print(f'Po wywołaniem funkcji show: {data}')

print()
print()
print()


############################ Słownik ############################


data1 = {0: 'Artur', 1:'Andrzej'}
print(f'\nID przed modyfikacją: {id(data1)}')
show(data1)



#przekazywanie argumentu przez wartość
print()
print()
print()
def show1(city):
    print(f'Przed modyfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    print(f'Po modyfikacją: {city}')
    print(f'Po modyfikacją: {id(city)}')

miasto = ['Gniezno','Poznań']
print(f'Po modyfikacją: {miasto}')
print(f'Po modyfikacją: {id(miasto)}')


show1(list(miasto))
print(f'Po funkcji: {miasto}')

print()
print()
print()




##################### słownik dict ###########################


print('\n#############################################################\n')
print()
print()
def show2(city):
    print(f'Przed modyfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    print(f'Po modyfikacją: {city}')
    print(f'Po modyfikacją: {id(city)}')

miasto1 = {0:'Gniezno',1:'Poznań'}
print(f'Po modyfikacją: {miasto1}')
print(f'Po modyfikacją: {id(miasto1)}')


show2(dict(miasto1))
print(f'Po funkcji: {miasto1}')

print()
print()
print()



















