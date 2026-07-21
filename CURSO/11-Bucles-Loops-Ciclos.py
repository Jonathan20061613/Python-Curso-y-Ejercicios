# Loop - Ciclos - Bucles

# Bucle While
my_condition = 0

while my_condition < 10: 
    print(my_condition)
    my_condition += 2
if my_condition == 10:
    print('Mi condicion es igual a 10')
else:
    print('Mi condicion es mayor o igual que 10')

print('--------------------------------------')

print('Le ejecucion continua')

print('--------------------------------------')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se deiene la ejecucion')
        break
    print(my_condition) 

print('Le ejecucion continua')

print('--------------------------------------')

# For
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print('--------------------------------------')

my_tuple = (20, 1.60, 'Jonathan', 'Jimenez', 'J.A.J.A')

for element in my_tuple:
    print(element)

print('--------------------------------------')

my_other_set = {'Jonathan', 'Jimenez', 20}

for element in my_other_set:
    print(element)

print('--------------------------------------')

my_dict = {'Nombre':'Jonathan', 'Apellido':'Jimenez', 'Edad':20, 1:'Python'}

for element in my_dict.values():
    print(element)

print('--------------------------------------')

my_dict = {'Nombre':'Jonathan', 'Apellido':'Jimenez', 'Edad':20, 1:'Python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        break
    print('Se ejecuta')
else:
    print('El bucle for para diccionario a finalizado')

print('--------------------------------------')

my_dict = {'Nombre':'Jonathan', 'Apellido':'Jimenez', 'Edad':20, 1:'Python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('El bucle for para diccionario a finalizado')