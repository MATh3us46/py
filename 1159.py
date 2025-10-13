x = int(input())
while x != 0:
    soma = 0
    if (x % 2) == 1:
        x += 1
    for i in range(5):
        soma += x + 2 * i
    print(soma)
    x = int(input())