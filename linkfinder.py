import urllib
import re
from BeautifulSoup import *

def extractLinks(html, base_url):
	print 'Start'
	mySoup = BeautifulSoup(html)
	results = set()
	finalResults = set()
	for link in mySoup.findAll('a', href=True):
		results.add(str(link)) 
	for link in results:
		myList = re.findall('href="([^"]+)', link)
		myLink = str(myList[0])
		if myLink[0] == '/':
			print 'yay'
			myLink = base_url+myLink
		if not myLink.startswith('http'):
			continue
		print myLink	
		finalResults.add(myLink)
	print len(finalResults)
	return finalResults	