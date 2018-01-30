import csv
import re
import numbers
from operator import itemgetter

CONST_LLINDAR = 0.96

sportiumstuff=[]
bwinstuff=[]
interwettenstuff=[]


#definnir Alpha 
def definirAlpha(q, w):
	alpha = ((float(q)*float(w))/(float(q)+float(w)))
	return round(alpha, 4)

#retornar possibles alphas amb dugues cases

def treureAlphas(a1,b1,a2,b2):

	alpha1 = definirAlpha(a1,b2)

	alpha2 = definirAlpha(b1,a2)

	return alpha1, alpha2	
#completa arrays agafant del csv

def completarArrays():
	csvFiletoRead = open("/home/miquelpuig/Documents/collectData/prog/csvdocs/data.csv", 'r')
	reader = csv.DictReader(csvFiletoRead)
	for r in reader:
		if r["casa de apostes"] == 'Sportium':
			sportiumstuff.append(r)
		elif r["casa de apostes"] == 'Bwin':
			bwinstuff.append(r)
		elif r["casa de apostes"] == 'Interwetten':
			interwettenstuff.append(r)
		else:
			print "casa no encontrada"
	print "Arrays completados..."

#agafa els stuffs excepte el passat per parametre
def getStuffArray():
	cases = []

	cases.append(sportiumstuff)

	cases.append(bwinstuff)

	cases.append(interwettenstuff)

	return cases

#et diu si el 75% de les lletres son iguals entre dos arrays
def checkInicials(a, b):
	inicials1=[]
	inicials2=[]
	for lletresA in a:
		if lletresA.isalpha():
			inicials1.append(lletresA)
	for lletresB in b:
		if lletresB.isalpha():
			inicials2.append(lletresB)
	contadoriguals = 0
	for i1 in inicials1:
		for i2 in inicials2:
			if i1 == i2:
				contadoriguals += 2
				break
	length = len(inicials1)+len(inicials2)

	if (contadoriguals >= 0.75*length):
		return True
	return False
def sortListbyFirstIndex(data):
	return 	data[data[:,0].argsort()]
	
def checkInicialsPercentatge(a1, b1, a2, b2):

	inicials1a=[]
	inicials2a=[]
	inicials1b=[]
	inicials2b=[]
	for lletresA in a1:
		if lletresA.isalpha():
			inicials1a.append(lletresA)
	for lletresB in b1:
		if lletresB.isalpha():
			inicials2a.append(lletresB)
	for lletresA in a2:
		if lletresA.isalpha():
			inicials1b.append(lletresA)
	for lletresB in b2:
		if lletresB.isalpha():
			inicials2b.append(lletresB)

	iguals1 = []
	iguals2 = []
	for i1 in inicials1a:
		for i2 in inicials1b:
			if i1 == i2:
				iguals1.append(i1)
				break	
	for i1 in inicials2a:
		for i2 in inicials2b:
			if i1 == i2:
				iguals2.append(i1)
				break

	contador = 0
	if (iguals1 == inicials1a)|(iguals1 == inicials1b):
		contador +=0.5
	elif checkInicials(inicials1a, inicials1b):
		contador += 0.25
	if (iguals2 == inicials2a)|(iguals1 == inicials2b):
		contador +=0.5
	elif checkInicials(inicials2a, inicials2b):
		contador += 0.25
	return contador
def checkTennis():
	print "Checking Tennis..."
	tennismatches=[]
	for casa in getStuffArray():
		for evento in casa:
			if evento['sport'] == 'Tennis':
				tennismatches.append(evento)
	alpha = guardarAlphes(checkForPairsinList(tennismatches))
	for a in alpha:
		print a
def checkBaseball():
	print "Checking Baseball..."
	baseballmatches=[]
	for casa in getStuffArray():
		for evento in casa:
			if evento['sport'] == 'Baseball':
				baseballmatches.append(evento)
	alpha = guardarAlphes(checkForPairsinList(baseballmatches))
	for a in alpha:
		print a


def checkForPairsinList(array):
	arrayaux = array
	llistaparelles = []
	for a in array:
		arrayaux.remove(a)
		aux = []
		if ((isinstance(float(a["cuota1"]), float))and(isinstance(float(a["cuota2"]), float))):
			aux.append(a)
			for b in arrayaux:
				if ((isinstance(float(b["cuota1"]), numbers.Real))and(isinstance(float(b["cuota2"]), numbers.Real))): 
					if (a['equipo1'].split()[-1] == b['equipo1'].split()[-1])and(a['equipo2'].split()[-1] == b['equipo2'].split()[-1]):
						aux.append(b)
						arrayaux.remove(b)
					elif (checkInicialsPercentatge(a['uppers1'], a['uppers2'], b['uppers1'], b['uppers2']) >= 0.75):
						aux.append(b)
						arrayaux.remove(b)
			llistaparelles.append(aux)
	return llistaparelles

def guardarAlphes(eventosMatched):
	alphessobrellindar=[]
	for grup in eventosMatched:
		alphesdegrup = retornaAlphes(grup)
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
				
		 
		
		
	
	
'''
def checkRestaDeCases(array):
	cases = addStuff(array)
	for a in array:
		if ((isinstance(float(a["cuota1"]), float))and(isinstance(float(a["cuota2"]), float))):
			for stuff in cases:
				for b in stuff:
					if ((isinstance(float(b["cuota1"]), numbers.Real))and(isinstance(float(b["cuota2"]), numbers.Real))): 
						if (a['equipo1'].split()[-1] == b['equipo1'].split()[-1]):
							if(a['equipo2'].split()[-1] == b['equipo2'].split()[-1]):
								a1, a2 = treureAlphas(a['cuota1'], b['cuota1'], a['cuota2'], b['cuota2'])
								if a1>CONST_LLINDAR:
									infomilloralpha = []
									infomilloralpha.append(a1)
									infomilloralpha.append(a["casa de apostes"])
									infomilloralpha.append(a["cuota1"])
									infomilloralpha.append(a["equipo1"])
									infomilloralpha.append(b["casa de apostes"])
									infomilloralpha.append(b["cuota2"])
									infomilloralpha.append(b["equipo2"])
									sureBets.append(infomilloralpha)
								if a2>CONST_LLINDAR:
									infomilloralpha=[]
									infomilloralpha.append(a2)
									infomilloralpha.append(a["casa de apostes"])
									infomilloralpha.append(a["cuota2"])
									infomilloralpha.append(a["equipo2"])
									infomilloralpha.append(b["casa de apostes"])
									infomilloralpha.append(b["cuota1"])
									infomilloralpha.append(b["equipo1"])
									sureBets.append(infomilloralpha)
						elif ((a['equipo1'].split()[-1] == b['equipo1'].split()[0])|(a['equipo1'].split()[0] == b['equipo1'].split()[-1])):
							if(a['equipo2'].split()[-1] == b['equipo2'].split()[0])|(a['equipo2'].split()[0] == b['equipo2'].split()[-1]):
								if checkInicials(a['uppers1'], b['uppers1']):
									if checkInicials(a['uppers2'], b['uppers2']):
										a1, a2 = treureAlphas(a['cuota1'], b['cuota1'], a['cuota2'], b['cuota2'])
										if a1>CONST_LLINDAR:
											infomilloralpha = []
											infomilloralpha.append(a1)
											infomilloralpha.append(a["casa de apostes"])
											infomilloralpha.append(a["cuota1"])
											infomilloralpha.append(a["equipo1"])
											infomilloralpha.append(b["casa de apostes"])
											infomilloralpha.append(b["cuota2"])
											infomilloralpha.append(b["equipo2"])
											sureBets.append(infomilloralpha)
										if a2>CONST_LLINDAR:
											infomilloralpha=[]
											infomilloralpha.append(a2)
											infomilloralpha.append(a["casa de apostes"])
											infomilloralpha.append(a["cuota2"])
											infomilloralpha.append(a["equipo2"])
											infomilloralpha.append(b["casa de apostes"])
											infomilloralpha.append(b["cuota1"])
											infomilloralpha.append(b["equipo1"])
											sureBets.append(infomilloralpha)
					



'''	
def trobaralphas():
	checkBaseball()
	checkTennis()


completarArrays()
trobaralphas()

	

		
	
	


