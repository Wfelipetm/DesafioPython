def calcular_terreno(frente, fundos):
    valorm2 = 7592.00
    area = frente * fundos
    valorterreno = valorm2 * area
    return area, valorterreno

def obter_medida_terreno(medida):
    while True:
        try:
            valor = float(input(f'Qual a medida do {medida} do terreno? '))
            if valor <= 0:
                print('Por favor, insira um valor válido maior que zero.')
            else:
                return valor
        except ValueError:
            print('Por favor, insira um valor numérico válido.')
frente = obter_medida_terreno('frente')
fundos = obter_medida_terreno('fundo')

area_terreno, valor_terreno = calcular_terreno(frente, fundos)

print('A área do terreno é: {:.2f}'.format(area_terreno))
print('O valor do terreno é: {:.2f}'.format(valor_terreno))

