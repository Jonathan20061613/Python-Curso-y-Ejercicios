# Diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Jonathan', 'Apellido':'Jimenez', 'Edad':20, 1:'Python'}
print(my_other_dict)

print('---------------------------------------------------------------------------------------')

my_dict = {
    'Nombre':'Jonathan', 
    'Apellido':'Jimenez', 
    'Edad':20, 
    'Lenguajes': {
        'Python',
        'Swift',
        'Kotlin'
    },
    1: 1.60
}

print(len(my_dict))
print(my_dict)

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Pedro'
print(my_dict[1])
print(my_dict)

my_dict['Calle'] = 'Calle Jonathan'
print(my_dict)

del my_dict['Calle']
print(my_dict)

my_dict = {
    'Nombre':'Jonathan', 
    'Apellido':'Jimenez', 
    'Edad':20, 
    'Lenguajes': {
        'Python',
        'Swift',
        'Kotlin'
    },
    1: 1.60
}

print('Nombre' in my_dict)
print('Jonathan' in my_dict)
print('Jonathan' in my_dict.values())

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print('-------------------------------------------')

my_list = ['Nombre', 1, 'Piso']
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

print('-------------------------------------------')

my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict)

print('-------------------------------------------')

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

print('-------------------------------------------')

my_new_dict = dict.fromkeys(my_dict, 'J.A.J.A')
print(my_new_dict)

print('-------------------------------------------')

my_values = my_new_dict.values()
print(type(my_values))
print(my_new_dict.values())

print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))