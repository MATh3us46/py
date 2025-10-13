diai, di = input().split()
di = int(di)

hi, c, mi, c, si = input().split()
hi, mi, si = int(hi), int(mi), int(si)

dia, dt = input().split()
dt = int(dt)

ht, c, mt, c, st = input().split()
ht, mt, st = int(ht), int(mt), int(st)

inicio = di * 86400 + hi * 3600 + mi * 60 + si
termino = dt * 86400 + ht * 3600 + mt * 60 + st

duracao = termino - inicio

dr = duracao // 86400
duracao %= 86400

hr = duracao // 3600
duracao %= 3600

mr = duracao // 60
sr = duracao % 60

print(f"{dr} dia(s)")
print(f"{hr} hora(s)")
print(f"{mr} minuto(s)")
print(f"{sr} segundo(s)")