def obter_quantidade_dias_trabalhados():
    while True:
        try:
            dias_trabalhados = int(input('Digite a quantidade de dias trabalhados: '))
            if dias_trabalhados > 0:
                return dias_trabalhados
            else:
                print("Quantidade inválida. Digite um valor maior que zero.")
        except ValueError:
            print("Quantidade inválida. Digite um valor numérico.")

def calcular_anos_meses_dias(dias_trabalhados):
    anos = dias_trabalhados // 365
    dias_trabalhados %= 365
    meses = dias_trabalhados // 30
    dias_trabalhados %= 30

    return anos, meses, dias_trabalhados

def exibir_resultado(anos, meses, dias):
    print(f'{anos} anos, {meses} meses, {dias} dias')

def main():
    dias_trabalhados = obter_quantidade_dias_trabalhados()
    anos, meses, dias = calcular_anos_meses_dias(dias_trabalhados)
    exibir_resultado(anos, meses, dias)

main()
