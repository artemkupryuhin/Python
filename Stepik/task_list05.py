src_lst = [int(i) for i in input().split()]
x = int(input())
out_lst = []
cnt_lst = 0
for i in range(len(src_lst)):
        if x == src_lst[i]:
                out_lst.append(i)
if out_lst == []:
        print('Отсутствует')
else:
        print(*sorted(out_lst))