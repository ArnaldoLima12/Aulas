def busca_sequencial(lista, alvo):
    """
    Realiza uma busca sequencial na lista e retorna a posição do alvo ou -1 se não estiver presente.
    """
    if not lista:  # Verifica se a lista está vazia
        return -1

    for i, elemento in enumerate(lista):
        if elemento == alvo:
            return i
    return -1


def busca_binaria(lista, alvo):
    """
    Realiza uma busca binária na lista e retorna a posição do alvo ou -1 se não estiver presente.
    A lista deve estar ordenada para que a busca binária funcione corretamente.
    """
    if not lista:  # Verifica se a lista está vazia
        return -1

    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


def testar_buscas():
    # Criando uma lista de números inteiros ordenados para testar as implementações
    lista_teste = [2, 4, 6, 8, 10]

    # Realizando testes com diferentes casos
    casos_teste = [8, 13]

    for alvo in casos_teste:
        # Busca sequencial
        posicao_sequencial = busca_sequencial(lista_teste, alvo)
        print(f"Busca sequencial: O número {alvo} está na posição {posicao_sequencial}" if posicao_sequencial != -1
              else f"Busca sequencial: O número {alvo} não está presente na lista")

        # Busca binária
        posicao_binaria = busca_binaria(lista_teste, alvo)
        print(f"Busca binária: O número {alvo} está na posição {posicao_binaria}" if posicao_binaria != -1
              else f"Busca binária: O número {alvo} não está presente na lista")


def comparar_eficiencia():
    # Lista maior para testar a eficiência
    lista_grande = list(range(1000000))

    alvo_presente = 999999
    alvo_ausente = 1000000

    # Busca sequencial
    comparações_sequencial_presente = busca_sequencial(
        lista_grande, alvo_presente)
    print(
        f"Busca sequencial - Número de comparações para encontrar o alvo presente: {comparações_sequencial_presente}")

    comparações_sequencial_ausente = busca_sequencial(
        lista_grande, alvo_ausente)
    print(
        f"Busca sequencial - Número de comparações para encontrar o alvo ausente: {comparações_sequencial_ausente}")

    # Busca binária
    lista_ordenada = sorted(lista_grande)
    comparações_binaria_presente = busca_binaria(lista_ordenada, alvo_presente)
    print(
        f"Busca binária - Número de comparações para encontrar o alvo presente: {comparações_binaria_presente}")

    comparações_binaria_ausente = busca_binaria(lista_ordenada, alvo_ausente)
    print(
        f"Busca binária - Número de comparações para encontrar o alvo ausente: {comparações_binaria_ausente}")


# Testando as implementações e comparando eficiência
testar_buscas()
comparar_eficiencia()
