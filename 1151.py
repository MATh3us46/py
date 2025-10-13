N = int(input())

if 0 < N < 46:
    a = 0
    b = 1
    for i in range(N):
        if i == 0:
            print(a, end="")
        else:
            print(f" {a}", end="")
        a, b = b, a + b
print()
