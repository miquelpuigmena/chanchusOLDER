from utilsScraper import *
from writer import *

from bs4 import BeautifulSoup
import numbers
import json

def interwettenFutbolScraper():
	contador=0
	try:
		file = open("htmls/interwetten/futbol.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		lligues = bsObj.find("form").find("div", {"class":"pageroot"}).table.find("tr").find("td", {"class":"colmiddle"}).findAll("div", {"class":"bets shadow"})
		for lliga in lligues:
			try:
				if lliga.find('div', {'class':'header gradient headerContainer'}) != None:
					nomlligaInter = lliga.div.div.h1.text.encode('utf-8')  #Sport - Lliga
					acces = False
					nomlliga = ""
					for paraules in nomlligaInter:
						if paraules == '-':
							acces = True
						elif acces:
							nomlliga += paraules # Lliga
					even = lliga.table.findAll("tr", {"class":"even"})
					odd = lliga.table.findAll("tr", {"class":"odd"})
					for partits in even:
						equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
						acces = True
						for equip in equips:
							if equip == equips[0]:
								equip1 = equip.p.span.text.encode('utf-8')
								cuota1 = equip.p.strong.text
							elif equip == equips[1]:	
								cuotaX = equip.p.strong.text
							elif equip == equips[2]:
								equip2 = equip.p.span.text.encode('utf-8')
								cuota2 = equip.p.strong.text
								contador += 1
								writerCSV1x2('Futbol','Interwetten', equip2, equip1, replaceChar(cuota2, ',', '.'), replaceChar(cuotaX, ',', '.'), replaceChar(cuota1, ',', '.'), nomlliga)
					    		acces = False
					for partits in odd:
						equips = partits.find("td", {"class":"bets"}).table.tr.findAll("td")
						acces = True
						for equip in equips:
							if equip == equips[0]:
								equip1 = equip.p.span.text.encode('utf-8')
								cuota1 = equip.p.strong.text
							elif equip == equips[1]:	
								cuotaX = equip.p.strong.text
							elif equip == equips[2]:
								equip2 = equip.p.span.text.encode('utf-8')
								cuota2 = equip.p.strong.text
								contador += 1
								writerCSV1x2('Futbol','Interwetten', equip2, equip1, replaceChar(cuota2, ',', '.'), replaceChar(cuotaX, ',', '.'), replaceChar(cuota1, ',', '.'), nomlliga)
					    		acces = False
			except:
				pass
	except:
		printError('Interwetten: Futbol Scraper Failed')
	finally:
		print "Total partits de Interwetten: ",
		print contador
def betfairFutbolScraper():
	contador = 0
	try:
		file = open ('htmls/betfair/futbol.txt')
		bsObj = BeautifulSoup(file, "lxml")
		eventosnolast = bsObj.find("div", {"id":"zone-container"}).div.div.find("div", {"class":"grid-1 "}).div.findAll("div", {"class":"grid-1 "})[1].div.div.div.div.find("div", {"class":"updated-markets browse-all-container"}).div.find("ul", {"class":"section-list"}).findAll("li", {"class":"section"})[-1].find("ul", {"class":"event-list"}).findAll("li", {"class":"com-coupon-line avb-row market-1x2 large "})
		eventolast = bsObj.find("div", {"id":"zone-container"}).div.div.find("div", {"class":"grid-1 "}).div.findAll("div", {"class":"grid-1 "})[1].div.div.div.div.find("div", {"class":"updated-markets browse-all-container"}).div.find("ul", {"class":"section-list"}).findAll("li", {"class":"section"})[-1].find("ul", {"class":"event-list"}).findAll("li", {"class":"com-coupon-line avb-row market-1x2 large last"})
		eventos = eventosnolast + eventolast
		for  partit  in eventos:
			try:
				infopartit = partit.div
				caixetiDeCuotes = infopartit.find("div", {"class":"details-market market-0-runners"}).find("div", {"class":"runner-list"}).ul.findAll("li", {"class":"selection"})
				for cuota in caixetiDeCuotes:
					if cuota == caixetiDeCuotes[0]:
						cuota1 = cuota.a.span.text
					elif cuota == caixetiDeCuotes[1]:
						cuotaX = cuota.a.span.text
					elif cuota == caixetiDeCuotes[2]:
						cuota2 = cuota.a.span.text
				equip1 = infopartit.find("div", {"class":"details-event"}).find("div", {"class":"event-name-info"}).a.find("span", {"class":"home-team-name"}).text.encode('utf-8')
				equip2 = infopartit.find("div", {"class":"details-event"}).find("div", {"class":"event-name-info"}).a.find("span", {"class":"away-team-name"}).text.encode('utf-8')
				contador += 1
				writerCSV1x2('Futbol','Betfair', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), replaceChar(cuota1, ',', '.'), replaceChar(cuotaX, ',', '.'), replaceChar(cuota2, ',', '.'), 'No Definida')
			except:
				pass
	except:
		printError('Betafair: Futbol Scraper Failed')	
	finally:
		print "Total partits de Betfair: ",
		print contador

def marathonbetFutbolScraper():
	contador = 0
	try:
		file = open("htmls/marathonbet/futbol.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		lligues = bsObj.find("div", {"class":"container"}).find("div", {"id":"body_container"}).find("div", {"id":"main_container"}).div.find("div", {"class":"main-content"}).find("div", {"class":"pure-u-1-1"}).div.div.find("div", {"class":"events-container"}).div.find("div", {"class":"sport-category-content"}).findAll("div", {"data-filtered":"false"})
		for lliga in lligues:
			try:
				spanNom = lliga.table.find("tr", {"class":""}).find("td", {"class":"category-label-td"}).a.h2.findAll("span", {"class":"nowrap"})
				if len(spanNom) == 1:
					lliganom = spanNom[0].text.encode('utf-8')
				elif spanNom[0] != 'Women.':
					lliganom = spanNom[0].text.encode('utf-8')+spanNom[1].text.encode('utf-8')
				else:
					lliganom = spanNom[0].text.encode('utf-8')+spanNom[1].text.encode('utf-8')+spanNom[2].text.encode('utf-8')
				eventosbuit = lliga.find("div", {"class":"category-content"}).div.table.findAll("tbody", {"class":""})
				eventosbg = lliga.find("div", {"class":"category-content"}).div.table.findAll("tbody", {"class":"bg"})
				events = eventosbuit + eventosbg
				for event in events:
					cuotes = event.find("tr", {"class":" event-header"}).findAll("td", {"colspan":'2'})
					for cuota in cuotes:
						if cuota == cuotes[0]:
							cuota1 = cuota.span.text
						elif cuota == cuotes[1]:
							cuotaX = cuota.span.text
						else:
							cuota2 = cuota.span.text
					noms = event.find("tr", {"class":" event-header"}).find("td", {"data-mutable-id":"MRMAmainRow"}).table.findAll("tr", {"class":""})

					for nom in noms:
						if nom == noms[0]:
							equip1 = nom.findAll("td")[0].div.findAll("div")[0].span.text.encode('utf-8')
						elif nom == noms[1]:
							equip2 = nom.findAll("td")[0].div.findAll("div")[0].span.text.encode('utf-8')
					contador += 1
					writerCSV1x2('Futbol','Marathonbet', equip1, equip2, replaceChar(cuota1, ',', '.'), replaceChar(cuotaX, ',', '.'), replaceChar(cuota2, ',', '.'), replaceChar(lliganom, '.', ' '))
			except:
				pass	
	except:
		printError('Marathon Bet: Futbol Scraper Failed')
	finally:
		print "Total partits de Marathon Bet: ",
		print contador

def williamhillFutbolScraper():
	contador = 0
	try:
		file = open("htmls/williamhill/futbol.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")
		lligues = bsObj.find("div", {"id":"contentCenter"}).find("div", {"id":"contentHolder"}).find("div", {"id":"contentA"}).find("div", {"id":"dm_placeholder"}).find("div", {"id":"ip_sport_0"}).div.findAll("div")
		lliguesbones=[]
		for lliga in lligues:
			try:
				if lliga.find("div").div.table.find("tbody").find("tr", {"class":"rowOdd"}):
					lliguesbones.append(lliga)
			except:
				pass
		for lliga in lliguesbones:
			try:
				nomlliga = lliga.h3.text.encode('utf-8')
				partits = lliga.find("div").div.table.find("tbody").findAll("tr", {"class":"rowOdd"})
				for partit in partits:
					cuotesinom = partit.findAll("td", {"scope":"col"})
					cuota1 = cuotesinom[4].div.div.text
					cuotaX = cuotesinom[5].div.div.text
					cuota2 = cuotesinom[6].div.div.text
					nom = cuotesinom[2].a.span.text.split()
					acces = True
					equip1 = ""
					equip2 = ""
					for paraula in nom:
						try:
							if is_ascii(paraula):
								this = that###forzar error
							else:
								acces = False
						except:
							if acces:
								equip1 += paraula+" "
							else:
								equip2 += paraula+" "
					contador += 1
					writerCSV1x2('Futbol','William Hill', eraseSpaces(eraseSimbolsPrincipi(equip1)), eraseSpaces(eraseSimbolsPrincipi(equip2)), cuota1, cuotaX, cuota2, nomlliga)
			except:
				pass
	except:
		printError('William Hill: Futbol Scraper Failed')
	finally:
		print "Total partits de William Hill: ",
		print contador

def sportiumFutbolScraper():
	contador = 0
	try:
		try:
			file = open("htmls/sportium/futbol/albaniaaustriabelgica.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/brasilchinaczech.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/coreadelsursuecia.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/denmarkslovakiahonduras.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/england.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/finlandiaindiaindonesianorway.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/germany.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/italyfrance.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/japonrumaniasuiza.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/mixWorld.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/polandrusia.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/portugalholanda.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/scotland.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/spain.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/sportium/futbol/thailandturkeyamistoso.txt","r")
			bsObj = BeautifulSoup(file, "lxml")
			lligues = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment custom-type-coupon"}).findAll("div", {"class":"expander"})
			for lliga in lligues:
				try:
					nomlliga = eraseSpaces(lliga.h4.text)
					partits = lliga.find("div").div.table.findAll("tr",{"class":"mkt"})
					for partit in partits:
						selns = partit.findAll("td", {"class":"seln"})
						for seln in selns:
							if seln == selns[0]:
								cuota1 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip1 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = seln.div.button.span.find("span", {"class":"price dec"}).text
							else:
								cuota2 = seln.div.button.span.find("span", {"class":"price dec"}).text
								equip2 = seln.div.button.span.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Sportium', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, nomlliga)
				except:
					pass
		except:
			pass
	except:
		printError('Sportium: Futbol Scraper Failed')
	finally:
		print "Total partits de Sportium: ",
		print contador

###MARCAAPUESTAS###
def marcaapuestasFutbolScraper():
	contador = 0
	try:
		file = open('htmls/marcaapuestas/futbol.txt','r')
		bsObj = BeautifulSoup(file, "lxml")

		timegroup = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).find("div", {"class":"fragment calendar streaming-enabled"}).find("div", {"class":"results"}).div.findAll("div",{"class":"time-group"})
		for group in timegroup:
			try:
				partits = group.findAll("div", {"class":"event"})
				for partit in partits:
					tablepartit = partit.find("table", {"class":"horizontal"})
					if tablepartit != None:
						nomlligaFutbol = partit.find("div", {"class":"title"}).find("span", {"class":"ev-detail icon-FOOT"}).text.encode('utf-8').split()
						nomlliga = ""
						for paraula in nomlligaFutbol:
							if paraula != nomlligaFutbol[0] and paraula != nomlligaFutbol[1]:
								nomlliga += paraula+" "
						selns = tablepartit.find("tr").findAll("td",{"class":"seln"})
						for seln in selns:
							constant = seln.div.button.span
							if seln == selns[0]:
								cuota1 = constant.find("span", {"class":"price dec"}).text
								equip1 = constant.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
							elif seln == selns[1]:
								cuotaX = constant.find("span", {"class":"price dec"}).text
							else:
								cuota2 = constant.find("span", {"class":"price dec"}).text
								equip2 = constant.find("span", {"class":"seln-label"}).span.span.text.encode('utf-8')
						contador += 1
						writerCSV1x2('Futbol','Marca apuestas', eraseSimbolsPrincipi(equip1), eraseSimbolsPrincipi(equip2), cuota1, cuotaX, cuota2, replaceChar(nomlliga, '-', ''))
			except:
				pass
	except:
		printError('Marca Apuestas: Futbol Scraper Failed')
	finally:
		print "Total partits de Marca apuestas: ",
		print contador

def suertiaFutbolScraper():
	c = 0
	try:
		file = open("htmls/suertia/futbol.txt","r")
		bsObj = BeautifulSoup(file, "lxml")

		contenedor= bsObj.find("div", {"class":"uk-flex"}).find("article").find("div", {"class":"snc-middle-content uk-grid uk-grid-small"}).div.div.find("div",{"class":"uk-switcher-tab"}).findAll("div",{"class":"snc-bets-item"})
		for partido in contenedor:
			try:
				nomlligaSuertiaINFO = partido.find("div").find("div",{"class":"snc-odds-title uk-flex uk-flex-middle uk-flex-space-between"}).find("div",{"class":"snc-odd-event-bloc uk-flex uk-flex-column uk-flex-item-auto"}).find("div",{"class":"snc-event-breadcrumb"}).div.nav.findAll("a")[-1].text
				nomlligaSuertiaPAIS = partido.find("div").find("div",{"class":"snc-odds-title uk-flex uk-flex-middle uk-flex-space-between"}).find("div",{"class":"snc-odd-event-bloc uk-flex uk-flex-column uk-flex-item-auto"}).find("div",{"class":"snc-event-breadcrumb"}).div.nav.findAll("a")[-2].text
				nomlliga=nomlligaSuertiaPAIS+ " "
				for lletra in nomlligaSuertiaINFO:
					if lletra ==',':
						break
					nomlliga += lletra
		
				equipos = partido.find("div").find("div",{"class":"snc-odds-title uk-flex uk-flex-middle uk-flex-space-between"}).find("div",{"class":"snc-odd-event-bloc uk-flex uk-flex-column uk-flex-item-auto"}).find("div",{"class":"snc-event"}).a.text
				cuotas = partido.find("div").find("div",{"class":"snc-odds"}).findAll("div",{"class":"snc-odd odd0"})
				contador = 0
				for cuota in cuotas:
					if contador == 0:
						cuota1 = cuota.find("div",{"class":"odd-without-actor"}).find("a").text
					elif contador == 1:
						cuotaX = cuota.find("div",{"class":"odd-without-actor"}).find("a").text
					else:
						cuota2 = cuota.find("div",{"class":"odd-without-actor"}).find("a").text
					contador += 1

				match=separarEquipos(equipos, "/")
				c += 1
				writerCSV1x2("Futbol", "Suertia", match[1], match[0], replaceChar(cuota2, ',', '.'), replaceChar(cuotaX, ',', '.'), replaceChar(cuota1, ',', '.'), nomlliga)
			except:
				pass
	except:
		printError('Suertia: Baseball Scraper Failed')	
	finally:
		print "Total partits de Suertia: ",
		print c

####KIROLBET####
def kirolbetFutbolScraper():
	c = 0
	try:
		file = open("htmls/kirolbet/futbol.txt", "r")
		bsObj = BeautifulSoup(file, "lxml")

		partidos = bsObj.find("div", {"id":"container"}).find("div", {"id":"main-wrap"}).find("div", {"id":"main"}).div.find("div", {"class":"column center"}).div.find("div", {"id":"divFiltrosMarketsEvePrin"}).find("div", {"class":"prox_eventos"}).div.find("div", {"id":"divCat"}).find("div", {"style":"padding-top:10px"}).find("div", {"id":"EveList"}).find("ul").findAll("li", {"class":"filtroCategoria"})

		for partido in partidos:
			try:
				noms = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"partido"}).a.text #Team1 vs. Team2 <hora> (+mercats)
				lligaKirol = partido.find("div", {"class":"infoEve"}).find("div", {"class":None}).find("div", {"class":"info"}).p.find("span", {"class":"overStar"}).find("span", {"class":"campeonato"}).a.text.split()
				nomlliga=""
				for paraula in lligaKirol:
					if paraula[0] != '(': ##Paraules que no vull en el nom
						nomlliga += paraula+" "
				cuadresCuotes = partido.find("div", {"sport-type":"Eve"}).find("ul", {"des":"1X2"}).findAll("li", {"class":None})
				contador = 0
				for cuadre in cuadresCuotes:
					if contador == 0:
						cuota1 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
					elif contador == 1:
						cuotaX = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
					else:
						cuota2 = replaceChar(cuadre.a.p.find("span", {"class":"coef"}).text, ',', '.')
					contador += 1
					nomsVector = separarEquipos(noms, 'vs.')
					if len(nomsVector) == 1:
						nomsVector = separarEquipos(noms, '-')
				c += 1
				writerCSV1x2('Futbol', 'Kirolbet', getTeamName(getTeamName(nomsVector[1].lower(), '>'), '('), getTeamName(getTeamName(nomsVector[0].lower(), '>'), '('),  cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
	except:
		printError('Kirolbet: Baseball Scraper Failed')	
	finally:
		print "Total partits de Kirolbet: ",
		print c

####CODERE####
def codereFutbolScraper():
	c = 0
	try:
        #Argentina
		file = open("htmls/codere/futbol/argentina.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
					c += 1
					contador += 1	
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)

			except:
				pass
        #Belgica
        	file = open("htmls/codere/futbol/belgica.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
					c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #France
        	file = open("htmls/codere/futbol/france.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #Germany
        	file = open("htmls/codere/futbol/germany.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #holland
       		file = open("htmls/codere/futbol/holland.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #italy
        	file = open("htmls/codere/futbol/italy.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #Portugal
        	file = open("htmls/codere/futbol/portugal.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #spain
		file = open("htmls/codere/futbol/spain.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
        #usa
		file = open("htmls/codere/futbol/usa.json", "r")
		data_eventos = json.load(file)
		for data_evento in data_eventos:
			try:
				nomlliga = data_evento['LeagueName']
				info_equips = data_evento['Games'][0]['Results']
				contador = 0
				for info_equip in info_equips:
					if contador == 0:
						equip1 = info_equip['Name']
						cuota1 = info_equip['Odd']
					elif contador == 1:
						cuotaX = info_equip['Odd']
					else:
						equip2 = info_equip['Name']
						cuota2 = info_equip['Odd']
						c += 1
					contador += 1
				writerCSV1x2('Futbol', 'Codere', equip2, equip1, cuota2, cuotaX, cuota1, nomlliga)
			except:
				pass
	except:
		printError('Codere: Futbol Scraper Failed')	
	finally:
		print "Total partits de Codere: ",
		print c
###BET365###
def bet365FutbolScraper():
	c = 0
	try:
		##England
		try:
			file = open("htmls/bet365/futbol/england/premier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Premier League")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/england/championship.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Premier 2")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/england/leagueOnePremier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "League One")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/england/leagueTwoPremier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "League Two")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/england/nationalLeague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "National league")
					c+=1
				except:
					pass
		except:
			pass
		##Spain
		try:
			file = open("htmls/bet365/futbol/spain/laliga.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "La liga")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/spain/segunda.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Segunda division spain")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/spain/segundaB.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Segunda division B spain")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/spain/superligafemenina.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "superliga femenina spain")
					c+=1
				except:
					pass
		except:
			pass
		##Italy	
		try:
			file = open("htmls/bet365/futbol/italy/serieA.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "serie A italy")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/italy/serieB.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "serie B italy")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/italy/serieC.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "serie C italy")
					c+=1
				except:
					pass
		except:
			pass
		##Germany
		try:
			file = open("htmls/bet365/futbol/germany/bundesliga.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga Germany")
					c+=1
				except:
					pass
		except:
			pass

		try:
			file = open("htmls/bet365/futbol/germany/bundesliga2.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga 2 Germany")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/germany/bundesliga3.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga 3 Germany")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/germany/bundesligafem.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga woman Germany")
					c+=1
				except:
					pass
		except:
			pass
		##France
		try:
			file = open("htmls/bet365/futbol/france/ligue1.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue 1 France")
					c+=1
				except:
					pass
		except:
			pass

		try:
			file = open("htmls/bet365/futbol/france/ligue2.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue 2 France")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/france/liguenational.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue national France")
					c+=1
				except:
					pass
		except:
			pass
		##EuropeChamp
		try:
			file = open("htmls/bet365/futbol/europechamp/championsleague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Champions League")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/europechamp/championsleaguefem.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Champions League Woman")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/europechamp/europaleague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Europe League UEFA")
					c+=1
				except :
					pass
		except:
			pass
		##Championships
		try:
			file = open("htmls/bet365/futbol/championships/libertadores.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Copa Libertadores")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/championships/concacaf.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "CONCACAF")
					c+=1
				except :
					pass
		except:
			pass
		##World cup
		try:
			file = open("htmls/bet365/futbol/worldcup/europequal.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/worldcup/concacafqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/worldcup/conmebolqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/worldcup/cafqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		##America Leagues
		try:
			file = open("htmls/bet365/futbol/americaleagues/mexico.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "mexico")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/americaleagues/mls.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "MLS")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/americaleagues/costarica.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Costa rica")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/americaleagues/honduras.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "honduras")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/southamericaleague/brazil.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Brazil")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/southamericaleague/argentina.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Argentina")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/southamericaleague/peru.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Peru")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bet365/futbol/southamericaleague/colombia.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Colombia")
					c+=1
				except :
					pass
		except:
			pass
		##Asian
		try:
			file = open("htmls/bet365/futbol/asianleagues/japan.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bet365', hometeam, awayteam, homeodd, drawodd, awayodd, "Japan")
					c+=1
				except :
					pass
		except:
			pass
		
	except:
		printError('Bet365: Futbol Scraper Failed')	
	finally:
		print "Total partits de Bet365: ",
		print c

###BWIN###
def bwinFutbolScraper():
	c = 0
	try:
		##England
		try:
			file = open("htmls/bwin/futbol/england/premier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Premier League")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/england/championship.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Premier 2")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/england/leagueOnePremier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "League One")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/england/leagueTwoPremier.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "League Two")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/england/nationalLeague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "National league")
					c+=1
				except:
					pass
		except:
			pass
		##Spain
		try:
			file = open("htmls/bwin/futbol/spain/laliga.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "La liga")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/spain/segunda.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Segunda division spain")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/spain/segundaB.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Segunda division B spain")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/spain/superligafemenina.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "superliga femenina spain")
					c+=1
				except:
					pass
		except:
			pass
		##Italy	
		try:
			file = open("htmls/bwin/futbol/italy/serieA.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "serie A italy")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/italy/serieB.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "serie B italy")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/italy/serieC.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "serie C italy")
					c+=1
				except:
					pass
		except:
			pass
		##Germany
		try:
			file = open("htmls/bwin/futbol/germany/bundesliga.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga Germany")
					c+=1
				except:
					pass
		except:
			pass

		try:
			file = open("htmls/bwin/futbol/germany/bundesliga2.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga 2 Germany")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/germany/bundesliga3.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga 3 Germany")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/germany/bundesligafem.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Bundesliga woman Germany")
					c+=1
				except:
					pass
		except:
			pass
		##France
		try:
			file = open("htmls/bwin/futbol/france/ligue1.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue 1 France")
					c+=1
				except:
					pass
		except:
			pass

		try:
			file = open("htmls/bwin/futbol/france/ligue2.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue 2 France")
					c+=1
				except:
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/france/liguenational.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Ligue national France")
					c+=1
				except:
					pass
		except:
			pass
		##EuropeChamp
		try:
			file = open("htmls/bwin/futbol/europechamp/championsleague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Champions League")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/europechamp/championsleaguefem.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Champions League Woman")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/europechamp/europaleague.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Europe League UEFA")
					c+=1
				except :
					pass
		except:
			pass
		##Championships
		try:
			file = open("htmls/bwin/futbol/championships/libertadores.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Copa Libertadores")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/championships/concacaf.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "CONCACAF")
					c+=1
				except :
					pass
		except:
			pass
		##World cup
		try:
			file = open("htmls/bwin/futbol/worldcup/europequal.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/worldcup/concacafqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/worldcup/conmebolqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/worldcup/cafqual.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "world cup")
					c+=1
				except :
					pass
		except:
			pass
		##America Leagues
		try:
			file = open("htmls/bwin/futbol/americaleagues/mexico.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "mexico")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/americaleagues/mls.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "MLS")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/americaleagues/costarica.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Costa rica")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/americaleagues/honduras.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "honduras")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/southamericaleague/brazil.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Brazil")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/southamericaleague/argentina.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Argentina")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/southamericaleague/peru.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Peru")
					c+=1
				except :
					pass
		except:
			pass
		try:
			file = open("htmls/bwin/futbol/southamericaleague/colombia.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Colombia")
					c+=1
				except :
					pass
		except:
			pass
		##Asian
		try:
			file = open("htmls/bwin/futbol/asianleagues/japan.txt", "r")
			bsObj = BeautifulSoup(file, "lxml")
			store = bsObj.prettify()
			cuadreTopRight = bsObj.find("c", {"name":"Next 10"})
			odds = cuadreTopRight.findAll("tr", {"class":"odd"})
			even = cuadreTopRight.findAll("tr", {"class":"even"})
			partits = odds + even
			for partit in partits:
				try:
					hometeam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"home"}).text)
					awayteam = eraseSpaces(partit.find("td", {"class":"match"}).a.find("span", {"class":"away"}).text)
					homeodd = partit.find("td", {"class":"homeodds fixture"}).a.text.split()[0]
					drawodd = partit.find("td", {"class":"drawodds fixture"}).a.text.split()[0]
					awayodd = partit.find("td", {"class":"awayodds fixture"}).a.text.split()[0]
					writerCSV1x2('Futbol', 'Bwin', hometeam, awayteam, homeodd, drawodd, awayodd, "Japan")
					c+=1
				except :
					pass
		except:
			pass
		
	except:
		printError('Bwin: Futbol Scraper Failed')	
	finally:
		print "Total partits de Bwin: ",
		print c
