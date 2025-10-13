hi, mi, hf, mf = map(int, input().split())

hora = hf - hi
minutos = mf - mi

if minutos < 0:
    minutos += 60
    hora -= 1 

if hora < 0:
    hora += 24

if hi == hf and mi == mf:
    hora = 24
    minutos = 0

print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")
