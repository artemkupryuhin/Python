lst = [1, 22, 3, 43, 5, 6, 3]

def modify_list(l):
    lst_new = l[:]
    for i in range(len(l)):
        if lst_new[i] % 2 != 0:
            ind = l.index(lst_new[i])
            del l[ind]
    for j in range(len(l)):
        l[j] = int(l[j] / 2)

modify_list(lst) 

print(lst)