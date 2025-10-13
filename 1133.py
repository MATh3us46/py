x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

for valores in range(inicio + 1, fim):
    if valores % 5 == 2 or valores % 5 == 3:
        print(valores)