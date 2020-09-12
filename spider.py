import os

#Each site u crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating directory "+ directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name+ 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#create a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)