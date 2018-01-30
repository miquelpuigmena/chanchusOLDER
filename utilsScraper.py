import csv
import time
from random import randint

#Definir colors per Print
class bcolors:
    VERMELL = '\033[91m'
    BLAU = '\033[94m'
    VERD = '\033[92m'
    TURQUESA = '\033[96m'
    ENDC = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRATLLAT = '\033[4m'


#Torna totes les mayus de la frase
def getUppers(frase):
	uppers = ""
	for paraula in frase:
		for lletra in paraula:
			if lletra.isupper():
				uppers += lletra
	return uppers
def ferUppers(primer, segon):
	paraulesseparades = primer.split()
	upper1=[]
	upper2=[]
	for p in paraulesseparades:
		for lletres in p:
			if lletres.isupper():
				upper1.append(lletres)
				break
	paraulesseparades = segon.split()
	for s in paraulesseparades:
		for lletres in s:
			if lletres.isupper():
				upper2.append(lletres)
				break
	return upper1, upper2

# Canvi de signe puntuacio: ','-->'.'
# Utilitzat per: Interwetten
def replaceChar(word, previouschar, finalchar):
	for letter in word:
		if letter == previouschar:
			word = word.replace(letter, finalchar)
			return word
	return word

# Agafa el nom fins primer parentesis --> '('
# Utilitzat per: WilliamHill, Betfair
def getTeamName(string, char):
	stringnou = ""
	acces=False
	for s in string:
		if s != "\n":
			if (s == char):
				return stringnou
			stringnou += s
	return stringnou
#Retorna data dia Avui
#Utilitzat a gethtml de MarcaApuestas
def getFecha():
	return time.strftime("%Y-%m-%d")

#Esborra Simbols al principi d'un nom
# Utilitzat per: Betfair
def eraseSimbolsPrincipi(nom):
	acces = False
	nomret = ""
	for paraules in nom.split():
		if paraules[0].isalpha():
			acces = True
		if acces:
			nomret += paraules+" "
	return nomret

#Separa nombre segun caracter
# Utilitzat per: Suertia
def separarEquipos(nombre, caracter):
    equip = nombre.split(caracter)
    return equip

#veure si es ascii
#
def is_ascii(char):
	return ord(char) < 128

#Asegurar error encode UTF-8
#Utilitzat a: writer.py
def asciiError(frase):
	fraseaux=""
	for letra in frase:
		if is_ascii(letra):
			fraseaux += letra.encode('utf-8', 'ignore')
	return fraseaux

#Comprobar si es dobles un equip i reotrna els jugadors x separat
#Utilitzat a: tennisScraper
def comprobarDoblesTennis(frase, char):
	persona1=""
	persona2=""
	acces = True
	for lletra in frase:
		if lletra == char:
			acces = False
		else:
			if acces:
				persona1 += lletra
			else:
				persona2 += lletra
	return persona1, persona2
	
#Retorna el format correcte de una parella de jugadors
def checkNomsTennisDobles(nom):
	equipcombinat = comprobarDoblesTennis(nom, '/')
	if equipcombinat[1] != "":
		nomretorn = equipcombinat[0] + " & " + equipcombinat[1]
	else:
		nomretorn = equipcombinat[0]
	return nomretorn


#Retorn random number entre els limits
#Utilitzat per fer el get page de GoldenPark
def getRandomNumber(limitA, limitB):
	return randint(limitA,limitB)

#Print error
def printError(error):
	print bcolors.VERMELL +error+ bcolors.ENDC

def printNegrita(dataevento):
	print bcolors.NEGRITA + str(dataevento)+ bcolors.ENDC
def printVerd(dataevento):
	for data in dataevento:
		if data != dataevento[-1]:
			print bcolors.VERD + str(data)+ bcolors.ENDC,
		else:
			print bcolors.VERD + str(data)+ bcolors.ENDC
def printNumeracio(numero):
	print bcolors.NEGRITA + bcolors.BLAU + str(numero)+". "+ bcolors.ENDC,

def printVerdNegrita(dataevento):
	for data in dataevento:
		if data != dataevento[-1]:
			print bcolors.NEGRITA + bcolors.VERD + str(data)+ bcolors.ENDC,
		else:
			print bcolors.NEGRITA + bcolors.VERD + str(data)+ bcolors.ENDC
def printVermellNegrita(dataevento):
	for data in dataevento:
		if data != dataevento[-1]:
			print bcolors.NEGRITA + bcolors.VERMELL + str(data)+ bcolors.ENDC,
		else:
			print bcolors.NEGRITA + bcolors.VERMELL + str(data)+ bcolors.ENDC
#Borra espacios del final de la palabra
def eraseSpaces(nom):
	nomnospaces = eraseSimbolsPrincipi(nom)
	nomgirat = nomnospaces[::-1]
	acces = False
	lletresbones=""
	for lletra in nomgirat:
		if lletra != " ":
			acces = True
		if acces:
			lletresbones += lletra
	return lletresbones[::-1]



