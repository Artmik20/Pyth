with open('file2.txt', 'w') as my_f2:
    num = f'{input("Введите числа через пробел: ")}'
    my_f2.write(num)
with open('file2.txt', 'r') as my_f2:
    a = my_f2.readline()
    b = map(int, a.split())
    print(sum(b))
