with open("D:\GitHub\MyRepo\Python\Stepik\\file1.txt", 'w') as inf: #rewrite to file, all prev info will be delete
    inf.write('\nadd ' + str(111))

with open("D:\GitHub\MyRepo\Python\Stepik\\file1.txt", 'a') as inf: #append to file
    inf.write('\nadd ' + str(111))

with open("D:\GitHub\MyRepo\Python\Stepik\\file1.txt") as inf: #read file
    for line in inf:
        line = line.strip()
        print(line)