import requests
import json
import pprint
import time

#Requisição
req = requests.get('https://economia.awesomeapi.com.br/all')
#Formata a saída dos dados
#Transforma o Json em um objeto python, no caso, um dict
cotacao = json.loads(req.text)


def coin(cotacao):
    while True:
        print('')
        print('=== Dólar ===')
        print('')
        print('Alta:', cotacao['USD']['high'])
        print('Baixa:', cotacao['USD']['low'])
        print('')
        print('=== Euro ===')
        print('')
        print('Alta:', cotacao['EUR']['high'])
        print('Baixa:', cotacao['EUR']['low'])
        print('')
        print('=== Bitcoin ===')
        print('')
        print('Alta:', cotacao['BTC']['high'])
        print('Baixa:', cotacao['BTC']['low'])
        time.sleep(1)

coin(cotacao)
