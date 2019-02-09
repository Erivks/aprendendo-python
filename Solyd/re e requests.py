import re
import requests

#REQUESTS E RE
req = requests.get('http://lacoxinha.com.br')

email = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w\.-]+', req.text)

print(email)