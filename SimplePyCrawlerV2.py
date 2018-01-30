# MIT License

# Copyright (c) 2018 Daniel Gunna

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
reload(sys)
sys.setdefaultencoding("utf8")
#Importa bibliotecas 
import requests # biblioteca para realizar requisicoes http
from bs4 import BeautifulSoup # biblioteca para parsear html
import urllib3

#Lista de adj 
lista_adj = {}




#=========================================#
#Metodo para pegar os links  de uma url   #
#=========================================#
def getLinks(url):
	#Lista para armazenar links do documento
	links = range(0)
	if(is_valid_url(url) != None):
		#Pega resposta da url
		print "\nUrl OK"
		try:
			response = requests.get(url)
			#Armazena dados da resposta
			data  = response.text
			#Cria objeto para parsear html
			soup = BeautifulSoup(data)
			#Loop para percorrer html data buscando por resultados
			for link in soup.find_all('a'):
				# Adiciona links na lista
				links.append(link.get('href'))
			#retornar lista de links
		except requests.exceptions.MissingSchema :
			links.append("Url Invalida")
		except requests.exceptions.InvalidSchema :
			links.append("Url Invalida")
		except requests.exceptions.ConnectionError: 
			#getLinks(url)
			links.append("Url Invalida")
		except urllib3.exceptions.LocationParseError:
			links.append("Url Invalida")
	else:
		links.append("Url Invalida")
	return links

	
#========================================================================#
#Metodo principal para realizar chamada recursiva saltos vezes           #
#========================================================================#
def principal(url,saltos):
	print  "\n\n" + str( url )

	#Se numero de saltos igual a 0 quebrar recursividade
	if saltos  > 0:
		#Chama metodo getLinks para url
	     	laux = getLinks(url)
		#Remove links invalidos
		links = remove(laux)
		#aux = {}
		#lista que retorna url existentes na lista de adjacencia
		add = lista_adj.keys()
		# se url existe na lista		
		lista_adj[url] = links;
		#Percorreer lista de links da url corrente
		for i in links:
			# pegar links dda url corrente da iteracao e adiciona na lista de adjacencia na posicao url corrente
			lista_adj[i] = getLinks(i)
			# chama funcao recursivamente para cada link passando saltos - um 		
			principal(i,saltos -1)
		
	
def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)










#========================================================================#
#Metodo para remover url invalidas de uma lista de urls                  #
#========================================================================#
def remove(lista):
	for i in range(0, len(lista) - 1):
		if(type(lista[i]) == "NoneType"):		
			if (not str (lista[i].find("http")) > -1):
				print "Removendo " + lista[i]
				lista[i] = "NULL"	
	
	return lista

def printar():
	
	for i in lista_adj:
		print "\n\nLink " + str(i)
		print "\nLista de links :\n "
		print lista_adj[i]
	print "\nLista  total :"
	print lista_adj.keys()
		



url = raw_input('Entre com a  url (adicione http:// ao inicio) : ') 
salto = int(raw_input('Entre com o numero de saltos : ')) 

principal(url,salto)
printar()





























