n = int(input())
soma = 0
for i in range(0, n):
    x, y = map(int, input().split())
    if y<x:
        aux = y
        y = x
        x = aux
    for j in range(x+1, y):
        if j%2 != 0:
            soma +=j
    print(soma)
    soma = 0
