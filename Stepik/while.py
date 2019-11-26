src_lst = [int(i) for i in input().split()]
out_lst = []

len_src_lst = len(src_lst)

if len_src_lst <= 1:
    out_lst = src_lst[:]
    for n in out_lst:
        print(n, end=' ')
else:
    for i in range(len_src_lst):
        if i == 0:
            elmnt = src_lst[-1] + src_lst[i+1]
        elif i == len_src_lst-1:
            elmnt = src_lst[i-1] + src_lst[0]
        else:
            elmnt = src_lst[i-1] + src_lst[i+1]
        out_lst.append(elmnt)
    for n in out_lst:
        print(n, end=' ')
