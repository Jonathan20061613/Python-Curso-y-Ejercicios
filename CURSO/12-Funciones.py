# Funciones 
def my_function():
    print('Esto es una funcion')

my_function()

def sum_two_values(num1, num2):
    print(num1 + num2)

sum_two_values(45, 65)
sum_two_values(23, 34)
sum_two_values(45, 98)
sum_two_values(34, 67)
sum_two_values(42, 65)

print('-----------------------------------------------------')

def sum_two_values_with_return(num1, num2):
    return num1 + num2

resultado = sum_two_values_with_return(23, 45)
print('El resultado de la suma es: ', resultado)

resultado = sum_two_values_with_return(32, 56)
print('El resultado de la suma es: ', resultado)

resultado = sum_two_values_with_return(12, 76)
print('El resultado de la suma es: ', resultado)

resultado = sum_two_values_with_return(56, 34)
print('El resultado de la suma es: ', resultado)

resultado = sum_two_values_with_return(76, 78)
print('El resultado de la suma es: ', resultado)

print('-----------------------------------------------------')

def print_name(name, surname):
    print(f'{name} {surname}')

print_name(name= 'Jonathan', surname= 'Jimenez')

print('-----------------------------------------------------')

def print_name_with_default(name, surname, alias = 'Sin Alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Jonathan', 'Jimenez')

print('-----------------------------------------------------')

def print_text(*texts):
    for text in texts:
        print(text)
        
print_text('Hola', 'Jonathan', 'Python', 'Jimenez')

print('-----------------------------------------------------')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts('Hola', 'Jonathan', 'Python', 'Jimenez')