x = int(input())
y = int(input())
soma = 0
if(y<x):
    aux = y
    y = x
    x = aux

for i in range(x+1, y):
    if(i%2!=0):
        soma+=i

print(soma)