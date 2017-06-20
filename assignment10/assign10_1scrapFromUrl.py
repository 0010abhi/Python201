from bs4 import BeautifulSoup
import urllib2

## get url from the user
print "We will give you 10 href present in the url."
url = raw_input("Please enter the url to scrap data:")
## Read Html Data from Url using urllib2
# url = "https://www.reddit.com"
print "Url Accepted:", url.strip()
url_to_scrap = urllib2.urlopen(url)
scrap_html_string = url_to_scrap.read()
url_to_scrap.close()

## Converting Html into python tree object structure using BeautifulSoup
soup = BeautifulSoup(scrap_html_string,"html.parser")
all_a_tags = soup.find_all("a",limit=10)

for tag_a in all_a_tags:
    print tag_a['href'],":",tag_a.next
