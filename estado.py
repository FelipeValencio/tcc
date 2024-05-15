import csv


def ler_tabela(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        tabela = [linha for linha in leitor_csv]
    return tabela


def validar_tabela(tabela):
    ids_encontrados = set()
    perguntas_encontradas = set()

    for num_linha, linha in enumerate(tabela[1:]):
        if not linha[0]:
            print(f"Erro: O campo ID é obrigatório e está vazio (Erro na linha {num_linha + 2}).")
            return False
        else:
            # Verificar IDs duplicados
            id_atual = linha[0]
            if id_atual in ids_encontrados:
                print(f"Erro: ID '{id_atual}' duplicado encontrado na linha {num_linha + 2}.")
                return False
            else:
                ids_encontrados.add(id_atual)

        if not linha[1]:
            print(f"Erro: O campo Perguntas é obrigatório e está vazio (Erro na linha {num_linha + 2}).")
            return False
        else:
            # Verificar perguntas duplicados
            pergunta_atual = linha[1]
            if id_atual in perguntas_encontradas:
                print(f"Erro: ID '{pergunta_atual}' duplicado encontrado na linha {num_linha + 2}.")
                return False
            else:
                perguntas_encontradas.add(pergunta_atual)

        if not linha[2] and not linha[3]:
            print(f"Erro: O campo Recomendações é obrigatório e está vazio (Erro na linha {num_linha + 2}).")
            return False

    return True


def maquina_de_estado(tabela_estado):
    if not validar_tabela(tabela_estado):
        print("Erro: A tabela não atende aos requisitos.")
        return

    controles = []
    estado_atual = 1
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

    controles = filter(None, controles)

    with open('output.txt', 'w') as f:
        for line in controles:
            f.write(f"{line}\n")


def encontrar_indice_por_id(tabela, id_desejado):
    for indice, linha in enumerate(tabela):
        if linha[0] == id_desejado:
            return indice
    return None


maquina_de_estado(ler_tabela('tabela_estado.csv'))
