import requests 
from bs4 import BeautifulSoup

#finding all links in the page
request = requests.get("https://divar.ir/s/iran/auto")

print(request.status_code)

soup = BeautifulSoup(request.text , "html.parser")
cards = soup.find_all('a', class_='kt-post-card__action')

links = []
for card in cards:
    href = card.get('href')
    links.append('https://divar.ir' + href)

#finding each element in each page 
for link in links :
  request = requests.get(link,timeout=5)
  soup = BeautifulSoup(request.text , "html.parser")

  titel_brand = None
  try:
    titel_brand = soup.find(class_="kt-unexpandable-row__action kt-text-truncate").text
  except TypeError:
    titel_brand = soup.find(class_="kt-base-row__end kt-unexpandable-row__value-box").text
  else : 
    titel_brand = None