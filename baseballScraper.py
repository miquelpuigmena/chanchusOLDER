from utilsScraper import *
from writer import *

from bs4 import BeautifulSoup
import numbers
import json

##SPORTIUM##
def sportiumBaseballScraper():
	c = 0
	try:
		file = open("htmls/sportium/baseball.txt","r")
		bsObj = BeautifulSoup(file, "lxml")
		#fragments es el fragment central de la web
		fragments = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).findAll("div", {"class":"fragment"})
		#Separacio de lligues
		expanders = fragments[-1].findAll("div", {"class":"expander"})
		for expander in expanders:
			nomlliga = asciiError(eraseSimbolsPrincipi(expander.h4.text))
			alltr = expander.find("div", {"class":"expander-content"}).div.table.findAll("tr", {"class":"mkt"})
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
						c += 1
						writerCSVBaseball('Baseball','Sportium', equip1, cuota1, equip2, cuota2, nomlliga)
					acces = False
	except:
		printError('Sportium: Baseball Scraper Failed')
	finally:
		print "Total partits de Sportium: ",
		print c

###BETFAIR### nomes MLB!!
def betfairBaseballScraper():
	c = 0
	try:
		file = open ('htmls/betfair/baseball.txt')
		bsObj = BeautifulSoup(file, "lxml")
		dies = bsObj.find("div", {"id":"zone-container"}).div.div.find("div", {"class":"grid-1 "}).div.findAll("div", {"class":"grid-1 "})[1].div.div.div.div.find("div", {"class":"updated-markets browse-all-container"}).div.find("ul").findAll("li", {"class":"section"})
		for dia in dies:
			partits = dia.find("ul").findAll("li", {"class":"com-coupon-line-new-layout layout-7511 avb-row avb-table market-avb set-template market-3-columns"})

			for  partit  in partits:
				infopartit = partit.div
				caixetiDeCuotes = infopartit.find("div", {"class":"avb-col avb-col-markets"}).findAll("div", {"class":"details-market market-2-runners"})[-1]
				if (caixetiDeCuotes.find("div", {"class":"runner-list"}).find("span", {"class":"ui-market-status-message"}) == None):
					cuotes = caixetiDeCuotes.find("div", {"class":"runner-list"}).find("ul").findAll("li", {"class":"selection"})
					noms = infopartit.find("div", {"class":"avb-col avb-col-runners"}).div.a.div.findAll("span", {"class":"team-name"})
					contador = 0
					for nom in noms:
						if contador == 0:
							equip1 = getTeamName(nom.text, '(')
						elif contador == 1:
							equip2 = getTeamName(eraseSimbolsPrincipi(nom.text), '(')
						contador += 1
					contador = 0
					for cuota in cuotes:
						if contador == 0:
							cuota1 = cuota.a.span.text
						elif contador == 1:
							cuota2 = cuota.a.span.text
							c += 1
							writerCSVBaseball('Baseball', 'Betfair', equip1, cuota1, equip2, cuota2, 'MLB')
						contador += 1
			    
			#Ultim Partit del mercat
			partitlast = dia.find("ul").find("li", {"class":"com-coupon-line-new-layout layout-7511 avb-row avb-table  last market-avb set-template market-3-columns"})
			infopartit = partitlast.div
			caixetiDeCuotes = infopartit.find("div", {"class":"avb-col avb-col-markets"}).findAll("div", {"class":"details-market market-2-runners"})[-1]
			if (caixetiDeCuotes.find("div", {"class":"runner-list"}).find("span", {"class":"ui-market-status-message"}) == None):
				cuotes = caixetiDeCuotes.findAll("div")[-1].find("ul").findAll("li", {"class":"selection"})
				noms = infopartit.find("div", {"class":"avb-col avb-col-runners"}).div.a.div.findAll("span", {"class":"team-name"})
				contador = 0
				for nom in noms:
					if contador == 0:
						equip1 = getTeamName(nom.text, '(')
					elif contador == 1:
						equip2 = getTeamName(eraseSimbolsPrincipi(nom.text), '(')
					else:
						print "Error RARO en Betfair saveDatatoCSV"
					contador += 1
				contador = 0
				for cuota in cuotes:
					if contador == 0:
						cuota1 = cuota.a.span.text
					elif contador == 1:
						cuota2 = cuota.a.span.text
						c += 1
						writerCSVBaseball('Baseball', 'Betfair', equip1, cuota1, equip2, cuota2, 'MLB')
					else:
						print "Error RARO en Betfair saveDatatoCSV"
					contador += 1
	except:
		printError('Betafair: Baseball Scraper Failed')
	finally:
		print "Total partits de Betfair: ",
		print c

###MARCAAPUESTAS###
def marcaapuestasBaseballScraper():
	try:
		file = open('htmls/marcaapuestas/baseball.txt','r')
		bsObj = BeautifulSoup(file, "lxml")

		expanders = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div",{"class":"expander"})
		for expander in expanders:
			nomlliga = asciiError(eraseSimbolsPrincipi(expander.h4.text))
			eventos = expander.find("div").div.table.findAll("tr", {"class":"mkt"})
			for partits in eventos:
				equips = partits.findAll("td", {"class":"seln"})
				contador = 0
				for equip in equips:
					nomicuota = equip.div.find("button", {"class":"price"})
					if contador == 0:
						equip1 = nomicuota.find("span", {"class":"seln-label"}).span.span.text
						cuota1 = nomicuota.find("span", {"class":"price dec"}).text
					elif contador == 1:
						equip2 = nomicuota.find("span", {"class":"seln-label"}).span.span.text
						cuota2 = nomicuota.find("span", {"class":"price dec"}).text
						writerCSVBaseball('Baseball', 'Marca apuestas', equip1, cuota1, equip2, cuota2, nomlliga)
					contador += 1
	except:
		printError('Marca Apuestas: Baseball Scraper Failed')

####TIPBET#### Nomes MLB!
def tipbetBaseballScraper():
	c = 0
	try:
		file = open ("htmls/tipbet/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		eventos = bsObj.findAll("tbody", {"class":"match-line"})
		for event in eventos:
			noms = event.find("tr", {"class":"main-line"}).find("td", {"class":"col2 teams"}).span.text.split()
			cuota1 = event.find("tr", {"class":"main-line"}).find("td", {"class":"col4"}).span.text
			cuota2 = event.find("tr", {"class":"main-line"}).find("td", {"class":"col6"}).span.text
			acces = True
			equip1 = ""
			equip2 = ""
			for paraules in noms:
				if paraules == ":":
				        acces = False
				else: 
					if acces:
						equip1 += paraules+" "
					else:
						equip2 += paraules+" "
			c += 1
			writerCSVBaseball('Baseball','Tipbet', equip2, cuota2, equip1, cuota1, 'MLB')
	except:
		printError('Tipbet: Baseball Scraper Failed')	
	finally:
		print "Total partits de tip bet: ",
		print c

####INTERWETTEN####
def interwettenBaseballScraper():
	c = 0
	try:
		file = open("htmls/interwetten/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		lligues = bsObj.find("form").find("div", {"class":"pageroot"}).table.find("tr").find("td", {"class":"colmiddle"}).findAll("div", {"class":"bets shadow"})
		for lliga in lligues:
			if lliga.h2 != None:
				nomlligaInter = lliga.h2.span.span.text.split()  #Sport - Lliga
				acces = False
				nomlliga = ""
				for paraules in nomlligaInter:
					if paraules == '-':
						acces = True
					elif acces:
						nomlliga += paraules+ " " # Lliga
				even = lliga.table.findAll("tr", {"class":"even"})
				odd = lliga.table.findAll("tr", {"class":"odd"})
				for partits in even:
					equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
					acces = True
					for equip in equips:
						if acces:
							equip1 = equip.p.span.text.encode('utf-8')
							cuota1 = equip.p.strong.text
						else:
							equip2 = equip.p.span.text.encode('utf-8')
							cuota2 = equip.p.strong.text
							c += 1
							writerCSVBaseball('Baseball','Interwetten', equip2, replaceChar(cuota2, ',', '.'), equip1, replaceChar(cuota1, ',', '.'), nomlliga)
				    		acces = False
				for partits in odd:
					equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
					acces = True
					for equip in equips:
						if acces:
							equip1 = equip.p.span.text.encode('utf-8')
							cuota1 = equip.p.strong.text
						else:
							equip2 = equip.p.span.text
							cuota2 = equip.p.strong.text.encode('utf-8')
							c += 1
							writerCSVBaseball('Baseball','Interwetten', equip2, replaceChar(cuota2, ',', '.'), equip1, replaceChar(cuota1, ',', '.'), nomlliga)
						acces = False
	except:
		printError('Interwetten: Baseball Scraper Failed')
	finally:
		print "Total partits de Interwetten: ",
		print c
###BET365###
def bwinBaseballScraper():
	c = 0
	try:
		file = open("htmls/bwin/baseball/MLB.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		store = bsObj.prettify()
		file = open("store.txt", "w")
		file.write(store.encode("utf-8"))
		file.close()
		cuadreTopRight = bsObj.find("table", {"class":"normaltable nextx"})
		odds = cuadreTopRight.findAll("tr", {"class":"odd"})
		even = cuadreTopRight.findAll("tr", {"class":"even"})
		partits = odds + even
		for partit in partits:
			hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
			awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
			homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
			awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
			writerCSVBaseball('Baseball', 'Bwin', hometeam, homeodd, awayteam, awayodd, "MLB")
			c+=1
	except:
		printError('Bwin: Baseball Scraper Failed')	
	finally:
		print "Total partits de Bwin: ",
		print c
'''
####BWIN####
def bwinBaseballScraper():
	c = 0
	try:
		file = open("htmls/bwin/baseball.txt","r")
		bsObj = BeautifulSoup(file, "lxml")
		cuadreSeparatDies = bsObj.find("div", {"class":"container"}).find("div", {"id":"plugin-wrapper"}).find("div", {"id":"main-wrap"}).div.find("div", {"class":"center "}).div.find("div", {"id":"markets-container"}).div.findAll("div", {"class", "ui-widget-content"})
		for dies in cuadreSeparatDies:
			lligues = dies.find("div", {"class":"ui-widget-content-body"}).div.div.div.find("div").findAll("div", {"class":"marketboard-event-group__item--sub-group"})
			for lliga in lligues:
				nomlligaBwin = lliga.find("h2").find("span").a.text.split()
				nomlliga=""
				for paraula in nomlligaBwin:
					if paraula == '-':
						break
					nomlliga += paraula+" "
				partits = lliga.find("div", {"class":"marketboard-event-group__item-container marketboard-event-group__item-container--level-3"}).findAll("div", {"class":"marketboard-event-group__item--event"})
				for partit in partits:
					equips = partit.find("div", {"class":"marketboard-event-with-header"}).find("div", {"class":"marketboard-event-with-header__markets-container"}).table.tr.findAll("td")
					acces = True
					for equip in equips:
						button = equip.find("button")
						nom = button.find("div", {"class":"mb-option-button__option-name mb-option-button__option-name--odds-4"}).text.encode('utf-8')
						cuota = button.find("div", {"class":"mb-option-button__option-odds "}).text
						if acces:
							equip1 = nom
							cuota1 = cuota
						else:
							equip2 = nom
							cuota2 = cuota
							c += 1
							writerCSVBaseball('Baseball','Bwin', equip1, cuota1, equip2, cuota2, nomlliga)
						acces = False
	except:
		printError('Bwin: Baseball Scraper Failed')	
	finally:
		print "Total partits de Bwin: ",
		print c

'''
####SUERTIA####
def suertiaBaseballScraper():
	c = 0
	try:
		file = open("htmls/suertia/baseball.txt","r")
		bsObj = BeautifulSoup(file, "lxml")

		contenedor= bsObj.find("div", {"id":"main"}).find("article").find("div", {"class":"snc-middle-content uk-grid uk-grid-small"}).div.div.find("div", {"class":"uk-switcher"}).find("div",{"class":"uk-switcher-tab"}).findAll("div",{"class":"snc-bets-item"})

		for partido in contenedor:
			nomlligaSuertia = partido.find("div").find("div",{"class":"snc-odds-title uk-flex uk-flex-middle uk-flex-space-between"}).find("div",{"class":"snc-odd-event-bloc uk-flex uk-flex-column uk-flex-item-auto"}).find("div",{"class":"snc-event-breadcrumb"}).div.nav.findAll("a")[-1].text
			nomlliga=""
			for lletra in nomlligaSuertia:
				if lletra ==',':
					break
				nomlliga += lletra
			
			equipos = partido.find("div").find("div",{"class":"snc-odds-title uk-flex uk-flex-middle uk-flex-space-between"}).find("div",{"class":"snc-odd-event-bloc uk-flex uk-flex-column uk-flex-item-auto"}).find("div",{"class":"snc-event"}).a.text
			cuotas = partido.find("div").find("div",{"class":"snc-odds"}).findAll("div",{"class":"snc-odd odd0"})
			contador = 0
			for cuota in cuotas:
				if contador == 0:
					cuota1 = cuota.find("div",{"class":"odd-without-actor"}).find("a").text
				else:
					cuota2 = cuota.find("div",{"class":"odd-without-actor"}).find("a").text
				contador += 1

			match=separarEquipos(equipos, "/")
			c += 1
			writerCSVBaseball("Baseball", "Suertia", match[1], replaceChar(cuota2, ',', '.'), match[0], replaceChar(cuota1, ',', '.'), nomlliga)
	except:
		printError('Suertia: Baseball Scraper Failed')	
	finally:
		print "Total partits de Suertia: ",
		print c

####WILLIAM#### nomes MLB!
def williamhillBaseballScraper():
	c = 0
	try:
		file = open("htmls/williamhill/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		cuadrePartits = bsObj.find("div", {"id":"contentCenter"}).find("div", {"id":"contentHolder"}).find("div", {"id":"contentA"}).find("div", {"id":"_sports_holder"}).div.div.find("div", {"id":"ip_type_226"}).findAll("div", {"id":"ip_type_226_mkt_grps"})

		cuadresbons = []
		for cuadre in cuadrePartits:
			reconeixerPartits = cuadre.find("div").table.find("thead").tr.find("th", {"class":"leftPad"}).span.text.split()[0]

			if ((reconeixerPartits == "Apuestas")|(reconeixerPartits == "MLB")):
				cuadresbons.append(cuadre)

		for cuadre in cuadresbons:
			contador = 0
			partitsPerEquip = cuadre.div.table.find("tbody").findAll("tr")
			contadorIntern = 0
			for partit in partitsPerEquip:
				infopartit = partit.findAll("td")
				if (infopartit[3].text.split() != []):
					if contadorIntern != 0:
						if ((contador > 0)|(len(cuadresbons) == 1)):
							if contadorIntern%2 == 1:
								equip1 = getTeamName(infopartit[2].text.encode('utf-8'), '(')
								cuota1 = infopartit[3].text.split()[0]

							elif contadorIntern%2 == 0:
								equip2 = getTeamName(infopartit[2].text.encode('utf-8'), '(')
								cuota2 = infopartit[3].text.split()[0]
								c += 1
								writerCSVBaseball('Baseball','William Hill', equip1, cuota1, equip2, cuota2, 'MLB')
						elif contador==0:
							cuota1 = infopartit[3].text.split()[0]
							equipsnom = (infopartit[4].text.encode('utf-8')).split()
							equip1 = ""
							equip2 = ""
							acces1 = True
							for paraula in equipsnom:
								if paraula == ":":
									acces1 = False
								if acces1:
									equip1 += paraula +" "
								else:
									equip2 += paraula +" "
							cuota2 = infopartit[5].text.split()[0]
							c += 1
							writerCSVBaseball('Baseball','William Hill', equip1, cuota1, equip2, cuota2, 'MLB')
					contadorIntern += 1
			contador += 1
	except:
		printError('William Hill: Baseball Scraper Failed')	
	finally:
		print "Total partits de William Hill: ",
		print c

####CODERE####
def codereBaseballScraper():
	c = 0
	try:
		file = open("htmls/codere/baseball.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			nomlliga = data_evento['LeagueName']
			info_equips = data_evento['Games'][0]['Results']
			contador = 0
			for info_equip in info_equips:
				if contador == 0:
					equip1 = info_equip['Name']
					cuota1 = info_equip['Odd']
				else:
					equip2 = info_equip['Name']
					cuota2 = info_equip['Odd']
					c += 1
					writerCSVBaseball('Baseball', 'Codere', equip2, cuota2, equip1, cuota1, nomlliga)
				contador += 1	
	except:
		printError('Codere: Baseball Scraper Failed')	
	finally:
		print "Total partits de Codere: ",
		print c

	
####BETSTARS####
def betstarsBaseballScraper():
	c = 0
	try:
		file = open("htmls/betstars/baseball.json", "r")
		data_lligues = json.load(file)
		#eventos_prematch = data_eventos['prematch']['event']
		for lliga in data_lligues:
			nomlliga = lliga['name']
			eventos_prematch = lliga['event']
			for evento_prematch in eventos_prematch:
				cuotesinoms = evento_prematch['markets'][0]['selection']
				contador = 0
				for cuota in cuotesinoms:
					if contador == 0:
						cuota1 = cuota['odds']['dec']
						equip1 = cuota['name']
					else:
						cuota2 = cuota['odds']['dec']
						equip2 = cuota['name']
						c += 1
						writerCSVBaseball('Baseball', 'Betstars', equip1, cuota1, equip2, cuota2, nomlliga)
					contador += 1
	except:
		printError('Bet Stars: Baseball Scraper Failed')	
	finally:
		print "Total partits de Bet stars: ",
		print c


####KIROLBET####
def kirolbetBaseballScraper():
	c = 0
	try:
		file = open("htmls/kirolbet/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		partidos = bsObj.find("div", {"id":"container"}).find("div", {"id":"main-wrap"}).find("div", {"id":"main"}).div.find("div", {"class":"column center"}).div.find("div", {"id":"divFiltrosMarketsEvePrin"}).find("div", {"class":"prox_eventos"}).div.find("div", {"id":"divCat"}).find("div", {"style":"padding-top:10px"}).find("div", {"id":"EveList"}).find("ul").findAll("li", {"class":"filtroCategoria"})

		for partido in partidos:
			noms = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"partido"}).a.text #Team1 vs. Team2 <hora> (+mercats)
			lligaKirol = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"overStar"}).find("span", {"class":"campeonato"}).a.text.split()
			nomlliga=""
			for paraula in lligaKirol:
				if paraula!= 'USA': ##Paraules que no vull en el nom
					nomlliga += paraula+" "
			cuadresCuotes = partido.find("div", {"sport-type":"Eve"}).find("ul", {"des":"Ganador"}).findAll("li", {"class":"pronos2"})
			contador = 0
			for cuadre in cuadresCuotes:
				if contador == 0:
					cuota1 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
				else:
					cuota2 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
				contador += 1
			nomsVector = separarEquipos(getTeamName(getTeamName(noms, '<'), '('), 'vs.')
			c += 1
			writerCSVBaseball('Baseball', 'Kirolbet', nomsVector[1], cuota2, nomsVector[0], cuota1, nomlliga)
	except:
		printError('Kirolbet: Baseball Scraper Failed')	
	finally:
		print "Total partits de Kirolbet: ",
		print c



####JUEGGING####
def jueggingBaseballScraper():
	c = 0
	try:
		file = open("htmls/juegging/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		partidos = bsObj.find("div", {"id":"container"}).find("div", {"id":"main-wrap"}).find("div", {"id":"main"}).div.find("div", {"class":"column center"}).div.find("div", {"id":"divFiltrosMarketsEvePrin"}).find("div", {"class":"prox_eventos"}).div.find("div", {"id":"divCat"}).find("div", {"style":"padding-top:10px"}).find("div", {"id":"EveList"}).find("ul").findAll("li", {"class":"filtroCategoria"})

		for partido in partidos:
			noms = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"partido"}).a.text #Team1 vs. Team2 <hora> (+mercats)
			lligaJuegging = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"overStar"}).find("span", {"class":"campeonato"}).a.text.split()
			nomlliga=""
			for paraula in lligaJuegging:
				if paraula!= 'USA': ##Paraules que no vull en el nom
					nomlliga += paraula+" "
			cuadresCuotes = partido.find("div", {"sport-type":"Eve"}).find("ul", {"des":"Ganador"}).findAll("li", {"class":"pronos2"})
			contador = 0
			for cuadre in cuadresCuotes:
				if contador == 0:
					cuota1 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
				else:
					cuota2 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
				contador += 1
			nomsVector = separarEquipos(getTeamName(getTeamName(noms, '<'), '('), 'vs.')
			c += 1
			writerCSVBaseball('Baseball', 'Juegging', nomsVector[1], cuota2, nomsVector[0], cuota1, nomlliga)
	except:
		printError('Juegging: Baseball Scraper Failed')	
	finally:
		print "Total partits de Juegging: ",
		print c

####MARATHON BET####
def marathonbetBaseballScraper():
	c = 0
	try:
		file = open("htmls/marathonbet/baseball.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		lligues = bsObj.find("div", {"class":"container"}).find("div", {"id":"body_container"}).find("div", {"id":"main_container"}).div.find("div", {"class":"main-content"}).find("div", {"class":"pure-u-1-1"}).div.div.find("div", {"class":"events-container"}).div.find("div", {"class":"sport-category-content"}).findAll("div", {"class":"category-container"})
		for lliga in lligues:
			spanNom = lliga.table.find("tr").find("td", {"class":"category-label-td"}).a.h2.findAll("span")
			if len(spanNom) == 1:
				nomlliga = spanNom[0].text
			else:
				if spanNom[1].text != 'Triple-A.':
					nomlliga = spanNom[1].text
				else:
					nomlliga = spanNom[2].text
			eventosbuit = lliga.find("div", {"class":"category-content"}).div.table.findAll("tbody", {"class":""})
			eventosbg = lliga.find("div", {"class":"category-content"}).div.table.findAll("tbody", {"class":"bg"})
			events = eventosbuit + eventosbg
			for event in events:
				cuota1 = event.find("tr", {"class":" event-header"}).find("td", {"class":"price height-column-with-price    first-in-main-row  "}).span.text
				cuota2 = event.find("tr", {"class":" event-header"}).find("td", {"class":"price height-column-with-price    "}).span.text
				noms = event.find("tr", {"class":" event-header"}).find("td", {"class":"first member-area   "}).table.findAll("tr")
				contador = 0
				for nom in noms:
					if contador == 0:
						equip1 = nom.find("td").div.find("div").span.text
					else:
						equip2 = nom.find("td").div.find("div").span.text	
					contador += 1
				c += 1
				writerCSVBaseball('Baseball', 'Marathonbet', getTeamName(equip1, '('), cuota1, getTeamName(equip2, '('), cuota2, nomlliga)
	except:
		printError('Marathon Bet: Baseball Scraper Failed')
	finally:
		print "Total partits de Marathon bet: ",
		print c

####PAF####
def pafBaseballScraper():
	c = 0
	try:
		file = open("htmls/paf/baseball.json", "r")
		data_eventos = json.load(file)

		eventos = data_eventos['events']
		for evento in eventos:
			nomlliga = evento['event']['group']
			equip1 = evento['event']['homeName']
			equip2 = evento['event']['awayName']
			cuotes = evento['betOffers'][0]['outcomes']
			contador = 0
			for cuota in cuotes:
				if contador == 0:
					acces = True	
					cuota1fraccio = separarEquipos(cuota['oddsFractional'], '/')
					if cuota1fraccio[0] == 'Evens':
						cuota1 = 2
						acces = False
					if acces:
						cuota1 = (float(cuota1fraccio[0])/float(cuota1fraccio[1]))+1
				else:
					acces = True
					cuota2fraccio = separarEquipos(cuota['oddsFractional'], '/')
					if cuota2fraccio[0] == 'Evens':
						cuota2 = 2
						acces = False
					if acces:
						cuota2 = (float(cuota2fraccio[0])/float(cuota2fraccio[1]))+1
				contador += 1
			c += 1
			writerCSVBaseball('Baseball', 'Paf', equip2, cuota2, equip1, cuota1, nomlliga)
	except:
		printError('Paf: Baseball Scraper Failed')	
	finally:
		print "Total partits de Paf: ",
		print c

###WANABET###
def wanabetBaseballScraper():
	c = 0
	try:
		file = open("htmls/wanabet/baseball.json", "r")
		data_eventos = json.load(file)

		eventos = data_eventos['events']
		for evento in eventos:
			nomlliga = evento['event']['path'][-1]['name']
			equip1 = evento['event']['homeName']
			equip2 = evento['event']['awayName']
			cuotes = evento['betOffers'][0]['outcomes']
			contador = 0
			for cuota in cuotes:
				if contador == 0:
					acces = True	
					cuota1fraccio = separarEquipos(cuota['oddsFractional'], '/')
					if cuota1fraccio[0] == 'Evens':
						cuota1 = 2
						acces = False
					if acces:
						cuota1 = (float(cuota1fraccio[0])/float(cuota1fraccio[1]))+1
				else:
					acces = True
					cuota2fraccio = separarEquipos(cuota['oddsFractional'], '/')
					if cuota2fraccio[0] == 'Evens':
						cuota2 = 2
						acces = False
					if acces:
						cuota2 = (float(cuota2fraccio[0])/float(cuota2fraccio[1]))+1
				contador += 1
			c += 1
			writerCSVBaseball('Baseball', 'Wanabet', equip2, cuota2, equip1, cuota1, nomlliga)
	except:
		printError('Wanabet: Baseball Scraper Failed')	
	finally:
		print "Total partits de Wanabet: ",
		print c

###GOLDENPARK###
def goldenparkBaseballScraper():
	c = 0
	try:
		file = open("htmls/goldenpark/baseballmlb.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		if bsObj.marketgroups is not None:
			markets = bsObj.marketgroups.marketgroup.markets.findAll("market")
			for market in markets:
				cuotesinoms = market.selections
				contador = 0
				for cuotainom in cuotesinoms:
					if contador == 0:
						equip1 = getTeamName(cuotainom.find("name").text, '(')
						cuota1 = (float(cuotainom.find("currentpriceup").text)/float(cuotainom.find("currentpricedown").text))+1
					else:
						equip2 = getTeamName(cuotainom.find("name").text, '(')
						cuota2 = (float(cuotainom.find("currentpriceup").text)/float(cuotainom.find("currentpricedown").text))+1
						c += 1
						writerCSVBaseball('Baseball', 'Goldenpark', equip2, cuota2, equip1, cuota1, 'MLB')
					contador += 1

		file = open("htmls/goldenpark/baseballlmb.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		if bsObj.marketgroups is not None:
			markets = bsObj.marketgroups.marketgroup.markets.findAll("market")
			for market in markets:
				cuotesinoms = market.selections
				contador = 0
				for cuotainom in cuotesinoms:
					if contador == 0:
						equip1 = getTeamName(cuotainom.find("name").text, '(')
						cuota1 = (float(cuotainom.find("currentpriceup").text)/float(cuotainom.find("currentpricedown").text))+1
					else:
						equip2 = getTeamName(cuotainom.find("name").text, '(')
						cuota2 = (float(cuotainom.find("currentpriceup").text)/float(cuotainom.find("currentpricedown").text))+1
						c += 1
						writerCSVBaseball('Baseball', 'Goldenpark', equip2, cuota2, equip1, cuota1, 'Liga Mexicana')
					contador += 1
	except:
		printError('Golden Park: Baseball Scraper Failed')	
	finally:
		print "Total partits de Golden Park: ",
		print c



###BET365###
def bet365BaseballScraper():
	c = 0
	try:
		file = open("htmls/bet365/baseball/MLB.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		store = bsObj.prettify()
		file = open("store.txt", "w")
		file.write(store.encode("utf-8"))
		file.close()
		cuadreTopRight = bsObj.find("table", {"class":"normaltable nextx"})
		odds = cuadreTopRight.findAll("tr", {"class":"odd"})
		even = cuadreTopRight.findAll("tr", {"class":"even"})
		partits = odds + even
		for partit in partits:
			hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
			awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
			homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
			awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
			writerCSVBaseball('Baseball', 'Bet365', hometeam, homeodd, awayteam, awayodd, "MLB")
			c+=1
	except:
		printError('Bet365: Baseball Scraper Failed')	
	finally:
		print "Total partits de Bet365: ",
		print c
