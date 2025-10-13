contador = 0
total = 0
while True:
    numero = int(input())
    if numero < 0:
        print(f"{total / contador:.2f}")
        break
    else:
        total += numero
        contador += 1