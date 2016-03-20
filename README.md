#Wikipedia IBA Cocktail Scraper

Hello, and welcome to my GitHub page for my very first web scraper. I created a scraper that would go through Wikipedia's list of cocktails page which can be found here:

https://en.wikipedia.org/wiki/List_of_cocktails

I intended to gather the following pieces of information from each linked page:
- The name of the cocktail
- The primary alcohol used
- The drinkware used
- Garnish (if applicable)
- The list of ingredients
- The method of preparation

Due to the inconsistent formatting of Wikipedia's website, which is understandably due to the fact that anyone can edit a Wikipedia page, I had to greatly simplify what I was looking for.

To give each Wikipedia page greater consistency, I used only the links from the following page:

https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails

I also had to narrow down the information I was scraping. I successfully collected the following information:

- The name of the cocktail
- The primary alcohol used
- The list of ingredients

Initially, I was anticipating collecting about 200 drink recipes from the original Wikipedia page. After I decided to use the IBA cocktail page, I anticipating only collected about 70 drink recipes. In the end, I collected 51 drinks.

I could spend more time refining the scraper to collect the remaining 20 or so drinks I am missing, however at that point, I may be better off manually inputting that information.

##How did I make this scraper?

I have included all of the files I used to create this scraper in the repo. Overall, I constructed this scraper by breaking down the tasks necessary into smaller python programs.

First, I created a python scraper that would scrape information off a single Wikipedia drink page. Luckily, most of these Wikipedia pages put all the information I needed in a table that had a specific class. After I got the scraper to work with one Wikipedia page, I would test a few others and make adjustments as necessary. The work for this step can be seen in test_ingredients.py

If you look in this file, you will notice that I create functions for each data I need. I will later ditch these functions.

Second, in the python file test_getlinks.py, I created a scraper that would collect all the links I needed to find the Wikipedia pages with the cocktail drink recipes. Luckily, this was an easy task. All of the links were in a div with a class, so they were very easy to extract.

The third step of my process was much trickier. In test_crawl.py, I attempted to combine the two previous python files. I knew I needed to create a loop that would go through each Wikipedia link. I put all of the scraping functions inside a larger function, and then I put that larger function in a loop. In this loop, the program is collecting links off the Wikipedia page. With each link it finds, it goes into the scraping function, causing it to run. I had my results printed to the console, confirming it was working.

Finally, now that I knew I could scrape multiple pages, I needed to save the data to a .csv file. This can be found in test_write.py, which greatly resembles my final product. I tinkered with the code until it would write as much data as possible to the .csv file.

##Okay, how does this work though?

Let me try to paraphrase what is going on with my function, as well as elaborate on my various challenges.

- First, I import all the modules necessary to complete my task.
- I then open a .csv file, give it a name and location, and finally I indicate the column headers.
- I begin writing my big scraping function. Notice that where I indicate to open a url, there's a variable present. This variable will ultimately be fed by the loop from the getLinks function.
- I gather the name of the drink and the primary alcohol, assigning the variables "name" and "alcohol". Scraping this information was not particularly difficult.
- You may notice that I have three ingredient variables. Since Wikipedia has very inconsistent formatting, I chose 3 bsObj's that would give me the information I needed.
- I create a list called cocktailInfo. This will be used to ultimately write rows into the .csv file. You may notice I include ingredient1, ingredient2, and ingredient3 even though there should only be 3 columns total. Since only one of those variables will have any information, each item will reliably fill no more than 3 rows.
- I create a loop that will, for each info in cocktailInfo, will write a row to the .csv file.
- This huge scraping function ends, then I start writing the getLinks function.
- In the getLinks function, towards the end, I have a loop that generates the various Wikipedia links that I need. I needed a way to feed these links into my scraper function, so I put my scraper function in this loop. Every time the getLinks function got a new link, my scraper function would immediately start scraping for that page, before moving on to the next page.
- Finally, I finish the getLinks function. I then call the getLinks function. Finally, I close the .csv file.
- Now I can rest.

Thank you for reading through this wall of text! If you have any questions, please feel free to message me.

