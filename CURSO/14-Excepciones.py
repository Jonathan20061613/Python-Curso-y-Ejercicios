# Exception Handling - Gestion de Excepciones ó Gestion de Errores

number_one = 5  
number_two = 1

number_two = '1'

# if type(number_two) == int:
#     print(number_one + number_two)
# else:
#     print('No se cumplio')

# Try Except
try:
    print(number_one + number_two)
    print('No ha producido error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido error')

print('--------------------------------------------------')

# Try Except Else
try:
    print(number_one + number_two)
    print('No ha producido error')
except:
    print('Se ha producido error')
else: 
    # Se ejecuta si no se produce una excepcion
    print('La ejecicion continua correctamente')

print('--------------------------------------------------')

# Try Except else Finaly
try:
    print(number_one + number_two)
    print('No ha producido error')
except: # Opcional
    # Se ejecuta si no se produce una excepcion
    print('Se ha producido error')
else: 
    # Se ejecuta si no se produce una excepcion
    print('La ejecicion continua correctamente')
finally: # Opcional 
    # Se ejecuta siempre
    print('La ejecucion continua')

print('--------------------------------------------------')

# Excepciones por tipo

try:
    print(number_one + number_two)
    print('No ha producido error')
except ValueError: 
    print('Se ha producido ValueError: ', ValueError)
except TypeError: 
    print('Se ha producido TypeError: ', TypeError)

print('----------------------------')

# Captura de la informacion de la excepcion

try:
    print(number_one + number_two)
    print('No ha producido error')
except ValueError as error: 
    print('Se ha producido ValueError: ', ValueError)
    print(error)
except TypeError as error: 
    print('Se ha producido TypeError: ', TypeError)
    print(error)

print('----------------------------')

# Captura de la informacion de la excepcion en caso de que no sea el error en especifico o desconocido

try:
    print(number_one + number_two)
    print('No ha producido error')
except ValueError as error: 
    print('Se ha producido ValueError: ', ValueError)
    print(error)
except Exception as error: 
    print('Se ha producido un error de tipo: ', TypeError)
    print(error)

# Y continua con normalidad el programa y no peta la app

num_1 = 3
num_2 = 56
print(num_1 + num_2)