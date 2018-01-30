import csv
import re


cases=["Sportium", "Bet365", "Wanabet", "Luckia", "Williamhill", "GoldenPark"]

casa1=[]
casa2=[]



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
	return ((float(q)*float(w))/(float(q)+float(w)))

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
		equip = s["equipo1"].split()[-1]
		for b in casa2:
			if b["equipo1"].split()[-1] == equip :
				a = [s["cuota1"], s["cuota2"], b["cuota1"], b["cuota2"]]
				lletra, alpha = millorAlpha(infomilloralpha[0],a[0], a[1], a[2], a[3])
				sortida = True
				for l in a:
					if float:
						print"aqui"
						sortida = False
				if sortida:
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
	return infomilloralpha		

completarArrays()
var = trobaralpha()
print""
print"==================================================================="
print "Alpha:   %.4f" % var[0]
print var[1:4]
print var[4:7]



