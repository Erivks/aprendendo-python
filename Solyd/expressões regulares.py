import re #expressões regulares

s_teste = 'O gato é bonito'

#Busca a palavra 'gata' dentro da string especificada que é 's_teste'
padrao = re.search(r'gata', s_teste) #RAW string (transforma caracteres especiais em não especiais)

if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

#Não querendo especificar um caractere, basta pôr um ponto final '.' em seu lugar.
padrao = re.search(r'g.to', s_teste)

print(padrao.group())


s_teste = 'gato, gata, gatinho, gatoes'
#findall retorna uma lista com todos os padrões encontrados e o caractere '+' informa a função
#que deve retornar a palavra inteira 
padrao = re.findall(r'gat\w+', s_teste)

print(padrao)

#especificando grupo de caracteres
padrao = re.findall(r'[gat]+', s_teste)

print(padrao)

#especificando quantidade de letras
padrao = re.findall(r'\w{4}', s_teste)
print(padrao)


#DETECTOR DE E-MAILS
print('')
print('===== DETECTOR DE E-MAILS =====')
print('')
e_mails = ['eri_ck@ahskajh.com', 'skdakdnalk', 'snal-snalk@dmnsdn.com.br', 'kdjaklakj']
for email in e_mails:
    try:
        padrao = re.search(r'[\w-]+@[\w-]+\.[\w\.-]+', email)
        print(padrao.group())
    except Exception as error:
        print('Fora do padrão.\nErro encontrado:', error)