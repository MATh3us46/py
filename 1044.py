a, b = map(int,input().split())

if(a < b):
    a, b = b, a

print("Nao sao Multiplos" if (a % b) else "Sao Multiplos")