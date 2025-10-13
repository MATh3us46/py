maior = 0
count = 0
for i in range(1, 101):
    n = int(input())
    if n > maior:
        maior = n
        count = i

print(maior)
print(count)