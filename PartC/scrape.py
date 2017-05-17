from bs4 import BeautifulSoup
import requests
import os

"""
@author: arian1123
"""

#class for scraping speeches

class Scraper:

    def __init__(self):

        self.url = ""
        self.dom = ""
        self.listOfLinks = []

    def loadUrl(self, url):

        self.url = url
        page_request = requests.get(self.url)
        dom = BeautifulSoup(page_request.content, "lxml")
        self.dom = dom

    def getLinks(self):

        links = []

        #element that holds elements that wrap the urls
        itemList = self.dom.find_all('ul', class_='catItemAttachments')

        for i in itemList:
            item = []
            link = i.find('li').find('a')

            #store URL
            item.append("http://www.parliament.go.ke" + link['href'])

            #store name of file
            item.append(link['title'])

            links.append(item)

        self.listOfLinks = self.listOfLinks + links

def main():

    scraper = Scraper()

    # startCount gets appended to this
    urlBase = "http://www.parliament.go.ke/the-senate/house-business/hansard?start="
    firstPageURL = "http://www.parliament.go.ke/the-senate/house-business/hansard?limitstart=0"

    # get and store all links to pdfs
    # the kenyan parliament site uses a number in the slug of each page. we decrease startCount to algorithmically traverse all pages
    for startCount in range(400, 20, -20):
        url = urlBase + str(startCount)
        scraper.loadUrl(url)
        scraper.getLinks()

    #the first page does not follow the same url convention so scrape seperately
    scraper.loadUrl(firstPageURL)
    scraper.getLinks()

    # set directory
    #os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/PDFs")

    #/PDFs subdirectory to save file in

    #download files
    for l in scraper.listOfLinks:
        resp = requests.get(l[0])

        #try to find year in title of
        if "2013" in l[1]:
            subdir = "/2013"
        elif "2014" in l[1]:
            subdir = "/2014"
        elif "2015" in l[1]:
            subdir = "/2015"
        elif "2016" in l[1]:
            subdir = "/2016"
        elif "2017" in l[1]:
            subdir = "/2017"
        else:
            subdir = "/Misc"

        #download file
        with open(os.path.dirname(os.path.realpath(__file__)) + "/PDFs" + subdir + "/" + l[1], 'wb') as f:
            f.write(resp.content)

        #log file saving
        #print(l[1] + " saved in " + subdir)


if __name__ == "__main__":
    main()
