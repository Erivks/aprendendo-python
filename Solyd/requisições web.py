import requests

requisicao = requests.get('https://solyd.com.br')

print(requisicao) #Requisição em si

print(requisicao.status_code) #Código do status: 200 - Sucesso e 404 - Falhou

print(requisicao.text) #Retorna o HTML da página requisitada

try: #É tentada a requisição da página G1 mas sem sucesso.
    requisicao = requests.get('https://g1.com.br')
except Exception as error:
    print('O erro foi:', error)

try: #É tirada a letra 's' do link a ser requisitado
    requisicao = requests.get('http://g1.com.br')
    print(requisicao.text)
except Exception as error:
    print('O erro foi:', error)

cabecalho = {'User-agent': 'Windows 12'}

try: 
    requisicao = requests.post('https://putsreq.com/wERMkV3HJbiaARZvk9f6',
headers=cabecalho)
    print(requisicao.text)
except Exception as error:
    print('O erro foi:', error)
