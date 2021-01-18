my_f = open('file1.txt', 'w')
a = 'Green 13000'
b = 'Brown 21000'
c = 'Grey 50000'
str_list = ['Grey; 50000;\n', 'Brown; 21000;\n', 'Green; 13000;\n']
my_f.writelines(str_list)
my_f.close()


f = open('file1.txt', 'r')
lines = f.readlines()
for value in lines:
    name, salary, n = value.split(';')
    salary = int(salary)
    if salary < 20000:
        print(name, salary)
f.close()












