N = int(input())
if 1 < N < 1000:
    for linhas in range(N):
        linhas += 1
        primeiro = linhas
        segundo = linhas ** 2
        terceiro = linhas ** 3
        print(f"{primeiro} {segundo} {terceiro}")
        print(f"{primeiro} {segundo + 1} {terceiro + 1}")