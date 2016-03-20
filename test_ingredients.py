from urllib.request import urlopen
from bs4 import BeautifulSoup



def cocktailScraper(url):

	html = urlopen(url)
	bsObj = BeautifulSoup(html, "html.parser")

	def getName():
		name = bsObj.find("caption",{"class":"fn"})
		
		try:
			print(name.get_text())
		except:
			pass

	def getAlcohol():
	
		try:
			alcohol = bsObj.find("table", {"class":"infobox bordered hrecipe"}).ul.li

			for item in alcohol:
				try:
					print(item.get_text())
				except:
					pass
		except:
			pass
			
	def getIngredients():
		try:
			ingredients = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
			for ingredient in ingredients:
				try:
					print(ingredient.get_text())
				except:
					pass
	
		except:
			pass

		try:
			ingredients = bsObj.find("table", {"class":"infobox bordered hrecipe"}).tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.ul
			for ingredient in ingredients:
				try:
					print(ingredient.get_text())
				except:
					pass
		except:
			ingredients = "null"

	getName()
	getAlcohol()
	getIngredients()
	
cocktailScraper("https://en.wikipedia.org/wiki/Singapore_Sling")