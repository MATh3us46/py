c = int(input())
c1 = c // 365
c %= 365
c2 = c // 30
c %= 30
print(f'{c1} ano(s)')
print(f'{c2} mes(es)')
print(f'{c} dia(s)')