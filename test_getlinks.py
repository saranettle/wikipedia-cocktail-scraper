from urllib.request import urlopen
from bs4 import BeautifulSoup

drinkLinks = []

html = urlopen("https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails")
bsObj = BeautifulSoup(html, "html.parser")

def getLinks():
	cocktailList = bsObj.find("div",{"id":"mw-content-text"}).findAll("div",{"class":"div-col columns column-width"})

	for cocktail in cocktailList:
		links = cocktail.findAll("a")
		for link in links:
			print(link.attrs['href'])

getLinks()


print(drinkLinks)