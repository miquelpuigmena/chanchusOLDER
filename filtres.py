#def checkLletresNoms(nom1, nom2):
	
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
	return contador >= 0.75

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

