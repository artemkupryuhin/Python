a = int(input())
prog01 = 'программист'
prog02 = 'программиста'
prog03 = 'программистов'

ost01 = a % 100
if ost01 >= 11 and ost01 <= 19:
    print(str(a) + ' '+ prog03)
else:
    ost02 = a % 10
    if ost02 == 1:
        print(str(a) + ' '+ prog01)
    elif ost02 == 2 or ost02 == 3 or ost02 == 4:
        print(str(a) + ' '+ prog02)
    else:
        print(str(a) + ' '+ prog03)