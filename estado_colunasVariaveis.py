import csv


def ler_tabela(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        tabela = [linha for linha in leitor_csv]
    return tabela


def validar_tabela(tabela):
    # Dicionário para armazenar as colunas marcadas como obrigatórias e seu índice na tabela
    colunas_obrigatorias = {}

    # Encontrar as colunas marcadas como obrigatórias
    for indice, valor in enumerate(tabela[1]):
        if valor == "obrigatorio":
            colunas_obrigatorias[indice] = tabela[0][indice]  # Armazenar o nome da próxima coluna

    # Dicionário para armazenar as colunas marcadas de recomendações e seu índice na tabela
    colunas_recomendacoes = {}

    # Encontrar as colunas marcadas como obrigatórias
    for indice, valor in enumerate(tabela[0]):
        if valor == "Recomendação Sim":
            colunas_recomendacoes[indice] = tabela[0][indice]  # Armazenar o nome da próxima coluna
        if valor == "Recomendação Não":
            colunas_recomendacoes[indice] = tabela[0][indice]  # Armazenar o nome da próxima coluna

    for num_linha, linha in enumerate(tabela[2:]):
        for indice_coluna in colunas_obrigatorias.keys():
            if not linha[indice_coluna]:
                print(f"Erro: O campo '{colunas_obrigatorias[indice_coluna]}' é obrigatório e está vazio (Erro na linha {num_linha + 3}).")
                return False
        if not linha[list(colunas_recomendacoes.keys())[0]] and not linha[list(colunas_recomendacoes.keys())[1]]:
            print(f"Erro: O campo Recomendações é obrigatório e está vazio (Erro na linha {num_linha + 3}).")
            return False

    return True


def maquina_de_estado(tabela_estado):
    if not validar_tabela(tabela_estado):
        print("Erro: A tabela não atende aos requisitos.")
        return

    controles = []
    estado_atual = 2
    while (estado_atual is not None or isinstance(estado_atual, int)) and estado_atual < len(tabela_estado):
        print("Estado atual: " + str(estado_atual))
        pergunta = tabela_estado[estado_atual][1]
        controles_sim = tabela_estado[estado_atual][2]
        controles_nao = tabela_estado[estado_atual][3]
        print("Pergunta:", pergunta)
        resposta = input("Responda com 'Sim' ou 'Não': ").lower()

        if resposta == 'sim':
            [controles.append(c.strip()) for c in controles_sim.split("\n") if c.strip() not in controles]
            print(tabela_estado[estado_atual][4])
            estado_atual = encontrar_indice_por_id(tabela_estado, tabela_estado[estado_atual][4])
        elif resposta == 'não' or resposta == 'nao':
            [controles.append(c.strip()) for c in controles_nao.split("\n") if c.strip() not in controles]
            estado_atual = encontrar_indice_por_id(tabela_estado, tabela_estado[estado_atual][5])
        else:
            print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
            continue

        print("Controles aplicáveis:\n", controles)
        print("\n")

    with open('output.txt', 'w') as f:
        for line in controles:
            f.write(f"{line}\n")


def encontrar_indice_por_id(tabela, id_desejado):
    for indice, linha in enumerate(tabela):
        if linha[0] == id_desejado:
            return indice
    return None


maquina_de_estado(ler_tabela('tabela_estadov2.csv'))
