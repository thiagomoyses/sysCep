#bibliotecas
import requests
import json
print("########### ATENÇAO: DIGITE APENAS NUMEROS ###########\n\n")
##testando se o usuário digitou apenas numeros
while True:
	cep = input('Informe qual o CEP -> ')
	try:
		int(cep)
		break
	except:
		print('Numero invalido!')
#transformando em String
str(cep)
#variavel que recebe a URL
url = 'https://viacep.com.br/ws/' + cep + '/json'
#Funçao para procurar CEP
def procuracep(url):
	req = requests.get(url)
	if req.status_code == 200:	
		res = req.json()
	else:
		res = None
	return res
#chamando funçao procuracep
json = procuracep(url)
#Testando informaçoes recebidas pela funçao
if json == None:
	print("CEP Invalido ou nao encontrado!")
else:
	print("################### INFORMAÇOES SOBRE O CEP ###################\n\n")
	print("# CEP: ", json['cep'])
	print("#-------------------------------------------------------------")
	print("# Logradouro: ", json['logradouro'])
	print("#-------------------------------------------------------------")
	print("# Bairro: ", json['bairro'])
	print("#-------------------------------------------------------------")
	print("# Cidade: ", json['localidade'])
	print("#-------------------------------------------------------------")
	print("# Estado: ", json['uf'])
	print("##############################################################\n\n")