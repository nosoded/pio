import requests
import time
from bs4 import BeautifulSoup
import re
import time
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session = get_tor_session()
request = session.get("https://steamcommunity.com/market/search?appid=730&q=#p0")

def sc_parse():
    soup = BeautifulSoup(request.content, 'html5lib')
    urlparse = soup.find_all('div', attrs={'id': 'searchResultsRows'})
    for parseuk in urlparse:
        hrefUK = parseuk.find_all('a', attrs={'class': 'market_listing_row_link'})
        for a in hrefUK:
            z = a["href"]
            print("var z = ", z)
            somebody = session.get(z)
            souup = BeautifulSoup(somebody.content, 'html5lib')

            sightparse = souup.find_all('script', attrs={'type': 'text/javascript'})
            try:
                result = re.search('ItemActivityTicker.Start\((.*)\)', sightparse.__str__())
                itemId = result.group(1)
            except:
                result = re.search('Market_LoadOrderSpread\((.*)\)', sightparse.__str__())
                itemId = result.group(1)
            print(itemId)
            print(request.status_code)
            print("------------------------------------------------------------------------------------")
            time.sleep(0.3)
sc_parse()
