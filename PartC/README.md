This script is used to scrape and download the pdf files of Kenyan parliamentary speeches available on: http://www.parliament.go.ke/

The Scraper class is used to extract the download links to the pdfs from a given entered webpage. The BeautifulSoup extension for python was used to parse the HTML DOM. Each found link, along with the file name, is added to a list stored in the Scraper object.

In the main method, to scrape all links that contain pdf downloads we update the query string "start" in the URL, starting at 400 and reducing it by 20 to get the next page (f.i. http://www.parliament.go.ke/the-senate/house-business/hansard?start=400). The first page of downloads does not follow this pattern however, so we scrape it separately (http://www.parliament.go.ke/the-senate/house-business/hansard?limitstart=0). To download the files we traverse the list of links in the Scraper object, check to see if we can find the year in the file name, and then store the file in its appropriate subdirectory. Subdirectories are categorized by year.

This downloaded files are uploaded to the Box.