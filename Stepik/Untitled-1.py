cars = ['audi', 'bmw', 'subaru','toyota', 'bMW']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    elif car.lower() == 'audi':
        print(car.lower())
    else:
        print(car.title())

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user not in banned_users:
    print(user + ' not in list')
else:
    print(user + ' in list')

test_list = []
test_list = [value for value in range(1,10)]
del test_list[:]
if test_list:
    print('list is not empty')
    print(test_list)
else:
    print('list is empty')

#Dictionary
alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'black', 'points': 15}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print(alien_1)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages)
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
for key, value in favorite_languages.items():
    print('\nKey - ' + key)
    print('Value - ' + value)

for key in favorite_languages.keys():
    print(key)
for value in favorite_languages.values():
    print(value)  