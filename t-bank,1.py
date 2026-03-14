a, b = 0, 1
result = []

st, end = map(int, input().split())

while a <= end:
    if a >= st:
        result.append(a)
    a, b = b, a + b

print(*result) if result else print("В заданном диапазоне нет чисел Фибоначчи")
