from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from utilsScraper import *
from random import randint
from lxml import html
from writer import *
from futbolScraper import *
import requests
import json
import time
import csv
import time
import collections 
class bcolors:
    VERMELL = '\033[91m'
    BLAU = '\033[94m'
    VERD = '\033[92m'
    TURQUESA = '\033[96m'
    ENDC = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRATLLAT = '\033[4m'

def escriureArxiu(url, where):
	response = requests.get(url)
	file = open (where, "w")
	file.write(response.text.encode("utf-8"))
	file.close()


###################GET BWIN
#Baseball
#printWhatDoing('BASEBALL', 'Bwin')
escriureArxiu("https://stats.betradar.com/s4/gismo.php?&html=1&id=1827&gatracker=UA-12985236-7&language=de&clientid=475&state=2_3,3_16,22_2,5_38836,9_overview", 'htmls/bwin/baseball/MLB.txt')


#Futbol
#printWhatDoing('FUTBOL', 'Bwin')
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
omplirCache()
