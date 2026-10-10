def ficha(nome='<desconhecido>', gols=0):
    """
    -> Função para mostrar a ficha de um jogador.
    :param nome: Nome do jogador.
    :param gols: Número de gols do jogador.
    :return: Retorna a ficha do jogador.
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nomejogador = input("Nome do jogador: ")
golsjogador = input("Número de gols: ")
print(ficha(nomejogador, golsjogador))

