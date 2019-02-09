import requests
import json

req = None
resp = True
def informations(dictionary):
    print('======= INFORMAÇÕES SOBRE O FILME =======')
    print('')
    print('Título:', dictionary['Title'])
    print('Ano:', dictionary['Year'])
    print('Lançamento:', dictionary['Released'])
    print('Direção:', dictionary['Director'])
    print('Nota(imdb):', dictionary['imdbRating'])
    print('Atores:', dictionary['Actors'])
    print('')

def requisicao(resp):   
    try:
        req = requests.get('http://www.omdbapi.com/?t='+ resp +'&apikey=360d8428')
        dictionary = json.loads(req.text)
        return dictionary
    except Exception as error:
        print('Erro detectado:', error)
        return None

def main():
    resp = True
    while resp:
        resp = input('Filme: ')
        if not resp:
            print('Obrigado por acessar e bons filmes!')
            return False
        else: 
            resp = resp.replace(' ', '+')
        dictionary = requisicao(resp)
        if dictionary['Response'] == 'True':
            informations(dictionary)
        else:
            print('Desculpe, não encontramos esse filme mas digite novamente.')

main()