def media_sentenca(texto):
    sentencas = separa_sentencas(texto)
    qtd_sentencas = len(sentencas)
    qtd_caracteres = 0
    for sentenca in range(0, len(sentencas)):
        qtd_caracteres += len(sentencas[sentenca])
    
    media_sentenca = qtd_caracteres / qtd_sentencas
    return media_sentenca