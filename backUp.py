import csv


def ferbackup():
	writerequips1 = csv.writer(open("csvdocs/backup/datacacheEquipsBaseballbackup.csv", 'w'))
	writerequips2 = csv.writer(open("csvdocs/backup/backupbackup/datacacheEquipsBaseballbackup.csv", 'w'))
	writerlligues1 = csv.writer(open("csvdocs/backup/datacacheLliguesBaseballbackup.csv", 'w'))
	writerlligues2 = csv.writer(open("csvdocs/backup/backupbackup/datacacheLliguesBaseballbackup.csv", 'w'))

	readerequips = csv.reader(open("csvdocs/cacheEquipsBaseball.csv", 'r'))
	for row in readerequips:
		writerequips1.writerow(row)
		writerequips2.writerow(row)

	print "cacheEquipsBaseball: Back Up Done"

	readerlligues = csv.reader(open("csvdocs/cacheLliguesBaseball.csv", 'r'))
	for row in readerlligues:
		writerlligues1.writerow(row)
		writerlligues2.writerow(row)

	print "cacheLliguesBaseball: Back Up Done"
