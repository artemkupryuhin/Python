chisla = (0,1,2,3,4,5,6,7,8,9)
output_str = ''

with open("D:\\GitHub\\MyRepo\\Python\\Stepik\\dataset_3363_2.txt") as inf: #read file
    for line in inf:
        line = line.strip()

sym = ['a','b','c']
ch = ''

for i in range(len(line)):
    if line[i] not in chisla:
        sym += line[i]
    else:
        ch += line[i]