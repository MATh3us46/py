vitoria_inter = 0
vitoria_gremio = 0
empates = 0
total_grenais = 0

while True:
    inter, gremio = map(int, input().split())
    total_grenais += 1

    if inter > gremio:
        vitoria_inter += 1
    elif gremio > inter:
        vitoria_gremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = int(input())
    
    if novo_grenal == 2:
        break

print(f"{total_grenais} grenais")
print(f"Inter:{vitoria_inter}")
print(f"Gremio:{vitoria_gremio}")
print(f"Empates:{empates}")

if vitoria_inter > vitoria_gremio:
    print("Inter venceu mais")
elif vitoria_gremio > vitoria_inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
