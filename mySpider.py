import urllib
from BeautifulSoup import *
from linkfinder import *
from general import *

class Spider():
	# Class Variables
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name+'/queue.txt'
		Spider.crawled_file = Spider.project_name+'/crawled.txt'
		self.boot()
		self.crawl_page('First Spider', Spider.base_url)	

	@staticmethod
	def boot():
		create_project_for(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)
		
	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print thread_name, '* now crawling *',page_url
			print 'Queue : ', str(len(Spider.queue)), ' | Crawled : ', str(len(Spider.crawled))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()

	@staticmethod
	def gather_links(page_url):
		mySet = set()
		try:
			response = urllib.urlopen(page_url)
			print response.info().getheader('Content-Type')
			if response.info().getheader('Content-Type').startswith('text/html'):
				myHtml = response.read()
				mySet = extractLinks(myHtml, Spider.base_url)
		except:
			pass		
		print "Received a Set of ", len(mySet)	
		return mySet

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			Spider.queue.add(url)	
		print "added"

	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)
		print "updated"
