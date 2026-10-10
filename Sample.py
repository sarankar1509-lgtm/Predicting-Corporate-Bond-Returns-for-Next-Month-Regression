def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci_series(limit):
    a, b = 0, 1
    series = []

    while a <= limit:
        if is_prime(a):
            series.append((a, "Prime"))
        else:
            series.append((a, "Not Prime"))
        a, b = b, a + b

    return series


limit = 100
result = fibonacci_series(limit)

for num, status in result:
    print(f"{num} - {status}")
