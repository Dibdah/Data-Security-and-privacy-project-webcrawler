from spider import Spider
from urllib import parse
from general import *
from get_policy import Get_Policy


# Read file with list of websites and store them in a set
def read_file(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Find all links in main page and save them to a list
def crawl_homepage():
    startover()
    websites = read_file('website_list')
    for link in sorted(websites):
        linkset = Spider.crawl_page_once(link)
        find_policy_link(link, linkset)


# Find privacy policy list and past it on the screen
def find_policy_link(base_link, linkset):
    for link in linkset:
        if 'privacy' not in link:
            continue
        write_privacy_link_to_file(base_link, link)
        break


# Write privacy policy link to file:
def write_privacy_link_to_file(base_link, link):
    with open('privacy_links.txt', 'a') as file:
        url = parse.urljoin(base_link, link)
        file.write(url + '\n')


# Delete previous constant from privacy_links.txt
def startover():
    with open('privacy_links.txt', 'w'):
        pass


# Save policy links in a list
def get_queue():
    return file_to_set('privacy_links.txt')


# Get text from each policy link
def extract_policy(queue):
    for link in queue:
        policy = Get_Policy(link)
        policy.save_policy()


crawl_homepage()
queue = get_queue()
extract_policy(queue)