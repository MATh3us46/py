t = int(input())
for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    conta = 0;

    while pa<=pb:
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        conta+=1
        if conta > 100:
            break

    if conta > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{conta} anos.")