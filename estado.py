import csv


def ler_tabela(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        tabela = [linha for linha in leitor_csv]
    return tabela


def maquina_de_estado(tabela_estado):
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


def encontrar_indice_por_id(tabela, id_desejado):
    for indice, linha in enumerate(tabela):
        if linha[0] == id_desejado:
            return indice
    return None


maquina_de_estado(ler_tabela('tabela_estado.csv'))
