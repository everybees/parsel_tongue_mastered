# number = int(input('Enter two digit numbers'))
for i in range(10, 100):
    if (i ** 2) % 100 == i:
        if len(str(i * i)) == 3:
            print(i)
