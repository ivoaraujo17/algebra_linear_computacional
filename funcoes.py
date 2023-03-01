def produto_interno(vetor1, vetor2):
    """
    Produto interno entre dois vetores com n dimensão.\n
    :param vetor1: vetor com n dimensão com estrutura em lista ou em tupla.
    :param vetor2: mesma estrutura do vetor1
    :return: caso os vetores seja de dimensão diferentes return -1, se não retorna
     o produto_interno.
    """
    if len(vetor1) != len(vetor2):
        print('Vetores de dimenssões diferentes')
        return -1
    else:
        pi = 0
        for indice in range(len(vetor1)):
            pi += vetor1[indice] * vetor2[indice]
        pi = pi ** 0.5
        return pi


def ortogonal(vetor1, vetor2):
    """
    Verifica se dois vetores de n dimensão são ortorgonais.\n
    :param vetor1: vetor com n dimensão com estrutura em lista ou em tupla.
    :param vetor2: mesma estrutura do vetor1
    :return: True caso seja ortogonal, caso contrário False.
    """
    if produto_interno(vetor1, vetor2) == 0:
        return True
    else:
        return False


def distancia_euclidiana(vetor1, vetor2):
    """
    Calcula a distancia euclidiana entre dois vetores.\n
    :param vetor1: vetor com n dimensão com estrutura em lista ou em tupla.
    :param vetor2: mesma estrutura do vetor1
    :return: se os vetores tiverem dimensão diferente return -1, se não irá a
        distancia.
    """
    if len(vetor1) != len(vetor2):
        print('Vetores de dimenssões diferentes')
        return -1
    else:
        distancia = 0
        for indice in range(len(vetor1)):
            subtracao = vetor1[indice] - vetor2[indice]
            distancia += subtracao**2
        distancia = distancia ** 0.5
        return distancia


def verificar_ortogonalidade_conj_vetores(lista):
    """
    Verifica se a lista de vetores passado é ortogonal.\n
    :param lista: lista de vetores que devem está em formato de lista ou tupla.
    :return: se todos forem ortogonais return True, caso algum não seja ortogonal
        return False
    """
    dimensao_do_conj_vetores = 0
    for posicao in range(len(lista)):
        if posicao == 0:
            dimensao_do_conj_vetores = len(lista[posicao])
        else:
            if len(lista[posicao]) != dimensao_do_conj_vetores:
                return -1
            else:
                for cada_vetor_ja_verificado in range(len(lista[:posicao])):
                    if not ortogonal(lista[posicao], lista[cada_vetor_ja_verificado]):
                       return False
    return True

