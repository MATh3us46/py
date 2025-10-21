m = [[0 for j in range(12)] for i in range(12)]
l = int(input())
t = input().strip()  

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())


if t == 'S':
    soma = sum(m[l])
    print(f"{soma:.1f}")
    
elif t == 'M':
    media = sum(m[l]) / 12
    print(f"{media:.1f}")
