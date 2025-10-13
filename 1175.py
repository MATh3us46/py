lista = []
for i in range(20):
    N = int(input())
    lista.append(N)

for i in range(10):
    lista[i], lista[19 - i] = lista[19 - i], lista[i]

for i in range(20):
    print(f"N[{i}] = {lista[i]}")