from bs4 import BeautifulSoup
from bs4 import Comment
import csv

writer = csv.writer(open("/home/miquelpuig/Documents/collectData/prog/csvdocs/data.csv", 'w+'))
writer.writerow(('sport','casa de apostes','equipo1', 'cuota1', 'equipo2', 'cuota2', 'uppers1', 'uppers2'))


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

def sportiumBaseballScraper():
	file = open("htmls/sportium/baseball.txt","r")
	bsObj = BeautifulSoup(file, "lxml")
	fragments = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).findAll("div", {"class":"fragment"})
	alltr = fragments[-1].find("div", {"class":"expander-content"}).find("div", {"class":None}).table.tbody.findAll("tr")
	for tr in alltr:
		selns = tr.findAll("td", {"class":"seln"})
		acces = True
		for seln in selns:
			nomicuota  = seln.div.button.span
			noms = nomicuota.find("span",{"class":"seln-label"}).text.split()
			nom=""
			for n in noms:
				nom += n+" "
			cuota = nomicuota.find("span",{"class":"price dec"}).text
			if acces:
				equip1 = nom
				cuota1 = cuota
			else:
				equip2 = nom
				cuota2 = cuota
				u1, u2 = ferUppers(equip1, equip2)		
				writer.writerow(('Baseball','Sportium',equip1, cuota1, equip2, cuota2, u1, u2))
			acces = False
def changeComa(word):
	for letter in word:
		if letter == ",":
			word = word.replace(letter, ".")
			return word
	return "error"
def interwettenBaseballScraper():
	file = open("htmls/interwetten/baseball.txt", "r")
	bsObj = BeautifulSoup(file, "lxml")

	lligues = bsObj.find("form").find("div", {"class":"pageroot"}).table.find("tr").find("td", {"class":"colmiddle"}).findAll("div", {"class":"bets shadow"})
	for lliga in lligues:
		cuadrepartits = lliga.table
		even = cuadrepartits.findAll("tr", {"class":"even"})
		odd = cuadrepartits.findAll("tr", {"class":"odd"})
		for partits in even:
			equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
			acces = True
			for equip in equips:
				if acces:
					equip1 = equip.p.span.text
					cuota1 = equip.p.strong.text
				else:
					equip2 = equip.p.span.text
					cuota2 = equip.p.strong.text
					u1, u2 = ferUppers(equip1, equip2)		
					writer.writerow(('Baseball','Interwetten',equip2, changeComa(cuota2), equip1, changeComa(cuota1), u1, u2))
		    		acces = False
		for partits in odd:
			equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
			acces = True
			for equip in equips:
				if acces:
					equip1 = equip.p.span.text
					cuota1 = equip.p.strong.text
				else:
					equip2 = equip.p.span.text
					cuota2 = equip.p.strong.text
					u1, u2 = ferUppers(equip1, equip2)		
					writer.writerow(('Baseball','Interwetten',equip2, changeComa(cuota2), equip1, changeComa(cuota1), u1, u2))
				acces = False
def bwinBaseballScraper():
	file = open("htmls/bwin/baseball.txt","r")
	bsObj = BeautifulSoup(file, "lxml")
	cuadreSeparatDies = bsObj.find("div", {"class":"container"}).find("div", {"id":"plugin-wrapper"}).find("div", {"id":"main-wrap"}).div.find("div", {"class":"center "}).div.find("div", {"id":"markets-container"}).div.findAll("div", {"class", "ui-widget-content"})
	for dies in cuadreSeparatDies:
		lligues = dies.find("div", {"class":"ui-widget-content-body"}).div.div.div.find("div").findAll("div", {"class":"marketboard-event-group__item--sub-group"})
		for lliga in lligues:
			partits = lliga.find("div", {"class":"marketboard-event-group__item-container marketboard-event-group__item-container--level-3"}).findAll("div", {"class":"marketboard-event-group__item--event"})
			for partit in partits:
				equips = partit.find("div", {"class":"marketboard-event-with-header"}).find("div", {"class":"marketboard-event-with-header__markets-container"}).table.tr.findAll("td")
				acces = True
				for equip in equips:
					button = equip.find("button")
					nom = button.find("div", {"class":"mb-option-button__option-name mb-option-button__option-name--odds-4"}).text
					cuota = button.find("div", {"class":"mb-option-button__option-odds "}).text
					if acces:
						equip1 = nom
						cuota1 = cuota
					else:
						equip2 = nom
						cuota2 = cuota
						u1, u2 = ferUppers(equip1, equip2)		
						writer.writerow(('Baseball','Bwin',equip1, cuota1, equip2, cuota2, u1, u2))
					acces = False

def williamhillBaseballScraper():
	return
def baseballmakeData():
	sportiumBaseballScraper()
	interwettenBaseballScraper()
	bwinBaseballScraper()
	williamhillBaseballScraper()

baseballmakeData()
'''
def sportiumScraper():
	sportiumBb = open("htmls/sportium.txt","r")
	bsObj = BeautifulSoup(sportiumBb, "lxml")
	divs = bsObj.findAll("div",{"class":"inactive-tab"})
	cont = 0
	for d in divs:
		id = d["id"]
		if (id == 'upcoming-tab-TENN'):
			tbodys = d.div.find("div",{"class":"pager-content"}).find("div",{"class":"pager-page"}).table.findAll("tbody")
			for body in tbodys:
				if body.tr is not None:
					mkts = body.findAll("tr",{"class":"mkt"})
					for mkt in mkts:
						cont = 0
						tdgrup = mkt.findAll("td")
						for td in tdgrup:
							if td.has_attr('colspan'):
								if td.div is not None:
									cont = cont+ 1
									if cont%2 == 1:
										equipo1 = td.find("div").button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota1 = td.find("div").button.span.find("span",{"class":"price dec"}).get_text()
									elif cont%2 == 0:
										equipo2 = td.div.button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota2 = td.div.button.span.find("span",{"class":"price dec"}).get_text()
										u1, u2 = ferUppers(equipo1, equipo2)		
										writer.writerow(('Tennis','Sportium',equipo1, cuota1, equipo2, cuota2, u1, u2))
			print "Sportium Tennis Checked"

		elif (id == 'upcoming-tab-BASK'):
			tbodys = d.div.find("div",{"class":"pager-content"}).find("div",{"class":"pager-page"}).table.findAll("tbody")
			for body in tbodys:
				if body.tr is not None:
					mkts = body.findAll("tr",{"class":"mkt"})
					for mkt in mkts:
						cont = 0
						tdgrup = mkt.findAll("td")
						for td in tdgrup:
							if td.has_attr('colspan'):
								if td.div is not None:
									cont = cont+ 1
									if cont%2 == 1:
										equipo1 = td.find("div").button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota1 = td.find("div").button.span.find("span",{"class":"price dec"}).get_text()
									elif cont%2 == 0:
										equipo2 = td.div.button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota2 = td.div.button.span.find("span",{"class":"price dec"}).get_text()
										u1, u2 = ferUppers(equipo1, equipo2)		
										writer.writerow(('Basket','Sportium',equipo1, cuota1, equipo2, cuota2, u1, u2))
			print "Sportium Basket Checked"

		elif (id == 'upcoming-tab-VOLL'):
			tbodys = d.div.find("div",{"class":"pager-content"}).find("div",{"class":"pager-page"}).table.findAll("tbody")
			for body in tbodys:
				if body.tr is not None:
					mkts = body.findAll("tr",{"class":"mkt"})
					for mkt in mkts:
						cont = 0
						tdgrup = mkt.findAll("td")
						for td in tdgrup:
							if td.has_attr('colspan'):
								if td.div is not None:
									cont = cont+ 1
									if cont%2 == 1:
										equipo1 = td.find("div").button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota1 = td.find("div").button.span.find("span",{"class":"price dec"}).get_text()
									elif cont%2 == 0:
										equipo2 = td.div.button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota2 = td.div.button.span.find("span",{"class":"price dec"}).get_text()
										u1, u2 = ferUppers(equipo1, equipo2)		
										writer.writerow(('Volley','Sportium',equipo1, cuota1, equipo2, cuota2, u1, u2))
			print "Sportium Volley Checked"
		elif (id == 'upcoming-tab-BASE'):
			tbodys = d.div.find("div",{"class":"pager-content"}).find("div",{"class":"pager-page"}).table.findAll("tbody")
			for body in tbodys:
				if body.tr is not None:
					mkts = body.findAll("tr",{"class":"mkt"})
					for mkt in mkts:
						cont = 0
						tdgrup = mkt.findAll("td")
						for td in tdgrup:
							if td.has_attr('colspan'):
								if td.div is not None:
									cont = cont+ 1
									if cont%2 == 1:
										equipo1 = td.find("div").button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota1 = td.find("div").button.span.find("span",{"class":"price dec"}).get_text()
									elif cont%2 == 0:
										equipo2 = td.div.button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota2 = td.div.button.span.find("span",{"class":"price dec"}).get_text()
										u1, u2 = ferUppers(equipo1, equipo2)		
										writer.writerow(('Baseball','Sportium',equipo1, cuota1, equipo2, cuota2, u1, u2))
			print "Sportium Baseball Checked"
		elif (id == 'upcoming-tab-DART'):
			tbodys = d.div.find("div",{"class":"pager-content"}).find("div",{"class":"pager-page"}).table.findAll("tbody")
			for body in tbodys:
				if body.tr is not None:
					mkts = body.findAll("tr",{"class":"mkt"})
					for mkt in mkts:
						cont = 0
						tdgrup = mkt.findAll("td")
						for td in tdgrup:
							if td.has_attr('colspan'):
								if td.div is not None:
									cont = cont+ 1
									if cont%2 == 1:
										equipo1 = td.find("div").button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota1 = td.find("div").button.span.find("span",{"class":"price dec"}).get_text()
									elif cont%2 == 0:
										equipo2 = td.div.button.span.find("span",{"class":"seln-label"}).span.span.get_text().encode('utf-8')
										cuota2 = td.div.button.span.find("span",{"class":"price dec"}).get_text()
										u1, u2 = ferUppers(equipo1, equipo2)		
										writer.writerow(('Dards','Sportium',equipo1, cuota1, equipo2, cuota2, u1, u2))
			print "Sportium Dardos Checked"


#####################################################SPORTIUM
def wanabetTennisScraper():
	wanabetT = open("htmls/tennis/wanabet.txt","r")
	bsObj = BeautifulSoup(wanabetT, "lxml")
	#obro primer element que conte tota la info, surt una llista
	divs = bsObj.findAll("div",{"class":"KambiBC-collapsible-container KambiBC-mod-event-group-container KambiBC-expanded"})
	#per cada element de la llista	
	for d in divs:
		#filtro per tag: li
		lis = d.find("div",{"class":"KambiBC-collapsible-content KambiBC-mod-event-group-event-container"}).find("ul",{"class":"KambiBC-list-view__column"}).findAll("li",{"class":"KambiBC-event-item KambiBC-event-item--combined-betoffers KambiBC-event-item--type-match"})
		#l es un element de lis
		for l in lis:
			#vecotrInfo conte tots els botons de tots els partits
			vectorInfo = l.a.div.find("div",{"class":"KambiBC-event-item__bet-offers-container"}).div.div.find("div",{"class":"KambiBC-list-view__column KambiBC-bet-offers-list__column"}).div.div.findAll("button",{"class":"KambiBC-mod-outcome"})
			#Separo els botons buscats amb la info	
			cont = 0
			for v in vectorInfo:
				cont = cont + 1
				if cont%2 == 1:
					equipo1 = v.div.find("div",{"class":"KambiBC-mod-outcome__label-wrapper"}).span.get_text().encode('utf-8')
					cuota1 = v.div.find("div",{"class":"KambiBC-mod-outcome__odds-wrapper"}).span.get_text()	
				elif cont%2 == 0:
					equipo2 = v.div.find("div",{"class":"KambiBC-mod-outcome__label-wrapper"}).span.get_text().encode('utf-8')
		 			cuota2 = v.div.find("div",{"class":"KambiBC-mod-outcome__odds-wrapper"}).span.get_text()
					u1, u2 = ferUppers(equipo1, equipo2)		
					writer.writerow(('Tennis','Wanabet',equipo1, cuota1, equipo2, cuota2, u1, u2))
	print("Wanabet Tennis checked.")



def wanabetBeisbolScraper():
	
	wanabetBb = open("htmls/beisbol/wanabet.txt","r")
	bsObj = BeautifulSoup(wanabetBb, "lxml")
	#obro primer element que conte tota la info, surt una llista
	divs = bsObj.findAll("div",{"class":"KambiBC-collapsible-container KambiBC-mod-event-group-container KambiBC-expanded"})
	#per cada element de la llista	
	for d in divs:
		#filtro per tag: li
		lis = d.find("div",{"class":"KambiBC-collapsible-content KambiBC-mod-event-group-event-container"}).find("ul",{"class":"KambiBC-list-view__column"}).findAll("li",{"class":"KambiBC-event-item KambiBC-event-item--combined-betoffers KambiBC-event-item--type-match"})
		#l es un element de lis
		for l in lis:
			#vecotrInfo conte tots els botons de tots els partits
			vectorInfo = l.a.div.find("div",{"class":"KambiBC-event-item__bet-offers-container"}).div.div.find("div",{"class":"KambiBC-list-view__column KambiBC-bet-offers-list__column"}).div.div.findAll("button",{"class":"KambiBC-mod-outcome"})
			#Separo els botons buscats amb la info	
			cont = 0
			for v in vectorInfo:
				cont = cont + 1
				if cont%2 == 1:
					equipo1 = v.div.find("div",{"class":"KambiBC-mod-outcome__label-wrapper"}).span.get_text().encode('utf-8')
					cuota1 = v.div.find("div",{"class":"KambiBC-mod-outcome__odds-wrapper"}).span.get_text()	
				elif cont%2 == 0:
					equipo2 = v.div.find("div",{"class":"KambiBC-mod-outcome__label-wrapper"}).span.get_text().encode('utf-8')
		 			cuota2 = v.div.find("div",{"class":"KambiBC-mod-outcome__odds-wrapper"}).span.get_text()
					u1, u2 = ferUppers(equipo1, equipo2)		
					writer.writerow(('Baseball','Wanabet',equipo2, cuota2, equipo1, cuota1, u2, u1))
	print("Wanabet Baseball checked.")

def bet365TennisScraper():

	bet365Bb = open("htmls/beisbol/bet365.txt","r")
	bsObj = BeautifulSoup(bet365Bb, "lxml")
	cont = 0
	#cuotes i noms
	cuotesCasa = []
	cuotesFora = []
	nomsCasa = []
	nomsFora = []
	cuadresPartits = bsObj.findAll("div")
	for cuadre in cuadresPartits:
		hey = cuadre.find("div",{"class":"gl-MarketGroup_Wrapper "})
		print hey





	#objectes mes generals possibles
	divsCuotes = bsObj.findAll("div",{"class":"sl-MarketCouponBaseball gl-Market_General gl-Market_AdditionalRowHeight gl-Market_PWidth-15-4 "})
	divsNomsEquips = bsObj.find("div",{"class":"sl-MarketCouponValuesExplicit13 gl-Market_General gl-Market_HasLabels "}).findAll("div")

	for w in divsNomsEquips:
		if w.div is not None:
			if w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}) is not None:
				cont = cont + 1
				if cont%2 == 1:
					nomsCasa.append(w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}).div.get_text())
				elif cont%2 == 0:
					nomsFora.append(w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}).div.get_text())
					
	
	cont = 0
	for w in divsCuotes:
		if w.find("div",{"class":"gl-ParticipantOddsOnlyDarker sl-CouponParticipantBaseballOddsOnly gl-ParticipantOddsOnly gl-Participant_General "}) is not None:
			divscuotes = w.findAll("div")
			for f in divscuotes:
				if f.span is not None:
					cont = cont + 1
					if cont%2 == 1:
						cuotesCasa.append(f.span.get_text())
					elif cont%2 == 0:
						cuotesFora.append(f.span.get_text())	

	for a,b,c,d in zip(nomsCasa, cuotesCasa, nomsFora, cuotesFora):
		writer.writerow(('Bet365',a,b,c,d))
	cont = 0
	print("Bet365 Tennis Checked.")


def bet365BeisbolScraper():
	bet365Bb = open("htmls/beisbol/bet365.txt","r")
	bsObj = BeautifulSoup(bet365Bb, "lxml")
	cont = 0
	#cuotes i noms
	cuotesCasa = []
	cuotesFora = []
	nomsCasa = []
	nomsFora = []
	#objectes mes generals possibles
	divsCuotes = bsObj.findAll("div",{"class":"sl-MarketCouponBaseball gl-Market_General gl-Market_AdditionalRowHeight gl-Market_PWidth-15-4 "})
	divsNomsEquips = bsObj.find("div",{"class":"sl-MarketCouponValuesExplicit13 gl-Market_General gl-Market_HasLabels "}).findAll("div")

	for w in divsNomsEquips:
		if w.div is not None:
			if w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}) is not None:
				cont = cont + 1
				if cont%2 == 1:
					nomsCasa.append(w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}).div.get_text())
				elif cont%2 == 0:
					nomsFora.append(w.find("div",{"class":"sl-CouponParticipantGameLineTwoWayWithPitchers_Name "}).div.get_text())
					
	
	cont = 0
	for w in divsCuotes:
		if w.find("div",{"class":"gl-ParticipantOddsOnlyDarker sl-CouponParticipantBaseballOddsOnly gl-ParticipantOddsOnly gl-Participant_General "}) is not None:
			divscuotes = w.findAll("div")
			for f in divscuotes:
				if f.span is not None:
					cont = cont + 1
					if cont%2 == 1:
						cuotesCasa.append(f.span.get_text())
					elif cont%2 == 0:
						cuotesFora.append(f.span.get_text())	

	for a,b,c,d in zip(nomsCasa, cuotesCasa, nomsFora, cuotesFora):
		if (b.isalpha() or d.isalpha()):
			print "Partit erroni"
		else:
			u1, u2 = ferUppers(a, c)		
			writer.writerow(('Baseball','Bet365',a,b,c,d, u1, u2))
	cont = 0
	print("Bet365 Baseball Checked.")
'''

