my_f = open('file1.txt', 'w')

with my_f:
    while True:
        b = (input("Введите текст "))
        my_f.write(f"{b}\n")

        if not b:
            break






