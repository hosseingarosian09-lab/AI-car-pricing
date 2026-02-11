import requests 
from bs4 import BeautifulSoup
from random_headers import get_random_headers, headers_len
from divar_scrape import extract_car_info
import random , time

# a function to sleep for a random amount of time like a human
def human_like_delay():
    r = random.random()
    if r < 0.65:
        time.sleep(random.uniform(4.8, 7.5))
    elif r < 0.90:
        time.sleep(random.uniform(7.5, 13.0))
    else:
        time.sleep(random.uniform(13.0, 28.0))

#finding all links in the page
request = requests.get("https://divar.ir/s/iran/auto",timeout=(5, 15), headers=get_random_headers("https://divar.ir/s/iran/auto"))

print(request.status_code)

soup = BeautifulSoup(request.text , "html.parser")
cards = soup.find_all('a', class_='kt-post-card__action')

links = []
for card in cards:
    href = card.get('href')
    links.append('https://divar.ir' + href)

false_headers = []
headers = None
for link in links :

    # check if headers is in false_headers list and if the list is too long, clear it
    if len(false_headers) > headers_len():
        false_headers.clear()
    while headers in false_headers:
        headers = get_random_headers(str(link))

    human_like_delay()
    request = requests.get(link,timeout=(5, 15), headers = headers)
    info_list = extract_car_info(request)
    
    if info_list[0] != None:
        #send jason
        pass
    else:
        false_headers.append(headers)

    print(
        "titel_brand: ", info_list[0], "\n",
        "kilometer: ", info_list[1], "\n",
        "year: ", info_list[2], "\n",
        "color: ", info_list[3], "\n",
        "gearbox: ", info_list[4], "\n",
        "fule: ", info_list[5], "\n",
        "price: ", info_list[6], "\n",
        "body_condition: ", info_list[7], "\n",
        "discription: ", info_list[8], "\n",
        "pictuer: ", info_list[9], "\n",
        "-----------------------------"
        )


    
    