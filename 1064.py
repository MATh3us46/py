conta = 0
soma = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        soma+=x 
        conta+=1

print(conta,"valores positivos")
print(f"{soma/conta:.1f}")