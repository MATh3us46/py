x, y = map(int,input().split())
if (x < y):
    time = x - y
    time = time * -1
else:
    time = y + 24 - x
print(f"O JOGO DUROU {time} HORA(S)")