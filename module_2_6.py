def generate_password(n):
    pairs = []
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append((i, j))
    for i, j in pairs:
        result += f"{i}{j}"

    return result
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Пожалуйста, введите число в диапазоне от 3 до 20.")