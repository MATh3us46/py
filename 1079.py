n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    a = a * 2
    b = b * 3
    c = c * 5
    resultado = (a + b + c) / 10
    print('{:.1f}'.format(resultado))