sum1, sum2 = 0, 0
while true:
    zpt = int(input())
    sum1 += zpt
    sum2 += zpt**2
    if sum1 == 0:
        print(sum2)
        break