a, b, c = map(float, input().split())
delta = (b ** 2) - 4 * a * c
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + pow(delta, 0.5))/ (2 * a)
    r2 = (-b - pow(delta, 0.5))/ (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))