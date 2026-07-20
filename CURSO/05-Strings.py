# String

my_string = 'My String'
my_other_string = 'My otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = 'Este es un string\ncon salto de linea'
print(my_new_line_string)

my_tab_string = '\tEste es un String con salto de linea'
print(my_tab_string)

my_scape_string = '\\tEste es un String con salto de linea \\n escapado'
print(my_scape_string)

# Formateo de strings
name, surname, age = 'Jonathan', 'Jimenez', 20
print('Con Estilo Viejo ----------------------------------------------------')
print('Mi Nombre es %s %s. Y Mi edad es: %d' %(name, surname, age))

print('Con Estilo Nuevo ----------------------------------------------------')
print('Mi Nombre es {} {}. Y Mi edad es: {}' .format(name, surname, age))

print('Con Interpolación de F String ---------------------------------------')
print(f'Mi Nombre es {name} {surname}. Y Mi edad es: {age}')

print('----------------------- Ejemplo -----------------------')
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print('--------------------------------------------------------')
# Desempaquetado de Caracteres
nombre = 'Jonathan'
a, b, c, d, e, f, g, h = nombre
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print('--------------------------------------------------------')
# Division de Strings
nombre_slice = nombre[1:3]
print(nombre_slice)

nombre_slice = nombre[1:]
print(nombre_slice)

nombre_slice = nombre[-2]
print(nombre_slice)

nombre_slice = nombre[1:2:4]
print(nombre_slice)

# Reverse
reversed_name = name[::-1]
print(reversed_name)

print('--------------------------------------------------------')
# Metodos o Funciones de Strings
print(name.capitalize())
print(name.upper())
print(name.count('t'))
print(name.lower())
print(name.isnumeric())
print('1'.isnumeric())
print(name.lower().islower())
print(name.startswith('J'))
