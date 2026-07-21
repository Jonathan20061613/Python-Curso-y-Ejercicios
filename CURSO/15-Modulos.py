# Modulos 
import module

module.sum(5, 3, 1)
module.res(40, 50, 20)
module.printValue('¡Hola, Python!')

print('-------------------------------------------------')

from module import sum, res, printValue

sum(34, 56, 70)
res(34, 56, 70)
printValue('¡Hola, Python!')

print('-----------------------------')

from math import pi as  PI

print(f'El numero PI: {PI}') # 3.141592653589793