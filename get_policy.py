from spider import Spider
from urllib.request import urlopen
from domain import *
from general import *
from boilerpipe.extract import Extractor
class Get_Policy:

    project_name = ''
    homepage_= ''
    domain_name = ''
    URL = ''

    def __init__(self, url):
        self.project_name = get_domain_name(url)
        self.homepage = url
        self.domain_name = get_domain_name(url)
        self.URL = url

    def save_policy(self):
        try:
            # page_bytes = urlopen(self.URL)
            # html_page = page_bytes.decode("utf-8")
            # print(html_page)
            extractor = Extractor(extractor='ArticleExtract', url=self.URL)
            print(extractor.getText())
            write_file(self.project_name, extractor.getText())
        except:
            print("Failed to get privacy policy from " + self.URL)


