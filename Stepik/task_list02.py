src_lst = [int(i) for i in input().split()]
out_src = []
for i in src_lst:
    cnt = 0
    for j in src_lst:
        if i == j:
            cnt += 1
    if cnt >= 2 and i not in out_src:
        out_src.append(i) 
    
for elmnt in sorted(out_src):
    print(elmnt, end =' ')