#
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+", that's great")
    print("-------------------------------\n")

pizzas = ['pizza1', 'pizza2', 'pizza3']
for pizza in pizzas:
    print('I like '+ pizza)

#Создание числовых списков

#Функция range()
for num in range(1,3):
    print(num)

#Использование range() для создания числового списка
numbers = list(range(1,5))
print(numbers)

#Функция range() также может генерировать числовые последовательности, пропуская числа в заданном диапазоне
numbers = list(range(1,5,2))
print(numbers)


