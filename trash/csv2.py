import csv
import re


cases=["Sportium", "Bet365", "Wanabet", "Luckia", "Williamhill", "GoldenPark"]

casa1=[]
casa2=[]
millorsalphas = []
millorsalphas.append(0)


def preguntarCases():
	print"==================================================================="
	print "Cases disponibles: "
	print cases[:]
	print ""
	print "Escriu la primera casa:"

	sortida = True
	while (sortida):
		casa = raw_input()
		for c in cases:
			if casa == c:
				casa1 = casa
				sortida = False
				break
		if sortida:
			print "Casa Incorrecte... Reescriu triant una de les opcions: "
			print cases[:]
	print "Primera casa guardada. Escriu la segona casa:"
	sortida = True
	while (sortida):
		casa = raw_input()
		if casa != casa1:
			for c in cases:
				if casa == c:
					casa2 = casa
					sortida = False
					break
		if sortida:
			print "Casa Incorrecte o repetida... Reescriu triant una de les opcions: "
			print cases[:]
			print ""
	print "Segona casa guardada."
	return casa1, casa2



def completarArrays():
	csvFiletoRead = open("/home/miquelpuig/Documents/collectData/prog/csvdocs/data.csv", 'r')
	reader = csv.DictReader(csvFiletoRead)
	primera, segona = preguntarCases()
	for r in reader:
		if r["casa de apostes"] == primera:
			casa1.append(r)
		elif r["casa de apostes"] == segona:
			casa2.append(r)


def definirAlpha(q, w):
	alpha = 0
	try:
		alpha = ((float(q)*float(w))/(float(q)+float(w)))
	except ValueError:
		print "Objeto erroneo"
	return alpha


def millorAlpha(best,a1,b1,a2,b2):

	alpha1 = definirAlpha(a1,b2)

	alpha2 = definirAlpha(b1,a2)

	if alpha1>=alpha2:
		if alpha1>best:
			return "A", alpha1
	else:
		if alpha2>best:
			return "B", alpha2
	return "C",0

def trobaralpha():
	infomilloralpha=[]
	infomilloralpha.append(0)

	for s in casa1:
		uppers1=[]
		uppers2= []

		equip1 = s["equipo1"].split()
		for paraula in equip1:
			for letter in paraula:
				if letter.isupper():
					uppers1.append(letter)
				break

		for b in casa2:
			acces = False
			equip2 = b["equipo1"].split()
			for paraula in equip2:
				for letter in paraula:
					if letter.isupper():
						uppers2.append(letter)
					break
		
			contador = 0
			for u1 in uppers1:
				for u2 in uppers2:
					if u1 == u2:
						contador += 1
			
			print contador
			if equip1[-1] == equip2[-1]:
				minim = min(len(uppers1), len(uppers2))
				maxim = max(len(uppers1), len(uppers2))
				if minim < 3:
					if contador == minim:
						acces = True

				else:
					if contador >= minim-1:
						acces = True

			if acces:
				a = [s["cuota1"], s["cuota2"], b["cuota1"], b["cuota2"]]
				lletra, alpha = millorAlpha(millorsalphas[0],a[0], a[1], a[2], a[3])
				if lletra == "C":
					break
				elif lletra == "A":
					infomilloralpha = []
					infomilloralpha.append(alpha)
					infomilloralpha.append(s["casa de apostes"])
					infomilloralpha.append(s["cuota1"])
					infomilloralpha.append(s["equipo1"])
					infomilloralpha.append(b["casa de apostes"])
					infomilloralpha.append(b["cuota2"])
					infomilloralpha.append(b["equipo2"])
				elif lletra == "B":
					infomilloralpha=[]
					infomilloralpha.append(alpha)
					infomilloralpha.append(s["casa de apostes"])
					infomilloralpha.append(s["cuota2"])
					infomilloralpha.append(s["equipo2"])
					infomilloralpha.append(b["casa de apostes"])
					infomilloralpha.append(b["cuota1"])
					infomilloralpha.append(b["equipo1"])
		millorsalphas.append(infomilloralpha[0])		

completarArrays()
trobaralpha()
print""
print"==================================================================="
print millorsalphas




