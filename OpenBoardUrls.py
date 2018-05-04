import requests
from bs4 import BeautifulSoup
import urllib
import webbrowser
import os

class Pages(object):
    currentPageIndex = 0
    pages = {}
    next = ""
    previous = ""
    last = ""

    def __init__(self, currentPageIndex, pages):
        self.currentPageIndex = currentPageIndex
        self.pages = pages

def getHTMLResource(url):
    response = requests.get(url)
    # charset_re = response.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=response.I)
    # pragma_re = response.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=response.I)
    # xml_re = response.compile(r'^<\?xml.*?encoding=["\']*(.+?)["\'>]')
    charset = requests.utils.get_encodings_from_content(response.text)
    if len(charset) > 0:
        response.encoding = charset[0]
    return response.text

def getResult(htmlText):
    linkList = list()
    pagesDict = {}
    date = ''
    soup = BeautifulSoup(htmlText, "html.parser")
    items = list()
    itemsNew = soup.findAll('th', attrs={'class': 'new'})
    itemsCommon = soup.findAll('th', attrs={'class': 'common'})
    itemsLock = soup.findAll('th', attrs={'class': 'lock'})
    items.extend(itemsNew)
    items.extend(itemsCommon)
    items.extend(itemsLock)
    print("total items count is " + str(len(items)))
    for item in items:
        author = item.find_next_sibling('td', attrs={'class': 'author'})
        if author:
            dates = author.select('em')
            if dates:
                date = dates[0]
        link = item.select('span a')
        if link and len(link) > 0:
            print(link[0].get('href') + '; ' + date.string + '; ' + link[0].string)
            linkList.append(link[0].get('href'))


    # form = soup.find('form', attrs={'name': 'moderate'})
    # if form:
    #     #items = form.select('.new')
    #     items = form.findAll('th', attrs={'class': 'new'})
    #     for item in items:
    #         print("name: " + item.name + "; content: " + item.string)

    # for form in forms:
    #     #itmes = form.findAll('tbody')
    #     tables = form.findAll('table')
    #     children = form.children
    #     for child in children:
    #         print(child.name)
    #     itmes = tables[len(tables) - 1].findAll('tbody')
    #     for item in itmes:
    #         # link = item.find('th',attrs={'class': 'new'})
    #         link = item.find('a').get('href')
    #         #print(link)
    #         linkList.append(link)
    pagesDiv = soup.find('div',attrs={'class': 'pages'})
    currentIndex = 0
    next = ""
    previous = ""
    last = ""
    if pagesDiv:
        for page in pagesDiv.children:
            if page.name == "a":
                pagesDict.setdefault(page.string, page.get('href'))
                step = page.get("class")
                #print(type(step))
                if step:
                    if "next" in step:
                        next = page.get('href')
                    elif "prev" in step:
                        previous = page.get('href')
                    elif "last" in step:
                        last = page.get('href')
            elif page.name == 'strong':
                currentIndex = page.string

    objPages = Pages(currentIndex, pagesDict)
    objPages.previous = previous
    objPages.next = next
    objPages.last = last
    return linkList, objPages


FORMAT_URL = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  -incognito {0}'
FORMAT_PAGES_INFO = "Current page is {0}, open links press 'G', Select another page press 'T', press 'E' to exit"
inputStr = input("Open the first website: ")
URL = inputStr.strip()

while True:
    htmlText = getHTMLResource(URL)
    linkList, objPages = getResult(htmlText)
    option = input(FORMAT_PAGES_INFO.format(objPages.currentPageIndex))
    if option.upper() == "G":
        for link in linkList:
            realUrl = urllib.parse.urljoin(URL, link)
            #webbrowser.open(realUrl, 2)
            url = FORMAT_URL.format(realUrl)
            print(url)
            os.system(url)
        temp = urllib.parse.urljoin(URL, objPages.next).strip()
        URL = temp
    elif option.upper() == "T":
        # for key in objPages.pages.keys():
        #     print("page: " + key)
        for key,value in objPages.pages.items():
            print("page: " + key + "; url: " + value)
        selectedPageKey = input("Select page to go:")
        if selectedPageKey in objPages.pages:
            temp = urllib.parse.urljoin(URL, objPages.pages.get(selectedPageKey)).strip()
            URL = temp
    elif option.upper() == 'E':
        break;
