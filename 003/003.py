notab1 = float(input('Nota primeiro Bimestre: '))
notab2 = float(input('Nota segundo Bimestre: '))
notab3 = float(input('Nota terceiro Bimestre: '))
notab4 = float(input('Nota Quarto Bimestre: '))

somaNotas = notab1 + notab2 + notab3 + notab4
media = somaNotas / 4
print('Sua media Final é: ' + str(media))

mediaReal = 6
if media >= mediaReal:
    print('Você foi APROVADO!')
else:
    print('você está REPROVADO!')