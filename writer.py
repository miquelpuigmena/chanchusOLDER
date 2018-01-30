import csv
from utilsScraper import ferUppers, asciiError, replaceChar, eraseSpaces, printNegrita
import datetime

w12o = open("csvdocs/data.csv", 'w')
writer = csv.writer(w12o)
writer.writerow(('sport','casa de apostes','equipo1', 'cuota1', 'equipo2', 'cuota2', 'uppers1', 'uppers2', 'lliga'))
w1x2o = open("csvdocs/data1x2.csv", 'w')
writer1x2 = csv.writer(w1x2o)
writer1x2.writerow(('sport','casa de apostes','equipo1', 'equipo2', 'cuota1', 'cuotaX','cuota2', 'lliga'))
notrobats=[]
notrobatlligues=[]

########fer funcio per preguntar els no trobats per ficar en el cache. Ja troba els no trobats i els classifica com toca
def closecsv1x2():
	w1x2o.close()
def closecsv12():
	w12o.close()
def checkRowisnotinVector(vector, row):
	for linia in vector:
		if linia == row:
			return False
	return True
def writerCSV1x2(esport, casa, equip1, equip2, cuota1, cuotaX, cuota2, lliga):
	#print getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))), getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))), getMatchingLeague1x2(eraseSpaces(replaceChar(asciiError(lliga), ',', '')))
	if (getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))) != 0)and(getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))) != 0)and(getMatchingLeague1x2(eraseSpaces(asciiError(lliga))) != 0):
		writer1x2.writerow((esport, casa, getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))), getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))), round(float(cuota1), 2), round(float(cuotaX), 2),  round(float(cuota2), 2), getMatchingLeague1x2(eraseSpaces(asciiError(lliga)))))
	else:
		if getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(equip1), 'equip']
			if checkRowisnotinVector(notrobats, missing):
				notrobats.append(missing)
		if getMatchingEquip1x2(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(equip2), 'equip']
			if checkRowisnotinVector(notrobats, missing):
				notrobats.append(missing)
		if getMatchingLeague1x2(eraseSpaces(replaceChar(asciiError(lliga), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(lliga), 'lliga']
			if checkRowisnotinVector(notrobatlligues, missing):
				notrobatlligues.append(missing)
def writerCSVBaseball(esport, casa, equip1, cuota1, equip2, cuota2, lliga):
	if (getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))) != 0)and(getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))) != 0)and(getMatchingLeagueBaseball(eraseSpaces(asciiError(lliga))) != 0):
		u1, u2 = ferUppers(equip1, equip2)		
		writer.writerow((esport, casa, getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))), round(float(cuota1), 2), getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))), round(float(cuota2), 2), u1, u2, getMatchingLeagueBaseball(eraseSpaces(asciiError(lliga)))))
	else:
		if getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip1), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(equip1), 'equip']
			if checkRowisnotinVector(notrobats, missing):
				notrobats.append(missing)
		if getMatchingEquipBaseball(eraseSpaces(replaceChar(asciiError(equip2), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(equip2), 'equip']
			if checkRowisnotinVector(notrobats, missing):
				notrobats.append(missing)
		if getMatchingLeagueBaseball(eraseSpaces(replaceChar(asciiError(lliga), ',', ''))) == 0 :
			missing = [casa, esport, asciiError(lliga), 'lliga']
			if checkRowisnotinVector(notrobatlligues, missing):
				notrobatlligues.append(missing)
def ferbackup():
	overwriteCSV("csvdocs/cacheEquipsBaseball.csv", "csvdocs/backup/datacacheEquipsBaseballbackup.csv")
	overwriteCSV("csvdocs/cacheLliguesBaseball.csv", "csvdocs/backup/datacacheLliguesBaseballbackup.csv")
	ferbackupbackup()

def ferbackupbackup():
	if datetime.datetime.today().weekday()%2 == 0:
		overwriteCSV("csvdocs/backup/datacacheEquipsBaseballbackup.csv", "csvdocs/backup/backupbackup/datacacheEquipsBaseballbackup.csv")
		overwriteCSV("csvdocs/backup/datacacheLliguesBaseballbackup.csv", "csvdocs/backup/backupbackup/datacacheLliguesBaseballbackup.csv")


def actualitzarAuxiliar(row, toappend, path):
	ra = open(path, 'r')
	readeractualitzar = csv.reader(ra)
	wa = open("csvdocs/auxiliar.csv", 'w')
	writeractualitzar = csv.writer(wa)	
	if row != None:
		for rowcache in readeractualitzar:
			acces = True
			auxrow=[]
			if rowcache == row and acces:
				for r in row:
					if r == '':
						break
					auxrow.append(r)
				if toappend != None:
					auxrow.append(asciiError(toappend))
				writeractualitzar.writerow(auxrow)
				acces = False
			else:
				writeractualitzar.writerow(rowcache)
	else:
		for rowcache in readeractualitzar:
			writeractualitzar.writerow(rowcache)
		writeractualitzar.writerow([toappend])
	ra.close()
	wa.close()
	overwriteCSV("csvdocs/auxiliar.csv", path)


def overwriteCSV(pathcsvoriginal, pathcsvcopia):
	ro = open(pathcsvoriginal, 'r')
	readerover = csv.reader(ro)
	wo = open(pathcsvcopia, 'w')
	writerover = csv.writer(wo)

	for row in readerover:
		writerover.writerow(row)
	ro.close()
	wo.close()	

def compareParaulesIguals(para1, para2):	
	for paraula1 in para1:
		for paraula2 in para2:
			if paraula2 == paraula1:
				para2.remove(paraula2)
				break
	return para2

def checkParaulaInRow(row, paraula):
	for words in row:
		if words.lower()==paraula.lower():
			return True
	return False

def checkFraseInRow(row, frase):
	paraules = frase.split()
	paraulestrobades = []
	for frases in row:
		for paraula in paraules:
			if checkParaulaInRow(frases.split(), paraula):
				acces = True
				for words in paraulestrobades:
					if words.lower() == paraula.lower():
						acces=False
				if acces:
					paraulestrobades.append(paraula)

	for paraula in paraulestrobades:
		paraules.remove(paraula)
	return paraules

def idemParaules(nomRebut, paraulesrestants):
	comp1 = compareParaulesIguals(paraulesrestants, nomRebut.split())
	if comp1 != []:
		return False
	comp2 = compareParaulesIguals(nomRebut.split(), paraulesrestants)
	if comp2 == []:
		return True
	return False

###Utilitzat a checkPhraseinCsv
###Comprovar que el 65% de les lletres d'una paraula estan en una linia
def checkWordinRowbyPercentage(row, word1):
	betamax = 0
	for casilla in row:
		for palabra in casilla.split():
			word11=[]
			word22=[]
			for letra in palabra:
				word11.append(letra)
			for letra in word1:
				word22.append(letra)
			contador = 0
			for letter in word11:
				for lletra in word22:
					if lletra == letter:
						word22.remove(lletra)
						contador += 2
						break
			sizepalabras= len(palabra)+len(word1)
			beta = float(contador)/float(sizepalabras)
			if beta > betamax:
				betamax= beta
	return betamax	
							
					
### Comprueba que una frase este en el cache Basebal:
	#1. Todo el nombre igual en alguna linea del cache; devuelve la clave de aquella linea
	#2. Si ninguna palabra coincide, pregunto por nueva linea
	#3. Compruebo coincidencia d letras de palabras restantes

def checkPhraseinCsv(frase, path, tipo):
	rc = open(path, 'r')
	readerChecker = csv.reader(rc)
	for row in readerChecker:
		for paraula in row:
			paraulesrestants = checkFraseInRow(row, frase)
			paraulesesborrar=[]
			for paraularestant in paraulesrestants:
				esborrar = True
				paraulesesborrar=[]
				for lletra in paraularestant:
					if lletra.islower():
						esborrar = False
						break
				if frase != paraularestant:
					if esborrar or paraularestant == 'fc':
						paraulesesborrar.append(paraularestant)
			for paraulaesborrar in paraulesesborrar:
				try:
					paraulesrestants.remove(paraulaesborrar)
				except:
					pass
				
			if (paraula.lower() == frase.lower())or(paraulesrestants == []):
				rc.close()
				return row, None #La paraula clau per aquella lliga nom
			elif (idemParaules(frase, paraulesrestants)):###Trec comparacio si la paraula es de longitud 1
				break
	rc.close()
	return 0

def resoldreMissing(notrobat, path):
	rc2 = open(path, 'r')
	readerChecker2 = csv.reader(rc2)
	for row in readerChecker2:
		acces = True
		paraulesrestants = checkFraseInRow(row, asciiError(notrobat[2]))
		for paraularestant in paraulesrestants:
			if checkWordinRowbyPercentage(row, paraularestant) < 0.85:
				acces = False
				break	
		if acces:
			print notrobat[1].upper()+" > "+notrobat[0].upper()+": ",
			response = raw_input("Quiere guardar ["+asciiError(notrobat[2])+"] en la linea ["+row[0]+"]? ['no' para cancelar] ")
			if response != 'no':
				rc2.close()
				return row, asciiError(notrobat[2])
			else:
				pass
	while True:
		print notrobat[1].upper()+" > "+notrobat[0].upper()+": ",
		notrobatres = raw_input("No hay coincidencias en el cache. Donde quiere guardar ["+asciiError(notrobat[2])+"]? ['cancelar' para no guardar]  ")

		if notrobatres == '':
			return None, notrobat
		if notrobatres != 'cancelar':
			rcinWhile = open(path, 'r')
			readerCheckinWhile = csv.reader(rcinWhile)

			for row in readerCheckinWhile:
				for paraula in row:
					paraulesrestants = checkFraseInRow(row, notrobatres)
					if (paraulesrestants == []):
						rcinWhile.close()
						return row, notrobat[2] #La paraula clau per aquella lliga nom
		else:
			print notrobat[1].upper()+" > "+notrobat[0].upper()+": ",
			print "["+notrobat[2]+"] No guardado"
			return 0
		resp = raw_input("Crear nueva linea para ["+notrobatres+"]? ['INTRO' para escribir] ")
		if resp == '':
				return None, notrobatres

def omplirCache():
	contador = 0
	printNegrita("INFORMACION")
	printNegrita ("=========================================================")
	print str(len(notrobats))+" equipos no se han encontrado "
	print str(len(notrobatlligues))+" ligas no se han encontrado "
	print "=========================================================\n"
	printNegrita("Lista Comandos:")
	response = raw_input("    <pass> para saltar llenar cache \n    <intro> para llenar cache de equipos y ligas \n    <liga> o <equipo> para escojer uno\n  >> ")
	notrobattotal = []
	if response == '':
		notrobattotal = notrobatlligues+notrobats
	for resposta in response.split():
		if resposta == 'liga':
			notrobattotal += notrobatlligues
		elif resposta == 'equipo':
			notrobattotal += notrobats
		elif resposta != 'pass':
			notrobattotal = notrobatlligues + notrobats
		else:
			return

	for notrobat in notrobattotal:
		if notrobat[1] == 'Futbol':
			if notrobat[3] == 'lliga':
				call = resoldreMissing(notrobat, "csvdocs/cacheLliguesFutbol.csv")
				if call == 0:
					pass
				elif call[0] == None:
					if len(call[1][2]) > 1:
						actualitzarAuxiliar(None, call[1][2], "csvdocs/cacheLliguesFutbol.csv") #Nova linia
					else:
						actualitzarAuxiliar(None, call[1], "csvdocs/cacheLliguesFutbol.csv") #Nova linia entrada per pantalla	
				else:
					actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheLliguesFutbol.csv") 
			else:
				call = resoldreMissing(notrobat, "csvdocs/cacheEquipsFutbol.csv")
				if call == 0:
					pass
				elif call[0] == None:
					if len(call[1][2]) > 1:
						actualitzarAuxiliar(None, call[1][2], "csvdocs/cacheEquipsFutbol.csv") #Nova linia
					else:
						actualitzarAuxiliar(None, call[1], "csvdocs/cacheEquipsFutbol.csv") #Nova linia entrada per pantalla
				else:
					actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheEquipsFutbol.csv") 
		elif notrobat[1] == 'Baseball':
			if notrobat[3] == 'lliga':
				call = resoldreMissing(notrobat, "csvdocs/cacheLliguesBaseball.csv")
				if call == 0:
					pass
				elif call[0] == None:
					if len(call[1][2]) > 1:
						actualitzarAuxiliar(None, call[1][2], "csvdocs/cacheLliguesBaseball.csv") #Nova linia
					else:
						actualitzarAuxiliar(None, call[1], "csvdocs/cacheLliguesBaseball.csv") #Nova linia entrada per pantalla
				else:
					actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheLliguesBaseball.csv") 
			else:
				call = resoldreMissing(notrobat, "csvdocs/cacheEquipsBaseball.csv")
				if call == 0:
					pass
				elif call[0] == None:
					if len(call[1][2]) > 1:
						actualitzarAuxiliar(None, call[1][2], "csvdocs/cacheEquipsBaseball.csv") #Nova linia
					else:
						actualitzarAuxiliar(None, call[1], "csvdocs/cacheEquipsBaseball.csv") #Nova linia entrada per pantalla
				else:
					actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheEquipsBaseball.csv") 

def getMatchingEquip1x2(nomRebut):
	call = checkPhraseinCsv(nomRebut, "csvdocs/cacheEquipsFutbol.csv", 'FUTBOL EQUIPS>')
	if call == 0:
		return 0
	elif call[1] == None:
		return call[0][0] #Trobat
	else:
		actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheEquipsFutbol.csv")
		return call[0][0] #Trobat per percentatge
def getMatchingLeague1x2(nomRebut):
	call = checkPhraseinCsv(nomRebut, "csvdocs/cacheLliguesFutbol.csv", 'LLIGA FUTBOL>')
	if call == 0:
		return 0
	elif call[1] == None:
		return call[0][0] #Trobat
	else:
		actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheLliguesFutbol.csv")
		return call[0][0] #Trobat per percentatge	

def getMatchingEquipBaseball(nomRebut):
	call = checkPhraseinCsv(nomRebut, "csvdocs/cacheEquipsBaseball.csv", 'BASEBALL EQUIPS>')
	if call == 0:
		return 0
	elif call[1] == None:
		return call[0][0] #Trobat
	else:
		actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheEquipsBaseball.csv")
		return call[0][0] #Trobat per percentatge
	

def getMatchingLeagueBaseball(nomRebut):
	call = checkPhraseinCsv(nomRebut, "csvdocs/cacheLliguesBaseball.csv", 'LLIGA BASEBALL>')
	if call == 0:
		return 0
	elif call[1] == None:
		return call[0][0] #Trobat
	else:
		actualitzarAuxiliar(call[0], call[1], "csvdocs/cacheLliguesBaseball.csv")
		return call[0][0] #Trobat per percentatge

