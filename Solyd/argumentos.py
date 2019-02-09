import sys 

argumentos = sys.argv

def soma(number1, number2):
	return number1 + number2

def sub(number1, number2):
	return number1 - number2

if argumentos[1] == "soma":
	resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)
