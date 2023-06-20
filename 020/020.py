frase = input('Digite uma frase: ')
print()


def quantidade_string(string):
    string = len(frase)
    return string


def conta_pontuacao(string):
    pontuacoes = ',!'
    contador = 0
    for char in string:
        if char in pontuacoes:
            contador += 1
    return contador


def conta_numeros(string):
    string = string.lower()
    numeros = '0123456789'
    return sum(string.count(i) for i in numeros)


def conta_vogais(string):
    string = string.lower()
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais)


q = quantidade_string(frase)
p = conta_pontuacao(frase)
n = conta_numeros(frase)
v = conta_vogais(frase)


print(f'a) Quantidade caracteres tem a string: {q}')
print(f'b) Quantidade caracteres são de pontuação: {p}')
print(f'c) Quantidade caracteres são de número: {n}')
print(f'd) Quantidade de caracteres vogais: {v}')
