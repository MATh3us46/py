i = 3
j = 2
S = 1
for n in range(1, 40):
    S = S + i/j
    i+=2
    j*=2

print(f"{S:.2f}")
