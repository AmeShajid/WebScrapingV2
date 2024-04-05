


from bs4 import BeautifulSoup
import requests

url = ("https://quotes.toscrape.com")

page_to_scrape = requests.get(url)

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.findAll("span", attrs={"class": "text"})

authors = soup.findAll("small", attrs={"class": "author"})


#for quote in quotes:
#    print(quote.text)
#for author in authors:
#    print(author.text)

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)









