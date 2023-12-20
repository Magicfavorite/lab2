while True:

    a = int(input("Введите первое число в диапозоне"))
    b = int(input("Введите второе число в диапозоне"))
    c = int(input("Введите число"))
    if c < a and c > b:
        break

    for i in range(a,b+1):
        if i == c:
            print("!" + str(c) + "!", end=" ")
            continue
        print(i, end=" ")




