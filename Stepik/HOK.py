# Определение НОК
a = int(input())
b = int(input())
fl = True
if a >= b:
    greater = a
else:
    greater = b

while fl:
    if ((greater % a == 0) and (greater % b == 0)):
        fl = False
    else: 
        greater += 1

print(str(greater))