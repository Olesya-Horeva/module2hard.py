def generate_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result


num = 0
while num < 3 or num > 21:
    num = int(input("Введите число для пароля от 3 до 20: "))
password = generate_password(num)
print(f"пароль для числа {num}: {password}")
print('Супер, вы сбежали')
