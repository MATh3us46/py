salario = float(input())
if salario >= 0 and salario <= 400.00:
    ajuste = salario * 0.15
    nsalario = salario + ajuste
    print('Novo salario: {:.2f}'.format(nsalario))
    print('Reajuste ganho: {:.2f}'.format(ajuste))
    print('Em percentual: 15 %')
elif salario > 400.00 and salario <= 800.00:
    ajuste = salario * 0.12
    nsalario = salario + ajuste
    print('Novo salario: {:.2f}'.format(nsalario))
    print('Reajuste ganho: {:.2f}'.format(ajuste))
    print('Em percentual: 12 %')
elif salario > 800.00 and salario <= 1200.00:
    ajuste = salario * 0.10
    nsalario = salario + ajuste
    print('Novo salario: {:.2f}'.format(nsalario))
    print('Reajuste ganho: {:.2f}'.format(ajuste))
    print('Em percentual: 10 %')
elif salario > 1200.00 and salario <= 2000.00:
    ajuste = salario * 0.07
    nsalario = salario + ajuste
    print('Novo salario: {:.2f}'.format(nsalario))
    print('Reajuste ganho: {:.2f}'.format(ajuste))
    print('Em percentual: 7 %')
elif salario > 2000.00:
    ajuste = salario * 0.04
    nsalario = salario + ajuste
    print('Novo salario: {:.2f}'.format(nsalario))
    print('Reajuste ganho: {:.2f}'.format(ajuste))
    print('Em percentual: 4 %')