n = int(input())
if 2 < n < 1000:
    for i in range(1, 11):
        resultado = i * n
        print(f'{i} x {n} = {resultado}')