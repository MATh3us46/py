n = float(input())

n100 = int(n // 100)
n %= 100
n50 = int(n // 50)
n %= 50
n20 = int(n // 20)
n %= 20
n10 = int(n // 10)
n %= 10
n5 = int(n // 5)
n %= 5
n2 = int(n // 2)
n %= 2

n = round(n * 100)

m1_00 = n // 100
n %= 100
m0_50 = n // 50
n %= 50
m0_25 = n // 25
n %= 25
m0_10 = n // 10
n %= 10
m0_05 = n // 5
n %= 5
m0_01 = n // 1
n %= 1

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(n100))
print("{:.0f} nota(s) de R$ 50.00".format(n50))
print("{:.0f} nota(s) de R$ 20.00".format(n20))
print("{:.0f} nota(s) de R$ 10.00".format(n10))
print("{:.0f} nota(s) de R$ 5.00".format(n5))
print("{:.0f} nota(s) de R$ 2.00".format(n2))

print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(m1_00))
print("{:.0f} moeda(s) de R$ 0.50".format(m0_50))
print("{:.0f} moeda(s) de R$ 0.25".format(m0_25))
print("{:.0f} moeda(s) de R$ 0.10".format(m0_10))
print("{:.0f} moeda(s) de R$ 0.05".format(m0_05))
print("{:.0f} moeda(s) de R$ 0.01".format(m0_01))
