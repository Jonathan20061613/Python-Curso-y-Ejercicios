# Listas
my_list = list()
my_other_list = []

print(len(my_list))

print('----------------------------------------------')

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(type(my_list))
print(len(my_list))

print('----------------------------------------------')
# Posiciones de Elementos

my_other_list = [35, 1.60, 'Jonathan', 'Jimenez']

print(my_other_list)
print(type(my_other_list))
print(len(my_other_list))

print('--------------')

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])

print('--------------')

print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])

#print(my_other_list[4]) <- Esto es un error
#print(my_other_list[-5]) <- Esto es un error

print('-----------------------------')

age, height, name, surname = my_other_list
print(age)
print(height)
print(name)
print(surname)

print('-----------------------------')
# my_other_list = [35, 1.60, 'Jonathan', 'Jimenez']
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(height)
print(age)
print(surname)

print('-----------------------------')
# Concatenacion de Listas

print(my_list + my_other_list)

print('-----------------------------')
# Metodos
my_other_list = [35, 1.60, 'Jonathan', 'Jimenez']

print(my_other_list.count('Jonathan'))

my_other_list.append('J.A.J.A')
print(my_other_list)

my_other_list.insert(1, 'Rojo')
print(my_other_list)

my_other_list[1] = 'Azul'
print(my_other_list)

my_other_list.remove('Azul')
print(my_other_list)

print('----------------')
my_list = [35, 24, 62, 52, 30, 30, 17]

my_list.remove(30)
print(my_list)

print(my_list)
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_new_list.append(2)
my_new_list.append(39)
my_new_list.append(42)
my_new_list.append(25)
print(my_new_list)

print(my_new_list[1:2])

print('-----------------------------')

my_list = 'Hola Python'
print(my_list)
print(type(my_list))

