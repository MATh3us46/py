c = int(input())
c1 = c // 3600
c %= 3600
c2 = c // 60
c %= 60
print(f'{c1}:{c2}:{c}')