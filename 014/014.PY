usuarios = {}

MEGABYTE = 1024 * 1024


def preenche_informacoes_usuarios():
    quantidade_usuarios = int(input("Quantidade de usuários: "))

    for i in range(1, quantidade_usuarios + 1):
        nome_usuario = input("Digite o nome do usuário " + str(i) + ": ")
        espaco_utilizado = int(input("Digite o espaço utilizado em MB pelo usuário " + str(i) + ": "))

        usuarios[nome_usuario] = espaco_utilizado * MEGABYTE


def converte_bytes_para_megabytes(espaco_em_bytes):
    return espaco_em_bytes / MEGABYTE


def cria_relatorio():
    quantidade_usuarios = len(usuarios)
    espaco_total = calcula_espaco_total()

    relatorio = "ACME Inc.    Uso do espaço em disco pelos usuários\n"
    relatorio += "----------------------------------------------------\n"
    relatorio += "Nr.  Usuário        Espaço utilizado     % do uso\n"

    numero = 1
    for nome_usuario, espaco_do_usuario in usuarios.items():
        espaco_em_mb = converte_bytes_para_megabytes(espaco_do_usuario)
        porcentagem = espaco_do_usuario * 100 / espaco_total

        texto_numero = str(numero).strip()
        texto_nome = nome_usuario.strip()
        texto_espaco = "{:.2f}".format(espaco_em_mb) + " MB"
        texto_porc = "{:.2f}".format(porcentagem) + "%"

        linha = "{:<5s}{:<15s}{:<20s}{}\n".format(texto_numero, texto_nome, texto_espaco, texto_porc)
        relatorio += linha
        numero += 1

    espaco_total_em_mb = converte_bytes_para_megabytes(espaco_total)
    relatorio += "\nEspaco total ocupado: {:.2f}".format(espaco_total_em_mb) + " MB\n"
    relatorio += "Espaco médio ocupado: {:.2f}".format(espaco_total_em_mb / quantidade_usuarios) + " MB\n"

    return relatorio


def calcula_espaco_total():
    espaco_total = 0
    for espaco_do_usuario in usuarios.values():
        espaco_total += espaco_do_usuario
    return espaco_total


def escreve_texto_no_arquivo(texto, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)
        print("Relatório salvo no arquivo " + nome_arquivo)
    except IOError:
        print("Ocorreu um erro ao salvar o relatório no arquivo:")


preenche_informacoes_usuarios()
relatorio = cria_relatorio()

print(relatorio)  # Exibir relatório no terminal

nome_arquivo = input("Digite o nome do arquivo para salvar o relatório: ")
escreve_texto_no_arquivo(relatorio, nome_arquivo)
