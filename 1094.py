x = int(input()) 
tc = 0 
tco = 0 
tr = 0 
ts = 0 
for repeticoes in range(x):
    a, b = input().split()  
    a = int(a) 

    tc += a
    if b == 'C':
        tco += a
    if b == 'R':
        tr += a
    if b == 'S':
        ts += a

pc = (tco/tc) * 100
pr = (tr/tc) * 100
ps = (ts/tc) * 100

print(f"Total: {tc} cobaias")
print(f"Total de coelhos: {tco}")
print(f"Total de ratos: {tr}")
print(f"Total de sapos: {ts}")
print(f"Percentual de coelhos: {pc:.2f} %")
print(f"Percentual de ratos: {pr:.2f} %")
print(f"Percentual de sapos: {ps:.2f} %")