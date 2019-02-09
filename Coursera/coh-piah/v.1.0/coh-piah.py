import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("")
    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print("")

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print("")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print("")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras(texto):
    sentencas = separa_sentencas(texto)
    frases = lista_frases(sentencas)
    palavras = lista_palavras(frases)
    return palavras

# MÉDIA DE PALAVRAS #

def lista_frases(sentencas):
    frases = []
    for sentenca in sentencas:
        frases += separa_frases(sentenca)
    print(frases)
    return frases

def lista_palavras(frases):
    palavras = []
    for frase in frases:
        palavras += separa_palavras(frase)
    print(palavras)
    return palavras

def tamanho_medio_palavra(texto):
    caracteres = 0
    palavras = n_palavras(texto)
    print(palavras)
    for palavra in palavras:
        caracteres += len(palavra)

    return caracteres / len(palavras)


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
    palavras = n_palavras(texto)
    total_palavras = len(palavras)
    hlr =  n_palavras_unicas(palavras) / total_palavras

    return hlr

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


def type_token(texto):
    palavras = n_palavras(texto)
    total_palavras = len(palavras)
    ttr = n_palavras_diferentes(palavras) / total_palavras
    return ttr

# MÉDIA SENTENÇA #

def media_sentenca(texto):
    sentencas = separa_sentencas(texto)
    qtd_sentencas = len(sentencas)
    qtd_caracteres = 0
    for sentenca in range(0, len(sentencas)):
        qtd_caracteres += len(sentencas[sentenca])
    
    media_sentenca = qtd_caracteres / qtd_sentencas
    return media_sentenca

# COMPLEXIADE DE SENTENÇA #

def complexidade_de_sentenca(texto):
    sentencas = separa_sentencas(texto)
    qtd_sentencas = len(sentencas)
    frases = []
    for sentenca in range(0, len(sentencas)):
        frases += separa_frases(sentencas[sentenca])

    media = len(frases) / qtd_sentencas

    return media 

# MÉDIA DE FRASE #

def media_frase(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    caracteres = 0
    qtd_frases = 0
    for sentenca in range(0, len(sentencas)):
        frases = separa_frases(sentencas[sentenca])
        qtd_frases += len(frases)
        for frase in range(0, len(frases)):
            caracteres += len(frases[frase])

    media = caracteres / qtd_frases
    return media

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similiaridades = 0
    for i in range(0, 6):
        similiaridade = as_a[i] - as_b[i]
        if similiaridade < 0:
            #converte numero negativo para positivo
            similiaridade *= -1
        similiaridades += similiaridade
    return similiaridades / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_palavra(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)  
    sal = media_sentenca(texto) 
    sac = complexidade_de_sentenca(texto) 
    pal = media_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in range(0, len(textos)):
        ass_txt = calcula_assinatura(textos[texto])
        similaridade = compara_assinatura(ass_txt, ass_cp)
        assinaturas.append(similaridade)

    txt = min(assinaturas)
    txt_certo = assinaturas.index(txt) + 1 
    return txt_certo

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    text = avalia_textos(textos, ass_cp)
    print("O autor do texto {} está infectado com COH-PIAH".format(text))

text = input("")
calcula_assinatura(text)