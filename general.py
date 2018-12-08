'''
Reference:
Bucky Roberts "thenewbosten" open source crawler:
https://github.com/buckyroberts/Spider.git
'''
import os


# Each website is stored in a separate directory.
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating directory " + directory)
        os.makedirs(directory)


# Create queue and crawled files.
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file.
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file.
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the content of a file
def delet_file_content(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item in the set will be a new line in the file
def set_to_file(links, file):
    delet_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)


# create_project_dir('test')
# create_data_files('test', 'https://www.facebook.com')
