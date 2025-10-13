c, q = input().split()
c = int(c)
q = int(q)
if c == 1:
    num = q * 4.00
    print('Total: R$ {:.2f}'.format(num))
elif c == 2:
    num = q * 4.50
    print('Total: R$ {:.2f}'.format(num))
elif c == 3:
    num = q * 5.00
    print('Total: R$ {:.2f}'.format(num))
elif c == 4:
    num = q * 2.00
    print('Total: R$ {:.2f}'.format(num))
elif c == 5:
    num = q * 1.50
    print('Total: R$ {:.2f}'.format(num))