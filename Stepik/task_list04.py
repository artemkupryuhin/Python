zpt = int(input())
lst = []
for i in range(zpt):
    for j in range(i+1):
        lst.append(i+1)
for n in lst[:zpt]:
    print(n, end=' ')