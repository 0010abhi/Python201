from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
soupFromHtmlFile = BeautifulSoup(open('D:\\Python201\\Python201\\assignment10\\webscrap.html'), "html.parser")
# soupFromHtmlString = BeautifulSoup('<html>Html String Data</html>', "html.parser")

# print "Data From Html File: ", soupFromHtmlFile
# prettify() : For alignment of html
# print "Prettify the html file data: ", soupFromHtmlFile.prettify()
# print "Data From Html String: ", soupFromHtmlString

#get only first para
paraTag = soupFromHtmlFile.p
# print "Para Tag", paraTag
# print type(paraTag)
# print paraTag['class']
# print paraTag['id']
# print paraTag.attrs
# print paraTag.string

#find all available tags
paras = soupFromHtmlFile.find_all('p')
# print paras
# for para in paras:
#     print para
#     print type(para)
#     print para['class']
#     print para['id']
#     print para.attrs
#     print para.string
#     print type(para.string)
#     print "\n****\n"

# Navigation in html tags
hereIsTitle = soupFromHtmlFile.title
hereIsTitleName = soupFromHtmlFile.title.name
# print "hereIsTitle: ",hereIsTitle, "\nhereIsTitleName: ",hereIsTitleName
hereIsTitleParent = soupFromHtmlFile.title.parent
hereIsHead = soupFromHtmlFile.head
# print "hereIsTitleParent: ",hereIsTitleParent, "\nhereIsHead: ",hereIsHead
# inside a tag .next & .previous
# print "Next to title: ",hereIsTitle.next
# print "Previous to title: ", hereIsTitle.previous, "Is Previous equals empty string: ", type(hereIsTitle.previous)


#Filtering the data from html.
# can pass string, regex, list, function
#1) By Passing string : all b tags
allBTags = soupFromHtmlFile.find_all('b')
# print "allBTags: ",allBTags

#2) By regex all tags start from s
tagsStartFromS = soupFromHtmlFile.find_all(re.compile('^s'))
# print tagsStartFromS

#3) By regex all tags contain a in their name
tagsContainA = soupFromHtmlFile.find_all(re.compile('a'))
# print "tags contain a in their name: "
# for tag in tagsContainA:
#     print tag.name

#4) By tags matching list 
tagsMatchingToList = soupFromHtmlFile.find_all(['a','b'])
# print "tagsMatchingToList: ",tagsMatchingToList

#5) All tags present in file
allTagsInFile = soupFromHtmlFile.find_all(True)
# print "allTagsInFile: "
# for tag in allTagsInFile:
#     print tag.name

#6) Search attr having class & id both
def HasClassAndIdAttr(tag):
    return tag.has_attr('class') and tag.has_attr('id')

ContainsClassAndIdAttr = soupFromHtmlFile.find_all(HasClassAndIdAttr)
# print "HasClassAndIdAttr: ",ContainsClassAndIdAttr

# print soupFromHtmlFile.find_all(id="NameInPara")

## passing name, attr, limit to these methods for filtering.
## Many More to explore like 
# 1) find_parent(), find_parents()
# 2) find_all_next(), find_next()
# 3) find_all_previous, find_previous()
# 4) find_next_siblings(), find_next_sibling()
# 5) find_previous_siblings(), find_previous_sibling()

# Formatting the data & get text
# soupFromHtmlFile.get_text()
# print soupFromHtmlFile.get_text('+')
# print soupFromHtmlFile.get_text('|',strip=True)

# parsing in efficient Way than find all.
only_tag_a = SoupStrainer('a')
soupForTagsAHtmlFile = BeautifulSoup(open('D:\\Python201\\Python201\\assignment10\\webscrap.html'), "html.parser",parse_only=only_tag_a).prettify()
print soupForTagsAHtmlFile