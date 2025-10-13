a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

maiorab = (a + b + abs(a - b)) / 2
maiorabc = (maiorab + c + abs(maiorab - c)) / 2
print('{:.0f} eh o maior'.format(maiorabc))