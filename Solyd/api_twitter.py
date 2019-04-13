import oauth2
import json
import pprint

# Autenticação com Oauth2 #

# Consumer #
consumerKey = 'iSD7OtCbkDWPJXsewfQeuBY5D'
consumerSecret = 'vYGwvqbD3nozBnA5441YyBLHW6gZpLZUEBJX9eKhcaB9qPdRXp'

# Token #
tokenKey = '1095061434847977472-1HkfpG6RAmrxSmnRoecBLaUFsB7cLW'
tokenSecret = 'ccOqI0ryloxXQ93qnkAB8YFO0p8loTpQEUAQJRhdgZctn'

# Criando o objeto 'consumer' passando 'consumerKey' e 'consumerSecret' #
consumer = oauth2.Consumer(consumerKey, consumerSecret)

# Criando o objeto 'token' passando 'tokenKey' e 'tokenSecret' #
token = oauth2.Token(tokenKey, tokenSecret)

# Criando um cliente com as keys de consumer e de token #
client = oauth2.Client(consumer, token)

# Fazendo uma requisição usando o cliente criando anteriormente #
request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=brasil&count=5')

# Decodificando a requisição de indice '1' (por ser bytes) em string #
requestDecode = request[1].decode()

# Usando a requisição decodificada para converter em json#
requestObject = json.loads(requestDecode)

# Usando a biblioteca pprint para visualizar melhor o retorno #
#pprint.pprint(requestObject)



def returnTweet(requestObject):
    for tweet in requestObject['statuses']: 
        name = tweet['user']['name']
        userName = tweet['user']['screen_name']
        text = tweet['text']
        print('\n{} - @{}\n\n{}'.format(name, userName, text))
        

returnTweet(requestObject)