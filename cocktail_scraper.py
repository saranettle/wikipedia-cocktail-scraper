import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

csvfile = open("wikicocktails.csv", 'w', newline='', encoding='utf-8')#open .csv file
c = csv.writer(csvfile)
c.writerow(['Name', 'Alcohol', 'Ingredients'])#column headers for rows

#this function will collect info off wiki pages
def cocktailScraper(url):

	html = urlopen("https://en.wikipedia.org"+url)
	bsObj = BeautifulSoup(html, "html.parser")
		
	#find the name of the drink
	try:
		name = bsObj.find("h1",{"class":"firstHeading"})
	except:
		pass

	#find the primary alcohol used
	try:
		alcohol = bsObj.find("table", {"class":"infobox bordered hrecipe"}).ul.li
	except:
		pass
	#get all the ingredients, there are 3 main formats I could find
	try:
		ingredients1 = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
	except:
		pass
	try:
		ingredients2 = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
	except:
		pass
	try:
		ingredients3 = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
	except:
		pass
		
	cocktailInfo = [name, alcohol, ingredients1, ingredients2, ingredients3]
	#I discovered this by mistake: I put the 3 different ingredient gathering methods
	#since each item will only use only method, there won't be more than 3 columns
	row = []
	for info in cocktailInfo:
		try:
			row.append(info.get_text())
		except:
			pass
	c.writerow( row )
	#writing to the .csv file

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
					print("Success!")
				except:
					print("fail")
					#this helps me know whether or not it's working
				
#calling the crawl function, so we can start crawling and gathering info
getLinks()

csvfile.close()
#closing the csv file