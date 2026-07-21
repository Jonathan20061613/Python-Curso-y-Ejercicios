# Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

print('---------------------------------------------')

class Person:
    def __init__(self):
        self.name = 'Jonathan'
        self.surname = 'Jimenez'

my_person = Person()
print(f'{my_person.name} {my_person.surname}')

print('---------------------------------------------')

class Person:
    def __init__(self, name, surname, alias = 'Sin Alias'):
        self.name = name
        self.surname = surname
        self.full_name = f'{name} {surname}, alias ({alias})'

    def walk(self):
        print(f'{self.full_name} esta caminando.')


my_person = Person('Jonathan', 'Jimenez')
print(f'{my_person.name} {my_person.surname}')
print(f'{my_person.full_name}')
my_person.walk()

print('--------------------------')

my_other_person = Person('Jonathan', 'Jimenez', 'J.A.J.A')
print(my_other_person.full_name)
my_other_person.walk()
print('=========================================')
my_other_person.full_name = 'Jonathan Jimenez (El loco de la programacion)'
print(my_other_person.full_name)

print('---------------------------------------------')