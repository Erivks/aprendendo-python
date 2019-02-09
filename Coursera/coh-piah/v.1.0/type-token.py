# TYPE TOKEN #
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
    
def n_palavras(texto):
    sentencas = separa_sentencas(texto)
    frases = lista_frases(sentencas)
    palavras = lista_palavras(frases)
    return palavras

def type_token(texto):
    palavras = n_palavras(texto)
    total_palavras = len(palavras)
    ttr = n_palavras_diferentes(palavras) / total_palavras
    return ttr
