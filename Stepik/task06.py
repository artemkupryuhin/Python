a = int(input())
b = int(input())
c = int(input())

if a > b and a > c and b > c:
    print(a, c, b, sep='\n')
if a > b and a > c and b < c:
    print(a, b, c, sep='\n')

if b > a and b > c and a > c:
    print(b, c, a, sep='\n')
if b > a and b > c and a < c:
    print(b, a, c, sep='\n')

if c > a and c > b and a > b:
    print(c, b, a, sep='\n')
if c > a and c > b and a < b:
    print(c, a, b, sep='\n')
    
if a == b and b > c:
    print(a, c, b, sep='\n')
elif a == b and b < c:
    print(c, a, b, sep='\n')
elif a == c and a > b:
    print(a, b, c, sep='\n')
elif a == c and a < b:
    print(b, a, c, sep='\n')
elif b == c and c > a:
    print(b, a, c, sep='\n')
elif b == c and c < a:
    print(a, c, b, sep='\n')
elif b == c == a:
    print(a, c, b, sep='\n')