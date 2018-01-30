from utilsScraper import *
from writer import *
from bs4 import BeautifulSoup
import numbers


##SPORTIUM##
def sportiumTennisScraper():
	try:
		file = open("htmls/sportium/tennis.txt","r")
		bsObj = BeautifulSoup(file, "lxml")
		torneos = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).findAll("div", {"class":"fragment"})[-1].findAll("div", {"class":"expander"})
		for torneo in torneos:
			alltr = torneo.find("div", {"class":"expander-content"}).div.table.findAll("tr", {"class":"mkt"})
			for tr in alltr:
				selns = tr.findAll("td", {"class":"seln"})
				acces = True
				for seln in selns:
					nomicuota  = seln.div.button.span
					noms = nomicuota.find("span",{"class":"seln-label"}).text.encode('utf-8').split()
					nom=""
					for n in noms:
						nom += n+" "
					cuota = nomicuota.find("span",{"class":"price dec"}).text
					if acces:
						equip1 = checkNomsTennisDobles(nom)	
						cuota1 = cuota
					else:
						equip2 = checkNomsTennisDobles(nom)
						cuota2 = cuota
						writerCSV('Tennis','Sportium', equip1, cuota1, equip2, cuota2)
					acces = False
	except:
		printError('Sportium: Tennis Scraper Failed')	


##INTERWETTEN##
def interwettenTennisScraper():
	try:
		file = open("htmls/interwetten/tennis.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		lligues = bsObj.find("form").find("div", {"class":"pageroot"}).table.find("tr").find("td", {"class":"colmiddle"}).findAll("div", {"class":"bets shadow"})
		for lliga in lligues:
			cuadrepartits = lliga.find("table")
			even = cuadrepartits.findAll("tr", {"class":"even"})
			odd = cuadrepartits.findAll("tr", {"class":"odd"})
			for partits in even:
				equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
				acces = True
				for equip in equips:
					if acces:
						equip1 = checkNomsTennisDobles(equip.p.span.text)
						cuota1 = equip.p.strong.text
					else:
						equip2 = checkNomsTennisDobles(equip.p.span.text)
						cuota2 = equip.p.strong.text
						writerCSV('Tennis','Interwetten', equip1, replaceChar(cuota1, ',', '.'), equip2, replaceChar(cuota2, ',', '.'))
			    		acces = False
			for partits in odd:
				equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
				acces = True
				for equip in equips:
					if acces:
						equip1 = checkNomsTennisDobles(equip.p.span.text)
						cuota1 = equip.p.strong.text
					else:
						equip2 = checkNomsTennisDobles(equip.p.span.text)
						cuota2 = equip.p.strong.text
						writerCSV('Tennis','Interwetten', equip1, replaceChar(cuota1, ',', '.'), equip2, replaceChar(cuota2, ',', '.'))
					acces = False
	except:
		printError('Interwetten: Tennis Scraper Failed')	

##TIPBET##
def tipbetTennisScraper():
	try:
		file = open ("htmls/tipbet/tennis.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		containers = bsObj.findAll("div", {"class":"container"})
		for contain in containers:
			if (contain.find("div", {"class":"main-container"}) is not None):
				partits = contain.find("div", {"class":"main-container"}).find("div", {"id":"content"}).find("section").find("div").findAll("div")[-1].table.findAll("tbody", {"class":"match-line"})
				for partit in partits:
					noms = partit.find("tr", {"class":"main-line"}).find("td", {"class":"col2"}).span.text
					cuota1 = partit.find("tr", {"class":"main-line"}).find("td", {"class":"col4"}).span.text
					cuota2 = partit.find("tr", {"class":"main-line"}).find("td", {"class":"col5"}).span.text
					vectornoms = separarEquipos(noms, ":")
					writerCSV('Tennis', 'Tipbet', checkNomsTennisDobles(vectornoms[0]), cuota1, checkNomsTennisDobles(vectornoms[1]), cuota2)
	except:
		printError('Tipbet: Tennis Scraper Failed')	


###BETFAIR###
def betfairTennisScraper():
	try:
		file = open ('htmls/betfair/tennis.txt')
		bsObj = BeautifulSoup(file, "lxml")

		dies = bsObj.find("div", {"id":"zone-container"}).div.div.find("div", {"class":"grid-1 "}).div.findAll("div", {"class":"grid-1 "})[1].div.div.div.div.find("div", {"class":"updated-markets browse-all-container"}).div.find("ul").findAll("li", {"class":"section"})
		for dia in dies:
			partitsmig = dia.find("ul", {"class":"event-list"}).findAll("li", {"class":"com-coupon-line avb-row market-avb large "})
			partitlast = dia.find("ul", {"class":"event-list"}).findAll("li", {"class":"com-coupon-line avb-row market-avb large last"})
			partits = partitsmig + partitlast
			for  partit  in partits:
				if (partit.div.find("div", {"class":"details-market market-0-runners"}).find("div", {"class":"runner-list"}).find("span", {"class":"ui-market-status-message"}) == None):	
					equip1 = partit.div.find("div", {"class":"details-event"}).find("div").a.find("span", {"class":"home-team-name"}).text
					equip2 = partit.div.find("div", {"class":"details-event"}).find("div").a.find("span", {"class":"away-team-name"}).text
					cuotes = partit.div.find("div", {"class":"details-market market-0-runners"}).find("div", {"class":"runner-list"}).ul.findAll("li", {"class":"selection"})
					contador = 0
					for cuota in cuotes:
						if contador == 0:
							cuota1 = cuota.a.span.text
						else:
							cuota2 = cuota.a.span.text
						contador += 1
					if (cuota1.split()!=[] and cuota2.split()!=[]):
						writerCSV('Tennis', 'Betfair', checkNomsTennisDobles(getTeamName(equip1, "")), cuota1, checkNomsTennisDobles(getTeamName(equip2, "")), cuota2)
	except:
		printError('Betfair: Tennis Scraper Failed')	    
	
####WILLIAM####
def williamhillTennisScraper():
	try:
		file = open("htmls/williamhill/tennis.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		cuadres = bsObj.find("div", {"id":"contentCenter"}).find("div", {"id":"contentHolder"}).find("div", {"id":"contentA"}).find("div", {"id":"_sports_holder"}).div.div.findAll("div")
		cuadresLliga=[]
		for lliga in cuadres:
			if lliga.h3 is not None:
				cuadresLliga.append(lliga)
		for lliga in cuadresLliga:
			live = lliga.find("div").find("div").table.find("tbody").findAll("tr", {"class":"rowLive"})
			prematch = lliga.find("div").find("div").table.find("tbody").findAll("tr", {"class":"rowOdd"})
			alltr = live + prematch
			for tr in alltr:
				tds = tr.findAll("td", {"scope":"col"})
				cuota1 = tds[2].text.split()[0]
				cuota2 = tds[4].text.split()[0]
				noms = tds[3].text.split()
				equip1=""
				equip2=""
				notrobat = True
				for paraula in noms:
					if notrobat:
						if len(paraula)!=1:
							equip1 += paraula +" "
						else:
							notrobat=False
					
					else:
						equip2 += paraula +" "
				writerCSV('Tennis', 'William Hill', checkNomsTennisDobles(equip1), cuota1, checkNomsTennisDobles(equip2), cuota2)
	except:
		printError('William Hill: Tennis Scraper Failed')	
