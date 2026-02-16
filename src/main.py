import requests 
from random_headers import get_random_headers, get_headers_len
from divar_scrape import extract_car_info
from divar_link_scrape import scrape_links_divar
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
links = scrape_links_divar("https://divar.ir/s/iran/auto")
# request = requests.get("https://divar.ir/s/iran/auto",timeout=(5, 15), headers=get_random_headers("https://divar.ir/s/iran/auto"))
# print(request.status_code)
# soup = BeautifulSoup(request.text , "html.parser")
# cards = soup.find_all('a', class_='kt-post-card__action')

# links = []
# for card in cards:
#     href = card.get('href')
#     links.append('https://divar.ir' + href)

false_headers = []
headers = None
len_data = 0
for link in links :

    # check if headers is in false_headers list and if the list is too long, clear it
    if len(false_headers) > get_headers_len():
        false_headers.clear()
    while headers in false_headers:
        headers = get_random_headers(str(link))

    human_like_delay()
    request = requests.get(link,timeout=(5, 15), headers = headers)

    #json data
    data = extract_car_info(request)
    if data != None :
        if data["title_brand"] != None:
            # send data to database or save it to a file
            pass
        else:
            false_headers.append(headers)

    print(data)
    len_data +=1
    print()

print(len_data)
    

    
    