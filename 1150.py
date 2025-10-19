x = int(input())
z = int(input())

while(z <= x):
    z = int(input())

soma = 0
conta = 0

for i in range(x, z):
    soma += i
    conta += 1
    if soma >= z:
        print(conta)
        break