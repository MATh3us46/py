cp, np, vu = input().split()
cp2, np2, vu2 = input().split()
np = int(np)
np2 = int(np2)
vu = float(vu)
vu2 = float(vu2)
multi = np * vu
multi2 = np2 * vu2
resul = multi + multi2
print('VALOR A PAGAR: R$ {:.2f}'.format(resul))