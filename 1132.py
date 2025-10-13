soma = 0 
x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

for numero in range(inicio, fim + 1):
    if not numero % 13 == 0:
        soma += numero
print(soma)