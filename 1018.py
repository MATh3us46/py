c = int(input())
print(c)
print(c // 100,'nota(s) de R$ 100,00')
c %= 100
print(c // 50,'nota(s) de R$ 50,00')
c %= 50
print(c // 20,'nota(s) de R$ 20,00')
c %= 20
print(c // 10,'nota(s) de R$ 10,00')
c %= 10
print(c // 5,'nota(s) de R$ 5,00')
c %= 5
print(c // 2,'nota(s) de R$ 2,00')
c %= 2
print(c // 1,'nota(s) de R$ 1,00')
c %= 1