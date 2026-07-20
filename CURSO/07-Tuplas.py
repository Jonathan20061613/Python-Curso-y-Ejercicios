# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.60, 'Jonathan', 'Jimenez', 'J.A.J.A', 'Jonathan')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

# print(my_tuple[4]) -> Esto es un Error
# print(my_tuple[-6]) -> Esto es un Error

print(my_tuple.count('Jonathan'))
print(my_tuple.index('Jimenez'))

# my_tuple[1] = 1.80 -> Esto es un error
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:4])

my_tuple = list(my_tuple)
print(type(my_tuple))

print('-----------------------------------------')

my_tuple[4] = 'Andres'
my_tuple.insert(1, 'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

print('-----------------------------------------')

# del my_tuple -> Esto es un Error
# print(my_tuple)