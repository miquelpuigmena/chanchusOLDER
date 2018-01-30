from baseballScraper import *
from tennisScraper import *
from futbolScraper import *
from utilsScraper import printNegrita
from writer import ferbackup, closecsv12, closecsv1x2, omplirCache
def baseballmakeData():
	sportiumBaseballScraper()
	interwettenBaseballScraper()
	bwinBaseballScraper()
	williamhillBaseballScraper()
	tipbetBaseballScraper()
	betfairBaseballScraper()
	marcaapuestasBaseballScraper()
	suertiaBaseballScraper()
	kirolbetBaseballScraper()
	codereBaseballScraper()
	betstarsBaseballScraper()
	jueggingBaseballScraper()
	marathonbetBaseballScraper()
	pafBaseballScraper()
	wanabetBaseballScraper()
	goldenparkBaseballScraper()
	bet365BaseballScraper()
	ferbackup()
def tennismakeData():
	interwettenTennisScraper()
	tipbetTennisScraper()
	sportiumTennisScraper()
	betfairTennisScraper()
	williamhillTennisScraper()
def futbolmakedata():
	interwettenFutbolScraper()
	betfairFutbolScraper()
	marathonbetFutbolScraper()
	williamhillFutbolScraper()
	sportiumFutbolScraper()
	marcaapuestasFutbolScraper()
	suertiaFutbolScraper()
	codereFutbolScraper()
	bet365FutbolScraper()
	bwinFutbolScraper()
def closecsvs():
	closecsv12()
	closecsv1x2()

#tennismakeData()
printNegrita( "PARSING FUTBOL")
printNegrita( "=============================================================")
futbolmakedata()
printNegrita( "PARSING BASEBALL")
printNegrita( "=============================================================")
baseballmakeData()
omplirCache()
closecsvs()
#ferbackup()

