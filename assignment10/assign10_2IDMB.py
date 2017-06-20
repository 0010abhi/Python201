from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2

## Read Html Data from Url using urllib2
url_to_scrap = urllib2.urlopen("http://www.imdb.com/chart/top")
scrap_html_string = url_to_scrap.read()
url_to_scrap.close()

## Converting Html into python tree object structure using BeautifulSoup
only_table = SoupStrainer("table")
soup = BeautifulSoup(scrap_html_string,"html.parser",parse_only=only_table)
top250MoviesTd = soup.find_all(attrs={"class":"titleColumn"},limit=250) 
for data in top250MoviesTd:
    print data.get_text(' ',strip=True)
