import csv


def ler_tabela(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        tabela = [linha for linha in leitor_csv]
    return tabela


def maquina_de_estado(tabelaEstado):
    estado_atual = 1
    while estado_atual is None or (isinstance(estado_atual, int) and estado_atual < len(tabelaEstado)):
        pergunta = tabelaEstado[estado_atual][1]
        controles_sim = tabelaEstado[estado_atual][2]
        controles_nao = tabelaEstado[estado_atual][3]
        print("Pergunta:", pergunta)
        resposta = input("Responda com 'Sim' ou 'Não': ").lower()

        if resposta == 'sim':
            controles = controles_sim
            print(tabelaEstado[estado_atual][4])
            estado_atual = encontrar_indice_por_id(tabela, tabelaEstado[estado_atual][4])
        elif resposta == 'não':
            controles = controles_nao
            estado_atual = encontrar_indice_por_id(tabela, tabelaEstado[estado_atual][5])
        else:
            print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
            continue

        print("Controles aplicáveis:", controles)
        print("\n")


tabela = ler_tabela('estados_controles.csv')

def encontrar_indice_por_id(tabela, id_desejado):
    for indice, linha in enumerate(tabela):
        if linha[0] == id_desejado:
            return indice
    return None

maquina_de_estado(tabela)
