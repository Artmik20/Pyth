my_f = open('file1.txt', 'w')
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
my_f.writelines(str_list)
my_f.close()

f = open('file1.txt', 'r')
size = sum(1 for _ in f)
print(size)

f = open('file1.txt', 'r')
lines = f.readlines()
for index, value in enumerate(lines):
    number_of_words = len(value.split())
    print('Line number {} has {} words.\n'.format(index + 1, number_of_words))


