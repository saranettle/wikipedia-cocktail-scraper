from urllib.request import urlopen
from bs4 import BeautifulSoup

#this function will collect info off wiki pages
def cocktailScraper(url):

	html = urlopen("https://en.wikipedia.org"+url)
	bsObj = BeautifulSoup(html, "html.parser")
	#find the name of the drink
	#find the name of the drink				
	try:
		name = bsObj.find("caption",{"class":"fn"})		
		for item in name:
			try:
				print(name.get_text())
				print("Success")
			except:
				print("None")
	except:
		print("fail")

	#find the primary alcohol used
	try:
		alcohol = bsObj.find("table", {"class":"infobox bordered hrecipe"}).ul.children

		for item in alcohol:
			try:
				print(item.get_text())
				print("Success")
			except:
				pass
	except:
		print("fail")

	#get all the ingredients
	try:
		ingredients = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
		for ingredient in ingredients:
			try:
				print(ingredient.get_text())
			except:
				pass
	#note, the wiki pages are formatted in two ways, so I provide two methods to find the info
	except:
		pass

	try:
		ingredients = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
		for ingredient in ingredients:
			try:
				print(ingredient.get_text())
				print("Success")
			except:
				pass
	except:
		print("fail")

#begin the crawling function
def getLinks():
	html = urlopen("https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails")
	bsObj = BeautifulSoup(html, "html.parser")

	cocktailList = bsObj.find("div",{"id":"mw-content-text"}).findAll("div",{"class":"div-col columns column-width"})
	#finding all the a tags
	for cocktail in cocktailList:
		links = cocktail.findAll("a")
		for link in links:
			if 'href' in link.attrs:
				try:
					cocktailScraper((str(link.attrs['href'])))
					#running the previously written scraping function above, for each link gathered
				except:
					pass
				
#calling the crawl function, so we can start crawling and gathering info
getLinks()