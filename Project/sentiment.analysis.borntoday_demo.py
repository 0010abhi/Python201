# from bs4 import BeautifulSoup
# from bs4 import SoupStrainer
# import urllib2
# # import time
# import json

# ## Read Html Data from Url using urllib2

# url = 'http://m.imdb.com/feature/bornondate_json?today=2017-06-10'
# url2 = "http://m.imdb.com/feature/bornondate"
# # req = urllib2.Request(url)

# response = urllib2.urlopen(url)
# r1 = response.read()
# print r1, type(r1)
# data = json.loads(r1)
# print json.loads(r1)
# response.close()

# # re1 = urllib2.Request(url2,data)
# url_to_scrap = urllib2.urlopen(url2)
# # print json.load(response)
# scrap_html_string = url_to_scrap.read()
# print scrap_html_string
# url_to_scrap.close()



# # print the_page

# ## Converting Html into python tree object structure using BeautifulSoup
# # soup = BeautifulSoup(scrap_html_string,"html.parser")
# # bornTodaySectioon = soup.find('section')

# # print bornTodaySectioon

# import sys  
# from PyQt4.QtGui import *  
# from PyQt4.QtCore import *  
# from PyQt4.QtWebKit import *  
  
# class Render(QWebPage):  
#   def __init__(self, url):  
#     self.app = QApplication(sys.argv)  
#     QWebPage.__init__(self)  
#     self.loadFinished.connect(self._loadFinished)  
#     self.mainFrame().load(QUrl(url))  
#     self.app.exec_()  
  
#   def _loadFinished(self, result):  
#     self.frame = self.mainFrame()  
#     self.app.quit()  
  
# # url = 'http://webscraping.com'  
# r = Render(url2)  
# html = r.frame.toHtml()  

from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Firefox(firefox_binary=binary)

url2 = "http://m.imdb.com/feature/bornondate"
# use firefox to get page with javascript generated content
with closing(Firefox()) as browser:
     browser.get(url2)
    #  button = browser.find_element_by_name('button')
    #  button.click()
     # wait for the page to load
     WebDriverWait(browser, timeout=10).until(
         lambda x: x.find_element_by_class('poster'))
     # store it to string variable
     page_source = browser.page_source
print(page_source)

# from selenium import webdriver
# from bs4 import BeautifulSoup

# url = 'http://nametrends.net/name.php?name=Ruby'
# driver = webdriver.Firefox()
# driver.get(url)
# print "start looking"
# # wait until 'tabular' appears on browser
# assert 'tabular' not in driver.page_source

# html = BeautifulSoup(driver.page_source)
# for table in html.find_all('table'):
#     print table
