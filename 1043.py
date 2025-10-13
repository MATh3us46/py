a, b, c = map(float, input().split())
if a < b + c and b < a + c and c < b + a:
    perimetro = a + b + c
    print('Perimetro =', perimetro)
else:
    area = ((a + b) * c) / 2
    print('Area =', area)