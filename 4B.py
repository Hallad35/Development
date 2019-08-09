serials = {
    'Reign' : 7.8,
    'Game of Thrones' : 8.5,
    'Anne with an E' : 8.1,
    'Peaky Blinders' : 8.7,
    'The Big Bang Theory' : 8,
    'Riverdale' : 7.3,
    'Lucyfer': 8,
    "The Handmaid's Tale" : 8.1,
    'Jessica Jones' : 8,
    'La casa de papel' : 7.8
    }

print(list(serials.keys()))
print('******************************************')

name = input('Jaki serial chcesz obejrzec? ')
print('Serial {} otrzymał ocenę {}'.format(name, serials[name]))

print('******************************************')
