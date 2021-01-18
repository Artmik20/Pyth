with open('file1.txt', 'r') as my_f2:
    lines = my_f2.readlines()
    for line in lines:
        new_str = ''.join((i if i in '1234567890' else '') for i in line)
        new_str2 = [int(i) for i in new_str.split()]
        print(f'{line.split()[0]} {sum(new_str2)}')
