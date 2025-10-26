x = int(input("Введите трёхзначное число: "))
if 100 <= x <= 999:
    digit1 = x // 100
    digit2 = (x // 10) % 10
    digit3 = x % 10
    result = (digit1 + digit2 + digit3) % 2 == 0
    print(result)
    print(True)
else:
    print(False)
