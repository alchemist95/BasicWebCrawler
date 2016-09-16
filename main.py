import threading
import time
from Queue import Queue
from mySpider import 	Spider
from linkfinder import *
from general import *

projectName = 'thePragmaticEngineer'
baseUrl = raw_input("Enter the Base Url : ")
domainName = ''
queueFile = projectName + '/queue.txt'
crawledFile = projectName + '/crawled.txt'
numberOfThreads = 4
threadQueue = Queue()
Spider(projectName, baseUrl, domainName)


# create worker threads(will die when this prg is done)

def create_workers():
	for _ in range(numberOfThreads):
		t = threading.Thread(target=work)
		t.daemon= True
		t.start()

def work():
	while True:
		url = threadQueue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		threadQueue.task_done()				

def create_jobs():
	for link in file_to_set(queueFile):
		threadQueue.put(link)
	threadQueue.join()
	crawl()

# check for items in the queue file and crawl if so
def crawl():
	queue_links = file_to_set(queueFile)
	if len(queue_links)>0:
		print str(len(queue_links)), 'links left'
		create_jobs()

create_workers()
crawl()