input_str = input().lower().split()
list_spis = input_str
set_spis = list_spis
dic_sl={}

for i in range(len(set_spis)):
    count = 0
    for j in range(len(list_spis)):
        if set_spis[i] == list_spis[j]:
            count += 1
    dic_sl[list_spis[i]] = count

for key, value in dic_sl.items():
    print(key, value)