n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n1 = n1 * 2
n2 = n2 * 3
n3 = n3 * 4
n4 = n4 * 1
media = (n1 + n2 + n3 + n4) / 10
print ('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print ('Nota do exame:',exame)
    media_final = (media + exame) / 2
    if media_final < 5.0:
        print('Aluno reprovado.')
        print ('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno aprovado.')
        print ('Media final: {:.1f}'.format(media_final))