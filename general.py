import os  
# Each website you crawl is a seperate project (folder)
def create_project_for(directory):
	if not os.path.exists(directory):
		print 'Creating project', directory
		os.makedirs(directory)	

# Create Queue and Crawled files
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

# Create a new file
def write_file(path, data):			
	f = open(path, 'w')
	f.write(data)
	f.close()

# convert links in file to set
def file_to_set(file_name):
	results = set()
	with open(file_name, 'r') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results
	
# reverse
def set_to_file(mySet,file):
	myFile = open(file, 'w')
	for link in sorted(mySet):
		myFile.write(link+'\n')		 
	myFile.close()