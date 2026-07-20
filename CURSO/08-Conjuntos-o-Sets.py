# Sets - Conjuntos
my_set = set() # Un set no es una estructura ordenada, y este no admite repetidos
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente esto es un Dict -> Diccionario

my_other_set = {'Jonathan', 'Jimenez', 20}
print(type(my_other_set))

print(len(my_other_set))

print('----------------------------------')
my_other_set.add('J.A.J.A')
print(my_other_set)

my_other_set.add('J.A.J.A')
print(my_other_set)

print('Jonathan' in my_other_set)
print('Jonatha' in my_other_set)

my_other_set.remove('Jonathan')
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set

my_set = {'Jonathan', 'Jimenez', 20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'}))

print(my_new_set.difference(my_set))