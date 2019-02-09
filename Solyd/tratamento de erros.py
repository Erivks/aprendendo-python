#Controlar erros (TRY e EXCEPT)
import time 
try: #Os comandos dentro do TRY serão executados e se houver erros, EXCEPT é executado.
    a = 1000 / 0
except ZeroDivisionError: #Pode - se especificar o erro ou não. Especificando o erro, 
                            #EXCEPT só executará quando aquele erro for encontrado.
    print('Não há divisão por zero.')

try:
    function() #Chamando função inexistente
except Exception as Error: #Assim, o erro será mostrado.
    print('Esse foi o erro:', Error)

def chama():
    try:
        arquivo = open('arquivo.txt')
        return arquivo
    except Exception as Error: #Assim, o erro será mostrado.
        print('Esse foi o erro:', Error)
        return False

while not chama():
    print('Tentando abrir o arquivo...')
    time.sleep(5)

print('Consegui')

