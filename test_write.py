import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

#opening the csv file
csvfile = open("test_write.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
c.writerow(['Name', 'Alcohol', 'Ingredients'])

cocktailInfo = []
#empty list where I will put in the cocktail information, name, alcohol, ingredients

itWorked = 0

#this function will collect info off wiki pages
def cocktailScraper(url):

	html = urlopen("https://en.wikipedia.org"+url)
	bsObj = BeautifulSoup(html, "html.parser")
	
	
	#find the name of the drink - this section works	
	try:
		name = bsObj.find("h1",{"class":"firstHeading"})
	except:
		pass

	#find the primary alcohol used - this section works
	try:
		alcohol = bsObj.find("table", {"class":"infobox bordered hrecipe"}).ul.li
	except:
		pass
	#get all the ingredients
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
	
	row = []
	for info in cocktailInfo:
		try:
			row.append(info.get_text())
		except:
			pass
	c.writerow( row )

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
				
#calling the crawl function, so we can start crawling and gathering info
getLinks()

print(cocktailInfo)

csvfile.close()
#closing the csv file