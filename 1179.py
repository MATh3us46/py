par = []
impar = []

for i in range(15):
    x = int(input())
    
    if x % 2 == 0:
        par.append(x)
        if len(par) == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
    else:
        impar.append(x)
        if len(impar) == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()

for j in range(len(impar)):
    print(f"impar[{j}] = {impar[j]}")
for j in range(len(par)):
    print(f"par[{j}] = {par[j]}")
