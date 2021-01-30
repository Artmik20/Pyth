a = {'One': 'Один',
     'Two': 'Два',
     'Three': 'Три',
     'Four': 'Четыре'}

with open('file1.txt', 'r') as my_f:
    with open('file2.txt', 'w') as my_f2:
        lines = my_f.readlines()
        for line in lines:
            b = line.split(" — ")
            my_f2.write(f'{a[b[0]]} — {b[1]}')

