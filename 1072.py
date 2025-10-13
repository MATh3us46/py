inn = 0
out = 0
n = int(input())
if n < 10000:
   for entradas in range(n): 
        x = int(input()) 
        if 10 <= x <= 20:
            inn += 1
        else:
            out += 1
print(f'{inn} in')
print(f'{out} out')