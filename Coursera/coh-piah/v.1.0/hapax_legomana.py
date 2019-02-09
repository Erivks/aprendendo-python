# HAPAX LEGOMANA #
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def hapax_legomana(texto):
    novo_texto = tirar_caracteres(texto)
    palavras = lista_palavras(novo_texto)
    total_palavras = len(palavras)
    hlr =  n_palavras_unicas(palavras) / total_palavras
    return hlr