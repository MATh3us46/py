lista = []
for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    lista.append(x)
for i in range(10):
    print(f"X[{i}] = {lista[i]}")