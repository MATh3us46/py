N = int(input())

if 0 < N < 13:
    resultado = 1
    for i in range(1, N + 1):
        resultado *= i
    print(resultado)