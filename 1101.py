while True:
    n, m = map(int, input().split())
    sum = 0
    if n <= 0 or m <= 0:
        break;
    else:
        if m<n:
            aux = m
            m = n
            n = aux
        for i in range(n, m+1):
            print(i, end=" ")
            sum += i;
    print(f"Sum={sum}")
