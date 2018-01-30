###Extreu Dades en Html: Interwetten, Betfair, WilliamHill, Sportium, Bwin, Tipbet, Marcaapuestas, Suertia, KirolBet, juegging, MarathonBet, GoldenPark
###Extreu dades en json: Codere, BetStars, Paf, Wanabet

import requests
from utilsScraper import getFecha, getRandomNumber

def escriureArxiu(url, where):
	response = requests.get(url)
	file = open (where, "w")
	file.write(response.text.encode("utf-8"))
	file.close()

def printWhatDoing(sport, casa):
	print "[Actualitzant "+sport+" de "+casa+"]\r"

def writeBaseball():
	###################GET INTERWETTEN
	#Baseball
	printWhatDoing('BASEBALL', 'Interwetten')
	escriureArxiu("https://www.interwetten.es/en/sportsbook/betting/bettingoffer.aspx?leagueid=14233,406176&type=0&ogPreselect=1", 'htmls/interwetten/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Interwetten')
	escriureArxiu("https://www.interwetten.es/es/apuestas-deportivas/top-leagues?topLinkId=15", 'htmls/interwetten/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Interwetten')
	escriureArxiu("https://www.interwetten.es/en/sportsbook/betting/bettingoffer.aspx?leagueid=10410,105120,405615,10659,1019,1020,405932,10347,406747,105325,406748,405432,10268,405907,1021,1022,10467,10468,10691,405369,405368,1091,1029,405298,407902,405355,407636,1030,105034,405449,405450,405451,405452,10523,1024,10617,405434,10416,1081,1025,105002,1023,10900,406244,405718,405871,1026,10605,405266,10607,10598,10269,1027,10448,1028,1036,405290,1060,405435,10412,405677,406000,407737,406341,1035,105225,408279,10235,10208,406338,10400,408612,408667,406245,408613,408665,408280,10293,405403,406344,10420,406007,408287,408286,405859,405281,10306,405364,405622,405931,1059,406254,406081,406174,405541,406539,406754,405920,405911,405618,405357,10909,10424,405899,10618,406281,406517,10750,406331,105121,405525,408709,405526,406935,405250,406106,407689,406296,406550,405416,406551,405415,407807,405440,406291,406569,10148,405394,407224,405773,406817,408571,406265,406379,406573,406588,406478,406314,406317,406373,406310,406210,406243,406251,405947,406949,406638,10405,408047,408157,407681,407751,406388,406847,405706,406567,105379,407984&type=0&ogPreselect=0", 'htmls/interwetten/futbol.txt')

	print "==========INTERWETTEN SCRAPED=========="
	print
	###################GET BETFAIR
	#Baseball
	printWhatDoing('BASEBALL', 'Betfair')
	escriureArxiu("https://www.betfair.es/sport/baseball", 'htmls/betfair/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Betfair')
	escriureArxiu("https://www.betfair.es/sport/tennis?action=loadCompetition&modules=multipickavbId@1059&selectedTabType=TODAY", 'htmls/betfair/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Betfair')
	escriureArxiu("https://www.betfair.es/sport/football", 'htmls/betfair/futbol.txt')
	print "==========BETFAIR SCRAPED=========="
	print
	###################GET WILLIAMHILL
	#Baseball
	printWhatDoing('BASEBALL', 'William Hill')
	escriureArxiu("http://sports.williamhill.es/bet_esp/es/betting/y/2/mh/B%C3%A9isbol.html", 'htmls/williamhill/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'William Hill')
	escriureArxiu("http://sports.williamhill.es/bet_esp/es/betting/y/17/mh/Tenis.html", 'htmls/williamhill/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'William Hill')
	escriureArxiu("http://sports.williamhill.es/bet_esp/es/betting/y/5/tm/0/F%C3%BAtbol.html", 'htmls/williamhill/futbol.txt')

	print "==========WILLIAM HILL SCRAPED=========="
	print
	###################GET SPORTIUM 
	#Baseball
	printWhatDoing('BASEBALL', 'Sportium')
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=38323-38389-38427-38548", 'htmls/sportium/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Sportium')
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=38631-43932", 'htmls/sportium/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Sportium')
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=43605-44009-45223-45225", 'htmls/sportium/futbol/mixWorld.txt')##mix
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=45211-45213-45215-45217-45218", 'htmls/sportium/futbol/spain.txt')##spain
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=40527-40542-40602-40606-40623", 'htmls/sportium/futbol/england.txt')##england
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=45915-45935-45942-45985-45986", 'htmls/sportium/futbol/gemany.txt')##germany
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=44561-44571-46074-46075-46087", 'htmls/sportium/futbol/italyfrance.txt')##italy, france
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=43084-43094-44977-44979-44997", 'htmls/sportium/futbol/portugalholanda.txt')##portugal, holanda
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=40700-41277-41284-41984-42039", 'htmls/sportium/futbol/albaniaaustriabelgica.txt')##albany, austria, belgium
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=39217-39951-40037-42382-42429", 'htmls/sportium/futbol/brasilchinaczech.txt')##brasil, china, czech
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=39490-39496-39511-45281-45873", 'htmls/sportium/futbol/denmarkslovakiahonduras.txt')##denmark, slovakia, honduras
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=44821-44823-44827-44836-44837", 'htmls/sportium/futbol/scotland.txt')##scotland
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=42853-44280-44304-46095-46096", 'htmls/sportium/futbol/finlandiaindiaindonesianorway.txt')##finlandia, india, indonesia, norway
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=44493-44500-44501-44743-44947", 'htmls/sportium/futbol/japonrumaniasuiza.txt')##japon, rumania, suiza
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=45072-45080-45097-45128-45241", 'htmls/sportium/futbol/polandrusia.txt')##poland, rusia
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=44893-44897-45008-45012-45013", 'htmls/sportium/futbol/coreadelsursuecia.txt')##korea, sweden
	escriureArxiu("http://sports.sportium.es/es/type-coupon?sb_type_ids=44674-44718-46162", 'htmls/sportium/futbol/thailandturkeyamistoso.txt')##thai, turkey, friendly
	print "==========SPORTIUM SCRAPED=========="
	print

	###################GET BWIN
	#Baseball
	printWhatDoing('BASEBALL', 'Bwin')
	escriureArxiu("https://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=de&clientid=475&state=2_3,3_16,22_2,5_38836,9_overview", 'htmls/bwin/baseball/MLB.txt')
	

	#Futbol
	printWhatDoing('FUTBOL', 'Bwin')
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_1%2C22_1%2C5_40942%2C9_summary", 'htmls/bwin/futbol/england/premier.txt') #Premier
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_1%2C22_1%2C5_41266%2C9_summary", 'htmls/bwin/futbol/england/championship.txt') #Premier 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_1,22_1,5_41268,9_summary", 'htmls/bwin/futbol/england/leagueOnePremier.txt') #League One
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_1,22_1,5_41270,9_summary", 'htmls/bwin/futbol/england/leagueTwoPremier.txt') #League two
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_1,22_1,5_41868,9_summary", 'htmls/bwin/futbol/england/nationalLeague.txt') #National League
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_32,22_1,5_42556,9_summary", 'htmls/bwin/futbol/spain/laliga.txt') #La liga
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_32,22_1,5_42560,9_summary", 'htmls/bwin/futbol/spain/segunda.txt') #Segunda
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_32%2C22_1%2C5_42826%2C9_overview", 'htmls/bwin/futbol/spain/segundaB.txt') #Segunda B
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_32%2C22_1%2C5_44414%2C9_summary", 'htmls/bwin/futbol/spain/superligafemenina.txt') #Fem Spain
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_42720%2C9_summary", 'htmls/bwin/futbol/italy/serieA.txt') #Serie A
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_43004%2C9_summary", 'htmls/bwin/futbol/italy/serieB.txt') #Serie B
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_43730%2C9_overview", 'htmls/bwin/futbol/italy/serieC.txt') #Serie C
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41576%2C9_summary", 'htmls/bwin/futbol/germany/bundesliga.txt') #Bundesliga
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41578%2C9_summary", 'htmls/bwin/futbol/germany/bundesliga2.txt') #Bundesliga 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41808%2C9_summary", 'htmls/bwin/futbol/germany/bundesliga3.txt') #Bundesliga 3
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_42724%2C33_122%2C9_summary", 'htmls/bwin/futbol/germany/bundesligafem.txt') #Bundesliga Fem
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_40958%2C9_summary", 'htmls/bwin/futbol/france/ligue1.txt') #Ligue 1
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_40960%2C9_summary", 'htmls/bwin/futbol/france/ligue1.txt') #Ligue 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_42786%2C9_summary", 'htmls/bwin/futbol/france/liguenational.txt') #Ligue National
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_41198%2C9_overview", 'htmls/bwin/futbol/championships/championsleague.txt') #Champ. league
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_43378%2C9_overview", 'htmls/bwin/futbol/championships/championsleague.txt') #Champ. league Woman
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_41238%2C9_overview", 'htmls/bwin/futbol/championships/europaleague.txt') #Europe league
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_393%2C22_3%2C5_38534%2C9_overview", 'htmls/bwin/futbol/championships/libertadores.txt') #Libertadores
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_393%2C22_2%2C5_33229%2C9_overview", 'htmls/bwin/futbol/championships/concacaf.txt') #Concacaf
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_4%2C22_1%2C5_10876%2C9_overview", 'htmls/bwin/futbol/worldcup/europequal.txt') #uefa qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_4%2C22_2%2C5_10080%2C9_overview", 'htmls/bwin/futbol/worldcup/concacafqual.txt') #concacaf qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_4%2C22_3%2C5_10872%2C9_summary", 'htmls/bwin/futbol/worldcup/conmebolqual.txt') #conmebol qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_4%2C22_4%2C5_10878%2C9_overview", 'htmls/bwin/futbol/worldcup/cafqual.txt') #caf qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_12%2C22_2", 'htmls/bwin/futbol/americaleagues/mexico.txt') #mexico
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_26%2C22_2%2C5_38738%2C9_overview", 'htmls/bwin/futbol/americaleagues/mls.txt') #MLS
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_289%2C22_2%2C5_42756%2C9_summary", 'htmls/bwin/futbol/americaleagues/costarica.txt') #Costa Rica
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1%2C3_437%2C22_2%2C5_42782%2C9_summary", 'htmls/bwin/futbol/americaleagues/honduras.txt') #Honduras
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_13,22_3", 'htmls/bwin/futbol/southamericaleague/brazil.txt') #Brazil
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_48,22_3", 'htmls/bwin/futbol/southamericaleague/argentina.txt') #Argentina
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_20,22_3", 'htmls/bwin/futbol/southamericaleague/peru.txt') #Peru
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_274,22_3", 'htmls/bwin/futbol/southamericaleague/colombia.txt') #Colombia
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=en&clientid=259&state=2_1,3_52,22_5", 'htmls/bwin/futbol/asianleagues/japan.txt') #Japan
	'''
	###################GET BWIN
	printWhatDoing('BASEBALL', 'Bwin')
	#Baseball
	url = "https://sports.bwin.es/es/sports/indexmultileague"
	data = {
		'sportId':'23',
		'dateFilter': getFecha() #Any-mes-dia
	}
	response = requests.post(url, data=data)
	file = open ('htmls/bwin/baseball.txt', "w")
	file.write(response.text.encode('utf-8'))
	file.close()
	#Tennis
	printWhatDoing('TENNIS', 'Bwin')
	url = "https://sports.bwin.es/es/sports/indexmultileague"
	data = {
		'sportId':'5'
	}
	response = requests.post(url, data=data)
	file = open ('htmls/bwin/tennis.txt', "w")
	file.write(response.text.encode('utf-8'))
	file.close()
	#Futbol
	printWhatDoing('FUTBOL', 'Bwin')
	url = "https://sports.bwin.es/es/sports/indexmultileague"
	data = {
		'sportId':'4',
		'dateFilter': getFecha() #Any-mes-dia
	}
	response = requests.post(url, data=data)
	file = open ('htmls/bwin/futbol.txt', "w")
	file.write(response.text.encode('utf-8'))
	file.close()
	print "==========BWIN SCRAPED=========="
	print
	'''

	###################GET TIPBET
	printWhatDoing('BASEBALL', 'Tipbet')
	#Baseball
	url = "https://www.tipbet.com/service/category-list"
	data = {
		'pageType':'categories',
		'categoryType':'total',
		'selectedSport':3,
		'selectedCategory':16,
		'selectedCategorySport':3,
		'selectedTournament':0,
		'isSportsExpanded':'true',
		'isCategoriesExpanded':'false',
		'isOutrightCategory':'false'
	}
	response = requests.post(url, data=data)
	file = open ('htmls/tipbet/baseball.txt', "w")
	file.write(response.text.encode('utf-8'))
	file.close()
	#Tennis
	printWhatDoing('TENNIS', 'Tipbet')
	escriureArxiu("https://www.tipbet.com/en/online-sport-betting/highlights", 'htmls/tipbet/tennis.txt')
	printWhatDoing('BASEBALL', 'Tipbet')
	#Futbol
	url = "https://www.tipbet.com/service/category-list"
	data = {
		'pageType':'highlights',
		'categoryType':'total',
		'selectedSport':1,
		'selectedCategory':0,
		'selectedCategorySport':0,
		'selectedTournament':0,
		'isSportsExpanded':'false',
		'isCategoriesExpanded':'false',
		'isOutrightCategory':'false'
	}
	response = requests.post(url, data=data)
	file = open ('htmls/tipbet/futbol.txt', "w")
	file.write(response.text.encode('utf-8'))
	file.close()
	print "==========TIPBET SCRAPED=========="
	print

	###################GET MARCAAPUESTAS
	#Baseball
	printWhatDoing('BASEBALL', 'Marca Apuestas')
	escriureArxiu("https://deportes.marcaapuestas.es/es/type-coupon?sb_type_ids=19248-44784-47030-47372-47373", 'htmls/marcaapuestas/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Marca Apuestas')
	escriureArxiu("https://deportes.marcaapuestas.es/es/calendar?date="+getFecha()+"&sport_code=TENN", 'htmls/marcaapuestas/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Marca Apuestas')
	escriureArxiu("https://deportes.marcaapuestas.es/es/calendar?date="+getFecha()+"&sport_code=FOOT", 'htmls/marcaapuestas/futbol.txt')
	print "==========MARCA APUESTAS SCRAPED=========="
	print


	###################GET SUERTIA
	#Baseball
	printWhatDoing('BASEBALL', 'Suertia')
	escriureArxiu("https://apuestas.suertia.es/deporte/3-beisbol", 'htmls/suertia/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Suertia')
	escriureArxiu("https://apuestas.suertia.es/deporte/21-tenis", 'htmls/suertia/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Suertia')
	escriureArxiu("https://apuestas.suertia.es/deporte/13-futbol", 'htmls/suertia/futbol.txt')
	print "==========SUERTIA SCRAPED=========="
	print


	###################GET KIROLBET
	#Baseball
	printWhatDoing('BASEBALL', 'Kirolbet')
	escriureArxiu("https://apuestas.kirolbet.es/esp/Sport/Deporte/429", 'htmls/kirolbet/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Kirolbet')
	escriureArxiu("https://apuestas.kirolbet.es/esp/Sport/Deporte/285", 'htmls/kirolbet/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Kirolbet')
	escriureArxiu("https://apuestas.kirolbet.es/esp/Sport/Deporte/40", 'htmls/kirolbet/futbol.txt')
	print "==========KIROLBET SCRAPED=========="
	print

	###################GET JUEGGING
	#Baseball
	printWhatDoing('BASEBALL', 'Juegging')
	escriureArxiu("https://apuestas.juegging.es/esp/Sport/Deporte/429", 'htmls/juegging/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Juegging')
	escriureArxiu("https://apuestas.juegging.es/esp/Sport/Deporte/285", 'htmls/juegging/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Juegging')
	escriureArxiu("https://apuestas.juegging.es/esp/Sport/Deporte/40", 'htmls/juegging/futbol.txt')
	print "==========JUEGGING SCRAPED=========="
	print

	###################GET CODERE
	printWhatDoing('BASEBALL', 'Codere')
	#Baseball
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=978215466&languageCode=es", 'htmls/codere/baseball.json')
	#Futbol
	printWhatDoing('FUTBOL', 'Codere')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103852954&languageCode=es", 'htmls/codere/futbol/spain.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103868646&languageCode=es", 'htmls/codere/futbol/holland.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103879105&languageCode=es", 'htmls/codere/futbol/france.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103860942&languageCode=es", 'htmls/codere/futbol/germany.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103877464&languageCode=es", 'htmls/codere/futbol/portugal.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103856868&languageCode=es", 'htmls/codere/futbol/italy.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=122051762&languageCode=es", 'htmls/codere/futbol/argentina.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=103850163&languageCode=es", 'htmls/codere/futbol/belgica.json')
	escriureArxiu("https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid=137775479&languageCode=es", 'htmls/codere/futbol/usa.json')
	print "==========CODERE SCRAPED=========="
	print

	###################GET BETSTARS
	#Baseball
	#printWhatDoing('BASEBALL', 'Betstars')
	#escriureArxiu("https://sports.betstars.es/sportsbook/v1/api/getCompetitionsForDay?sport=BASEBALL&date="+getFecha()+"&locale=es-es", 'htmls/betstars/baseball.json')
	#Tennis
	#printWhatDoing('TENNIS', 'Betstars')
	#escriureArxiu("https://sports.betstars.es/sportsbook/v1/api/getCompetitionsForDay?sport=TENNIS&date="+getFecha()+"&locale=es-es", 'htmls/betstars/tennis.json')
	#Futbol
	#printWhatDoing('FUTBOL', 'Betstars')
	#escriureArxiu("https://sports.betstars.es/sportsbook/v1/api/getCompetitionsForDay?sport=SOCCER&date="+getFecha()+"&locale=es-es", 'htmls/betstars/futbol.json')
	#print "==========BETSTARS SCRAPED=========="
	#print

	###################GET MARATHONBET
	#Baseball
	printWhatDoing('BASEBALL', 'Marathon Bet')
	escriureArxiu("https://www.mbet.es/en/betting/5?periodGroupAllEvents=6", 'htmls/marathonbet/baseball.txt')
	#Tennis
	printWhatDoing('TENNIS', 'Marathon Bet')
	escriureArxiu("https://www.mbet.es/en/popular/Tennis/?menu=2398", 'htmls/marathonbet/tennis.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Marathon Bet')
	escriureArxiu("https://www.mbet.es/en/betting/11?periodGroupAllEvents=24", 'htmls/marathonbet/futbol.txt')
	print "==========MARATHON BET SCRAPED=========="
	print

	###################GET PAF
	#Baseball
	printWhatDoing('BASEBALL', 'Paf')
	escriureArxiu("https://e3-api.kambi.com/offering/api/v3/pafes/listView/baseball.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1502746225266&categoryGroup=COMBINED&displayDefault=true", 'htmls/paf/baseball.json')
	#Tennis
	printWhatDoing('TENNIS', 'Paf')
	escriureArxiu("https://e3-api.kambi.com/offering/api/v3/pafes/listView/tennis.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1502746359383&categoryGroup=COMBINED&displayDefault=true", 'htmls/paf/tennis.json')
	#Futbol
	printWhatDoing('FUTBOL', 'Paf')
	escriureArxiu("https://e1-api.aws.kambicdn.com/offering/api/v3/pafes/listView/football.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1503679251177&categoryGroup=COMBINED&displayDefault=true", 'htmls/paf/futbol.json')
	print "==========PAF SCRAPED=========="
	print

	###################GET GOLDENPARK
	#Baseball
	printWhatDoing('BASEBALL', 'Golden Park')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/419122.2.xml", 'htmls/goldenpark/baseballmlb.txt')#MLB
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/408282.2.xml", 'htmls/goldenpark/baseballlmb.txt')#LMB
	#Tennis
	printWhatDoing('TENNIS', 'Golden Park')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/386998.2.xml", 'htmls/goldenpark/tennisatp.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/404123.2.xml", 'htmls/goldenpark/tenniswta.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/404124.2.xml", 'htmls/goldenpark/tennischallenger.txt')
	#Futbol
	printWhatDoing('FUTBOL', 'Golden Park')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/58974.2.xml", 'htmls/goldenpark/futbol/spain.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/116071.2.xml", 'htmls/goldenpark/futbol/england.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/59010.2.xml", 'htmls/goldenpark/futbol/germany.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/59009.2.xml", 'htmls/goldenpark/futbol/france.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/59016.2.xml", 'htmls/goldenpark/futbol/italy.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/59006.2.xml", 'htmls/goldenpark/futbol/holland.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/385008.2.xml", 'htmls/goldenpark/futbol/portugal.txt')
	escriureArxiu("https://www.goldenpark.es/cache/boNavigationMarketGroup/1335/ES/8/"+str(getRandomNumber(1401290153,14012901530))+"/384852.2.xml", 'htmls/goldenpark/futbol/otras.txt')
	print "==========GOLDEN PARK SCRAPED=========="
	print

	###################GET WANABET
	#Baseball
	printWhatDoing('BASEBALL', 'Wanabet')
	escriureArxiu("https://e1-api.aws.kambicdn.com/offering/api/v3/rfes/listView/baseball.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1502747964224&categoryGroup=COMBINED&displayDefault=true", 'htmls/wanabet/baseball.json')
	#Tennis
	printWhatDoing('TENNIS', 'Wanabet')
	escriureArxiu("https://e1-api.aws.kambicdn.com/offering/api/v3/rfes/listView/tennis.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1502748232749&categoryGroup=COMBINED&displayDefault=true", 'htmls/wanabet/tennis.json')
	#Futbol
	printWhatDoing('FUTBOL', 'Wanabet')
	escriureArxiu("https://e1-api.aws.kambicdn.com/offering/api/v3/rfes/listView/football.json?lang=es_ES&market=ES&client_id=2&channel_id=1&ncid=1503680878713&categoryGroup=COMBINED&displayDefault=true", 'htmls/wanabet/futbol.json')
	print "==========WANABET SCRAPED=========="
	print

	###################GET BET365
	#Baseball
	printWhatDoing('BASEBALL', 'Bet365')
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_3,3_16,22_2,5_38836,9_overview", 'htmls/bet365/baseball/MLB.txt')
	

	#Futbol
	printWhatDoing('FUTBOL', 'Bet365')
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_1%2C22_1%2C5_40942%2C9_summary", 'htmls/bet365/futbol/england/premier.txt') #Premier
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_1%2C22_1%2C5_41266%2C9_summary", 'htmls/bet365/futbol/england/championship.txt') #Premier 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_1,22_1,5_41268,9_summary", 'htmls/bet365/futbol/england/leagueOnePremier.txt') #League One
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_1,22_1,5_41270,9_summary", 'htmls/bet365/futbol/england/leagueTwoPremier.txt') #League two
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_1,22_1,5_41868,9_summary", 'htmls/bet365/futbol/england/nationalLeague.txt') #National League
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_32,22_1,5_42556,9_summary", 'htmls/bet365/futbol/spain/laliga.txt') #La liga
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_32,22_1,5_42560,9_summary", 'htmls/bet365/futbol/spain/segunda.txt') #Segunda
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_32%2C22_1%2C5_42826%2C9_overview", 'htmls/bet365/futbol/spain/segundaB.txt') #Segunda B
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_32%2C22_1%2C5_44414%2C9_summary", 'htmls/bet365/futbol/spain/superligafemenina.txt') #Fem Spain
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_42720%2C9_summary", 'htmls/bet365/futbol/italy/serieA.txt') #Serie A
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_43004%2C9_summary", 'htmls/bet365/futbol/italy/serieB.txt') #Serie B
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_31%2C22_1%2C5_43730%2C9_overview", 'htmls/bet365/futbol/italy/serieC.txt') #Serie C
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41576%2C9_summary", 'htmls/bet365/futbol/germany/bundesliga.txt') #Bundesliga
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41578%2C9_summary", 'htmls/bet365/futbol/germany/bundesliga2.txt') #Bundesliga 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_41808%2C9_summary", 'htmls/bet365/futbol/germany/bundesliga3.txt') #Bundesliga 3
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_30%2C22_1%2C5_42724%2C33_122%2C9_summary", 'htmls/bet365/futbol/germany/bundesligafem.txt') #Bundesliga Fem
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_40958%2C9_summary", 'htmls/bet365/futbol/france/ligue1.txt') #Ligue 1
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_40960%2C9_summary", 'htmls/bet365/futbol/france/ligue1.txt') #Ligue 2
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_7%2C22_1%2C5_42786%2C9_summary", 'htmls/bet365/futbol/france/liguenational.txt') #Ligue National
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_41198%2C9_overview", 'htmls/bet365/futbol/championships/championsleague.txt') #Champ. league
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_43378%2C9_overview", 'htmls/bet365/futbol/championships/championsleague.txt') #Champ. league Woman
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_393%2C22_1%2C5_41238%2C9_overview", 'htmls/bet365/futbol/championships/europaleague.txt') #Europe league
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_393%2C22_3%2C5_38534%2C9_overview", 'htmls/bet365/futbol/championships/libertadores.txt') #Libertadores
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_393%2C22_2%2C5_33229%2C9_overview", 'htmls/bet365/futbol/championships/concacaf.txt') #Concacaf
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_4%2C22_1%2C5_10876%2C9_overview", 'htmls/bet365/futbol/worldcup/europequal.txt') #uefa qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_4%2C22_2%2C5_10080%2C9_overview", 'htmls/bet365/futbol/worldcup/concacafqual.txt') #concacaf qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_4%2C22_3%2C5_10872%2C9_summary", 'htmls/bet365/futbol/worldcup/conmebolqual.txt') #conmebol qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_4%2C22_4%2C5_10878%2C9_overview", 'htmls/bet365/futbol/worldcup/cafqual.txt') #caf qualification
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_12%2C22_2", 'htmls/bet365/futbol/americaleagues/mexico.txt') #mexico
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_26%2C22_2%2C5_38738%2C9_overview", 'htmls/bet365/futbol/americaleagues/mls.txt') #MLS
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_289%2C22_2%2C5_42756%2C9_summary", 'htmls/bet365/futbol/americaleagues/costarica.txt') #Costa Rica
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1%2C3_437%2C22_2%2C5_42782%2C9_summary", 'htmls/bet365/futbol/americaleagues/honduras.txt') #Honduras
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_13,22_3", 'htmls/bet365/futbol/southamericaleague/brazil.txt') #Brazil
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_48,22_3", 'htmls/bet365/futbol/southamericaleague/argentina.txt') #Argentina
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_20,22_3", 'htmls/bet365/futbol/southamericaleague/peru.txt') #Peru
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_274,22_3", 'htmls/bet365/futbol/southamericaleague/colombia.txt') #Colombia
	escriureArxiu("http://stats.betradar.com/s4/gismo.php?&html=1&id=2563&gatracker=UA-29952099-17&language=en&clientid=259&state=2_1,3_52,22_5", 'htmls/bet365/futbol/asianleagues/japan.txt') #Japan

	print "==========BET365 SCRAPED=========="
	print


writeBaseball()


