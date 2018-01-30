import csv
import re
import numbers
from operator import itemgetter
from filtres import *
from utilsScraper import printError, printVerdNegrita, printVerd, printVermellNegrita, printNumeracio

CONST_LLINDAR = 0.98
llista_de_cases_operatives=[['sportium','sp'],['bwin','bw'],['interwetten','in'],['william hill', 'wh'],['tipbet', 'tb'],['betfair','bf'],['marca apuestas','ma'],['suertia','su'],['kirolbet','kb'],['codere','ce'],['betstars', 'bs'],['juegging','jg'],['Mbet','mb'],['paf','pf'],['wanabet','wb'],['golden park', 'gp']]
sportiumstuff=[]
bwinstuff=[]
interwettenstuff=[]
williamstuff=[]
tipbetstuff=[]
betfairstuff=[]
marcastuff=[]
suertiastuff=[]
kirolbetstuff=[]
coderestuff=[]
betstarsstuff=[]
jueggingstuff=[]
marathonbetstuff=[]
pafstuff=[]
wanabetstuff=[]
goldenparkstuff=[]
bet365stuff=[]
#1x2
sportiumstuff1x2=[]
bwinstuff1x2=[]
interwettenstuff1x2=[]
williamstuff1x2=[]
tipbetstuff1x2=[]
betfairstuff1x2=[]
marcastuff1x2=[]
suertiastuff1x2=[]
kirolbetstuff1x2=[]
coderestuff1x2=[]
betstarsstuff1x2=[]
jueggingstuff1x2=[]
marathonbetstuff1x2=[]
pafstuff1x2=[]
wanabetstuff1x2=[]
goldenparkstuff1x2=[]
bet365stuff1x2=[]

#definnir Alpha 
def definirAlpha(q, w):
	alpha = ((float(q)*float(w))/(float(q)+float(w)))
	return round(alpha, 4)
def definirAlpha1x2(uno,x,dos):
	alpha = ((float(uno)*float(x)*float(dos))/((float(uno)*float(x))+(float(uno)*float(dos))+(float(x)*float(dos))))
	return round(alpha, 4)

#retornar possibles alphas amb dugues cases

def treureAlphas(a1,b1,a2,b2):

	alpha1 = definirAlpha(a1,b2)

	alpha2 = definirAlpha(b1,a2)

	return alpha1, alpha2	
def treureAlphas1x2(a1,ax,a2,b1,bx,b2):

	#alpha1 = definirAlpha1x2(a1,ax,a2)
	alpha2 = definirAlpha1x2(a1,ax,b2)
	alpha3 = definirAlpha1x2(a1,bx,a2)
	alpha4 = definirAlpha1x2(a1,bx,b2)
	alpha5 = definirAlpha1x2(b1,ax,a2)
	alpha6 = definirAlpha1x2(b1,ax,b2)
	alpha7 = definirAlpha1x2(b1,bx,a2)
	#alpha8 = definirAlpha1x2(b1,bx,b2)
	return  alpha2,alpha3,alpha4,alpha5,alpha6,alpha7
#completa arrays agafant del csv

def completarArrays():

	csvFiletoRead = open("csvdocs/data.csv", 'r')
	reader = csv.DictReader(csvFiletoRead)
	for r in reader:
		if r["casa de apostes"] == 'Sportium':
			sportiumstuff.append(r)
		elif r["casa de apostes"] == 'Bwin':
			bwinstuff.append(r)
		elif r["casa de apostes"] == 'Interwetten':
			interwettenstuff.append(r)
		elif r["casa de apostes"] == 'William Hill':
			williamstuff.append(r)
		elif r["casa de apostes"] == 'Tipbet':
			tipbetstuff.append(r)
		elif r["casa de apostes"] == 'Betfair':
			betfairstuff.append(r)
		elif r["casa de apostes"] == 'Marca apuestas':
			marcastuff.append(r)
		elif r["casa de apostes"] == 'Suertia':
			suertiastuff.append(r)
		elif r["casa de apostes"] == 'Kirolbet':
			kirolbetstuff.append(r)
		elif r["casa de apostes"] == 'Codere':
			coderestuff.append(r)
		elif r["casa de apostes"] == 'Betstars':
			betstarsstuff.append(r)
		elif r["casa de apostes"] == 'Juegging':
			jueggingstuff.append(r)
		elif r["casa de apostes"] == 'Marathonbet':
			marathonbetstuff.append(r)
		elif r["casa de apostes"] == 'Paf':
			pafstuff.append(r)
		elif r["casa de apostes"] == 'Wanabet':
			wanabetstuff.append(r)
		elif r["casa de apostes"] == 'Goldenpark':
			goldenparkstuff.append(r)
		elif r["casa de apostes"] == 'Bet365':
			bet365stuff.append(r)
		else:
			print "casa no encontrada"
	csvFiletoRead.close()
def completarArrays1x2():

	csvFiletoRead = open("csvdocs/data1x2.csv", 'r')
	reader = csv.DictReader(csvFiletoRead)
	for r in reader:
		if r["casa de apostes"] == 'Sportium':
			sportiumstuff1x2.append(r)
		elif r["casa de apostes"] == 'Bwin':
			bwinstuff1x2.append(r)
		elif r["casa de apostes"] == 'Interwetten':
			interwettenstuff1x2.append(r)
		elif r["casa de apostes"] == 'William Hill':
			williamstuff1x2.append(r)
		elif r["casa de apostes"] == 'Tipbet':
			tipbetstuff1x2.append(r)
		elif r["casa de apostes"] == 'Betfair':
			betfairstuff1x2.append(r)
		elif r["casa de apostes"] == 'Marca apuestas':
			marcastuff1x2.append(r)
		elif r["casa de apostes"] == 'Suertia':
			suertiastuff1x2.append(r)
		elif r["casa de apostes"] == 'Kirolbet':
			kirolbetstuff1x2.append(r)
		elif r["casa de apostes"] == 'Codere':
			coderestuff1x2.append(r)
		elif r["casa de apostes"] == 'Betstars':
			betstarsstuff1x2.append(r)
		elif r["casa de apostes"] == 'Juegging':
			jueggingstuff1x2.append(r)
		elif r["casa de apostes"] == 'Marathonbet':
			marathonbetstuff1x2.append(r)
		elif r["casa de apostes"] == 'Paf':
			pafstuff1x2.append(r)
		elif r["casa de apostes"] == 'Wanabet':
			wanabetstuff1x2.append(r)
		elif r["casa de apostes"] == 'Goldenpark':
			goldenparkstuff1x2.append(r)
		elif r["casa de apostes"] == 'Bet365':
			bet365stuff1x2.append(r)
		else:
			print "casa no encontrada"
	csvFiletoRead.close()

#agafa els stuffs excepte el passat per parametre
def getStuffArray(casesbuscades):
	cases = []
	if casesbuscades ==  []: ##Totes les cases
		cases.append(sportiumstuff)
		cases.append(bwinstuff)
		cases.append(interwettenstuff)
		cases.append(williamstuff)
		cases.append(tipbetstuff)
		cases.append(betfairstuff)
		cases.append(marcastuff)
		cases.append(suertiastuff)
		cases.append(kirolbetstuff)
		cases.append(coderestuff)
		cases.append(betstarsstuff)
		cases.append(jueggingstuff)
		cases.append(marathonbetstuff)
		cases.append(pafstuff)
		cases.append(wanabetstuff)
		cases.append(goldenparkstuff)
		cases.append(bet365stuff)
	else:
		for casa in casesbuscades: ##Cases buscades
			if casa == 'sportium':
				cases.append(sportiumstuff)
			elif casa == 'bwin':
				cases.append(bwinstuff)
			elif casa == 'interwetten':
				cases.append(interwettenstuff)
			elif casa == 'william hill':
				cases.append(williamstuff)
			elif casa == 'tipbet':
				cases.append(tipbetstuff)
			elif casa == 'betfair':
				cases.append(betfairstuff)
			elif casa == 'marca apuestas':
				cases.append(marcastuff)
			elif casa == 'suertia':
				cases.append(suertiastuff)
			elif casa == 'kirolbet':
				cases.append(kirolbetstuff)
			elif casa == 'codere':
				cases.append(coderestuff)
			elif casa == 'bet stars':
				cases.append(betstarsstuff)
			elif casa == 'juegging':
				cases.append(jueggingstuff)
			elif casa == 'marathon bet':
				cases.append(marathonbetstuff)
			elif casa == 'paf':
				cases.append(pafstuff)
			elif casa == 'wanabet':
				cases.append(wanabetstuff)
			elif casa == 'golden park':
				cases.append(goldenparkstuff)
			elif casa == 'bet365':
				cases.append(bet365stuff)
	return cases
def getStuffArray1x2(casesbuscades):
	cases1x2 = []
	if casesbuscades ==  []: ##Totes les cases
		cases1x2.append(sportiumstuff1x2)
		cases1x2.append(bwinstuff1x2)
		cases1x2.append(interwettenstuff1x2)
		cases1x2.append(williamstuff1x2)
		cases1x2.append(tipbetstuff1x2)
		cases1x2.append(betfairstuff1x2)
		cases1x2.append(marcastuff1x2)
		cases1x2.append(suertiastuff1x2)
		cases1x2.append(kirolbetstuff1x2)
		cases1x2.append(coderestuff1x2)
		cases1x2.append(betstarsstuff1x2)
		cases1x2.append(jueggingstuff1x2)
		cases1x2.append(marathonbetstuff1x2)
		cases1x2.append(pafstuff1x2)
		cases1x2.append(wanabetstuff1x2)
		cases1x2.append(goldenparkstuff1x2)
		cases1x2.append(bet365stuff1x2)
	else:
		for casa in casesbuscades: ##Cases buscades
			if casa == 'sportium':
				cases1x2.append(sportiumstuff1x2)
			elif casa == 'bwin':
				cases1x2.append(bwinstuff1x2)
			elif casa == 'interwetten':
				cases1x2.append(interwettenstuff1x2)
			elif casa == 'william hill':
				cases1x2.append(williamstuff1x2)
			elif casa == 'tipbet':
				cases1x2.append(tipbetstuff1x2)
			elif casa == 'betfair':
				cases1x2.append(betfairstuff1x2)
			elif casa == 'marca apuestas':
				cases1x2.append(marcastuff1x2)
			elif casa == 'suertia':
				cases1x2.append(suertiastuff1x2)
			elif casa == 'kirolbet':
				cases1x2.append(kirolbetstuff1x2)
			elif casa == 'codere':
				cases1x2.append(coderestuff1x2)
			elif casa == 'bet stars':
				cases1x2.append(betstarsstuff1x2)
			elif casa == 'juegging':
				cases1x2.append(jueggingstuff1x2)
			elif casa == 'marathon bet':
				cases1x2.append(marathonbetstuff1x2)
			elif casa == 'paf':
				cases1x2.append(pafstuff1x2)
			elif casa == 'wanabet':
				cases1x2.append(wanabetstuff1x2)
			elif casa == 'golden park':
				cases1x2.append(goldenparkstuff1x2)
			elif casa == 'bet365':
				cases1x2.append(bet365stuff1x2)
	return cases1x2

def preguntar():
	casesbuscades = []
	contador = 0
	for casesoperatives in llista_de_cases_operatives:
		contador += 1
		print "[",
		longi = 0
		for element in casesoperatives:
			longi += len(element)
			print element,
		if longi > 12:
			print "]\t",
		else:
			print "]\t\t",
		if contador%4 == 0:
			print
	print "==========================================================================================\n"
	print " >>",
	resp = raw_input("Que casas quiere buscar? [Intro para buscar todas]: ")
	resposta = resp.split()
	for casa in resposta:
		for casesoperatives in llista_de_cases_operatives:
			if (casesoperatives[0]==casa)or(casesoperatives[1]==casa):
				casesbuscades.append(casesoperatives[0])
	if casesbuscades != []:
		print "Buscant a ",
		print casesbuscades
	else:
		print "Buscant a TOTES ..."
	return casesbuscades

def checkTennis():
	print
	print "=========================================================================================="
	print "Checking Tennis..."
	print "=========================================================================================="
	tennismatches=[]
	for casa in getStuffArray([]):
		for evento in casa:
			if evento['sport'] == 'Tennis':
				tennismatches.append(evento)
	alpha = guardarAlphes(checkForPairsinList(tennismatches))
	printAlphesColor(alphessobrellindar)
def checkBaseball():
	print
	print "=========================================================================================="
	print "Checking Baseball..."
	print "=========================================================================================="
	
	casesbuscar = preguntar()
	
	baseballmatches=[]
	for casa in getStuffArray(casesbuscar):
		baseballmatchesauxiliar=[]
		for evento in casa:
			if evento['sport'] == 'Baseball':
				baseballmatchesauxiliar.append(evento)
		baseballmatches.append(baseballmatchesauxiliar)
	alphessobrellindar = guardarAlphes(checkForPairs(baseballmatches))
	printAlphesColor(sortbyfirstcolumn(alphessobrellindar))
def checkFootball():
	print
	print "=========================================================================================="
	print "Checking Football..."
	print "=========================================================================================="
	
	casesbuscar = preguntar()
	
	footballmatches=[]
	for casa in getStuffArray1x2(casesbuscar):
		footballmatchesauxiliar=[]
		for evento in casa:
			if evento['sport']=='Futbol':      #realmente ahora es todo futbol y esta linia no haria falta ahora
				footballmatchesauxiliar.append(evento)
		footballmatches.append(footballmatchesauxiliar)
	alphessobrellindar = guardarAlphes1x2(checkForPairs(footballmatches))
	printAlphesColor(sortbyfirstcolumn(alphessobrellindar))

def sortbyfirstcolumn(lista):
	listaordenada = []
	for element in lista:
		acces = True
		if listaordenada != []:
			conta = 0
			for ele in listaordenada:
				if float(element[0])>=float(ele[0]):
					acces = False
					listaordenada.insert(conta, element)
					break
				conta += 1
		else:
			acces = False
			listaordenada.append(element)
		if acces:
			listaordenada.append(element)
	return listaordenada

def girarVectorcreuat(b):
	try:
		organitzarvector = {}
		organitzarvector['equipo1']=b['equipo2']
		organitzarvector['equipo2']=b['equipo1']
		organitzarvector['casa de apostes']=b['casa de apostes']
		organitzarvector['cuotaX']=b['cuotaX']
		organitzarvector['lliga']=b['lliga']
		organitzarvector['sport']=b['sport']
		organitzarvector['cuota2']=b['cuota1']
		organitzarvector['cuota1']=b['cuota2']
	except:
		return 0
	return organitzarvector
	

##no eficient
def checkifelementisinvv(vv, element):
	for v in vv:
		for ele in v:
			if ele == element:
				return False
	return True
def checkForPairs(vV):
	vVaux = vV
	llistaparelles = []
	for v in vV:
		for element in v:
			llistaparellesaux = []
			for vaux in vVaux:
				acces = True
				for elementaux in vaux:
					if acces:
						if (element['equipo1'] == elementaux['equipo1'])and(element['equipo2'] == elementaux['equipo2']):
							if checkifelementisinvv(llistaparelles, elementaux):
								llistaparellesaux.append(elementaux)
								acces = False
						elif (element['equipo1'] == elementaux['equipo2'])and(element['equipo2'] == elementaux['equipo1']):
							if checkifelementisinvv(llistaparelles, girarVectorcreuat(elementaux)):
								appe = girarVectorcreuat(elementaux)
								if appe == 0:
									break
								llistaparellesaux.append(appe)
								acces = False
			if llistaparellesaux != []:
				llistaparelles.append(llistaparellesaux)
	return llistaparelles
def checkForPairsinList(vectorVectores):
	c = 0
	arrayauxvv = vectorVectores
	llistaparelles = []
	contador = 0
	for array in vectorVectores:
		for a in array:
			aux = []	
			try:
				
				arrayauxvv[contador].remove(a)
				printError("=============================")
				aux.append(a)
				#if ((isinstance(float(a["cuota1"]), float))and(isinstance(float(a["cuota2"]), float))):
				for arrayaux in arrayauxvv:
					acces = True
					for b in arrayaux:
						if acces:
							#if ((isinstance(float(b["cuota1"]), numbers.Real))and(isinstance(float(b["cuota2"]), numbers.Real))): 
							if a['lliga'] == b['lliga']:
								if (a['equipo1'] == b['equipo1'])and(a['equipo2'] == b['equipo2'])and(a['casa de apostes'] != b['casa de apostes']):
									aux.append(b)
									#arrayaux.remove(b)
									acces = False
								elif (a['equipo1'] == b['equipo2'])and(a['equipo2'] == b['equipo1'])and(a['casa de apostes'] != b['casa de apostes']):
									aux.append(girarVectorcreuat(b))
									acces = False
				for partit in aux:
					if partit != aux[0]:
						try:
							arrayaux.remove(partit)	
						except:
							arrayaux.remove(girarVectorcreuat(partit))
				llistaparelles.append(aux)
			except:
				pass
		contador += 1
	return llistaparelles

def guardarAlphes(eventosMatched):
	alphessobrellindar=[]
	for grup in eventosMatched:
		alphesdegrup = retornaAlphes(grup)
		print alphesdegrup
		for alpha in alphesdegrup:
			alphessobrellindar.append(alpha)
	return alphessobrellindar
def guardarAlphes1x2(eventosMatched):
	alphessobrellindar=[]
	for grup in eventosMatched:
		alphesdegrup = retornaAlphes1x2(grup)
		for alpha in alphesdegrup:
			alphessobrellindar.append(alpha)
	return alphessobrellindar


def retornaAlphes(grup):
	alphes=[]
	if len(grup) < 2:
		a = definirAlpha(grup[0]['cuota1'], grup[0]['cuota2'])

		if a >= CONST_LLINDAR:
			infomilloralpha = []
			infomilloralpha.append(a)
			infomilloralpha.append(grup[0]["casa de apostes"])
			infomilloralpha.append(grup[0]["cuota1"])
			infomilloralpha.append(grup[0]["equipo1"])
			infomilloralpha.append(grup[0]["casa de apostes"])
			infomilloralpha.append(grup[0]["cuota2"])
			infomilloralpha.append(grup[0]["equipo2"])
			alphes.append(infomilloralpha)
	else:
		aux = grup
		for evento in grup:
			a = definirAlpha(evento['cuota1'], evento['cuota2'])
			if a >= CONST_LLINDAR:
				infomilloralpha = []
				infomilloralpha.append(a)
				infomilloralpha.append(evento["casa de apostes"])
				infomilloralpha.append(evento["cuota1"])
				infomilloralpha.append(evento["equipo1"])
				infomilloralpha.append(evento["casa de apostes"])
				infomilloralpha.append(evento["cuota2"])
				infomilloralpha.append(evento["equipo2"])
				alphes.append(infomilloralpha)
			aux.remove(evento)
			for ev in aux:
				a1, a2 = treureAlphas(evento['cuota1'], ev['cuota1'], evento['cuota2'], ev['cuota2'])
				if a1>=CONST_LLINDAR:
					infomilloralpha = []
					infomilloralpha.append(a1)
					infomilloralpha.append(evento["casa de apostes"])
					infomilloralpha.append(evento["cuota1"])
					infomilloralpha.append(evento["equipo1"])
					infomilloralpha.append(ev["casa de apostes"])
					infomilloralpha.append(ev["cuota2"])
					infomilloralpha.append(ev["equipo2"])
					alphes.append(infomilloralpha)
				if a2 >= CONST_LLINDAR:
					infomilloralpha=[]
					infomilloralpha.append(a2)
					infomilloralpha.append(evento["casa de apostes"])
					infomilloralpha.append(evento["cuota2"])
					infomilloralpha.append(evento["equipo2"])
					infomilloralpha.append(ev["casa de apostes"])
					infomilloralpha.append(ev["cuota1"])
					infomilloralpha.append(ev["equipo1"])
					alphes.append(infomilloralpha)
	return alphes

def retornaAlphes1x2(grup):
	alphes=[]
	if len(grup) < 2:	
		a = definirAlpha1x2(grup[0]['cuota1'],grup[0]['cuotaX'], grup[0]['cuota2'])
		if a >= CONST_LLINDAR:
			infomilloralpha = []
			infomilloralpha.append(a)
			infomilloralpha.append(grup[0]["casa de apostes"])
			infomilloralpha.append(grup[0]["cuota1"])
			infomilloralpha.append(grup[0]["equipo1"])
			infomilloralpha.append(grup[0]["casa de apostes"])
			infomilloralpha.append(grup[0]["cuotaX"])
			infomilloralpha.append(grup[0]["casa de apostes"])
			infomilloralpha.append(grup[0]["cuota2"])
			infomilloralpha.append(grup[0]["equipo2"])
			alphes.append(infomilloralpha)
	else:	
		col1 = []
		col2 = []
		col3 = []		
		for each in grup:
			col1.append(each['equipo1'])
			col1.append(each['cuota1'])
			col1.append(each['casa de apostes'])
			col2.append(None)
			col2.append(each['cuotaX'])
			col2.append(each['casa de apostes'])
			col3.append(each['equipo2'])
			col3.append(each['cuota2'])
			col3.append(each['casa de apostes'])
		contador1 = 0
		for ele1 in col1:
			contador1 += 1
			contador2 = 0
			for ele2 in col2:
				contador3 = 0
				contador2 += 1
				for ele3 in col3:
					contador3 += 1
					try:
						alpha = definirAlpha1x2(float(ele1), float(ele2), float(ele3))
						if alpha >= CONST_LLINDAR:
							infomilloralpha = []
							infomilloralpha.append(alpha)
							infomilloralpha.append(col1[contador1])
							infomilloralpha.append("["+col1[contador1-2])
							infomilloralpha.append(ele1+"]")
							infomilloralpha.append(col2[contador2])
							infomilloralpha.append("["+"Empate")
							infomilloralpha.append(ele2+"]")
							infomilloralpha.append(col3[contador3])
							infomilloralpha.append("["+col3[contador3-2])
							infomilloralpha.append(ele3+"]")

							alphes.append(infomilloralpha)
							contador += 1
					except:
						pass
	return alphes

def mirarPartitMateixosEquips(evento1, evento2):
	return 
def printAlphesColor(llistaeventos):
	possiblesErrors = []
	contador = 0
	for evento in llistaeventos:
		if evento[0] < 0.99:
			contador += 1
			printNumeracio(contador)
			print evento
		elif evento[0] > 1.15:
			possiblesErrors.append(evento)
		elif evento[0] > 1:
			contador += 1
			printNumeracio(contador)
			printVerdNegrita(evento)
		else:
			contador += 1
			printNumeracio(contador)
			printVerd(evento)
	if len(possiblesErrors) > 1:
		print " POSSIBLES ERRORS: "
		contador = 0
		for possibleError in possiblesErrors:
			contador += 1
			printNumeracio(contador)
			printVermellNegrita(possibleError)

def trobaralphas():
	checkFootball()
	checkBaseball()

completarArrays()
completarArrays1x2()
trobaralphas()

	

		
	
	


