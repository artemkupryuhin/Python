#Списки
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[1].upper())
print(bicycles[2])
print(bicycles[3].title())

print('--------------------------')

print(bicycles[-4])
print(bicycles[-3])
print(bicycles[-2])
print(bicycles[-1])

print('--------------------------')

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#Изменение элементов в списке
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#Присоединение элементов в конец списка
motorcycles.append('ducati02')
print(motorcycles)

'''
Метод append() упрощает динамическое построение списков. Например, вы можете начать с пустого списка и добавлять в него элементы серией команд append().
'''

motorcycles02 = []
motorcycles02.append('honda')
motorcycles02.append('yamaha')
motorcycles02.append('suzuki')
print(motorcycles02)

'''
Вставка элементов в список
Метод insert() позволяет добавить новый элемент в произвольную позицию списка. Для этого следует указать индекс и значение нового элемента.
'''
motorcycles02.insert(2,'ducati')
print(motorcycles02)

#Удаление элементов из списка
#Элементы удаляются из списка по позиции или по значению.
#Если вам известна позиция элемента, который должен быть удален из списка, воспользуйтесь командой del.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

print('\n'+'='*80)

#Удаление элемента с использованием метода pop()
print('''\nУдаление элемента с использованием метода pop()
Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления.\n''')
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print('\n'+'='*80)

print('''\nИзвлечение элементов из произвольной позиции списка
Вызов pop() может использоваться для удаления элемента в произвольной позиции
списка; для этого следует указать индекс удаляемого элемента в круглых скобках.\n''')
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() +'.')

print('''\nПомните, что после каждого вызова pop() элемент, с которым вы работаете, уже не находится в списке.
Если вы не уверены в том, какой из двух способов выбрать — команду del или метод pop(), — то простое правило поможет вам определиться. Если вы собираетесь
просто удалить элемент из списка, никак не используя его, выбирайте команду del; если же вы намерены использовать элемент после удаления из списка, выбирайте
метод pop().\n''')

print('\n'+'='*80)

#Удаление элементов по значению
print('''\nУдаление элементов по значению
Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте метод remove().
Метод remove() удаляет только первое вхождение заданного значения.\n''')
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

print('\n'+'='*80)

#Упорядочение списка
print('''\nУпорядочение списка
Постоянная сортировка списка методом sort()
Метод sort() позволяет относительно легко отсортировать список. Сортировка в самом списке меняется и вернуться к исходному не получится\n''')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(cars.sort())
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the reverse sorted list:")
cars.sort(reverse=True)
print(cars)

print('\n'+'='*80)

#Временная сортировка списка функцией sorted()
print ('''\nВременная сортировка списка функцией sorted().
Чтобы сохранить исходный порядок элементов списка, но временно представить их
в отсортированном порядке, можно воспользоваться функцией sorted()\n''')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print('\n'+'='*80)

#Вывод списка в обратном порядке
print ('''\nВывод списка в обратном порядке
Чтобы переставить элементы списка в обратном порядке, используйте метод reverse(). 
Обратите внимание: метод reverse() не сортирует элементы в обратном алфавитном порядке, а просто переходит к обратному порядку списка\n''')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print('\n'+'='*80)

#Определение длины списка
print ('''\nОпределение длины списка
Вы можете быстро определить длину списка с помощью функции len()\n''')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print('Длина списка: ' + str(len(cars)))

print('\n'+'='*80)


state_list = ['Украина', 'Франция', 'Венгрия', 'Польша']
print(state_list)
print(sorted(state_list, reverse=True))

print('sfdsdgdfgds\
sdfgdgdfgfdgfdg')

help(str)

str1 = '  qwerty -'

print(str1.strip().strip('-'))
print('v1 - {} V2 - {}'.format('test1','test2'))
dir(str1)
type(str1)
int1 = 10
type(int1)

print(1 < int1 < 15)