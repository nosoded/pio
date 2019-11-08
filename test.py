from bs4 import BeautifulSoup
import requests
headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://steamcommunity.com/market/search?appid=730&q=#p1'
def ss_parse(base_url, headers):
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        try:
            count = int(1301)
            for i in range(count):
                url = f'https://steamcommunity.com/market/search?appid=730&q=#p{i}'
                if url not in urls:
                    urls.append(url)
        except:
            pass
        urlparse = soup.find_all('div', attrs={'id': 'searchResultsRows'})
        firstpriceparse = soup.find_all('span', attrs={'class': 'market_table_value normal_price'})
        for fp in firstpriceparse:
            firstprice = fp.find('span', attrs={'class': 'normal_price'})['data-price']
            #print(int(firstprice)/100)

        for parseuk in urlparse:
            hrefUK = parseuk.find_all('a', attrs={'class': 'market_listing_row_link'})
            for a in hrefUK:
                z = a["href"]
                somebody = session.get(z, headers = headers)
                souup = BeautifulSoup(somebody.content, 'html.parser')
                sightparse = souup.find_all('div', attrs={'id': 'market_commodity_buyrequests'})
                print(sightparse)
                for lolo in sightparse:
                    try:
                        itemname = lolo.find_all('span', attrs={'class': 'market_commodity_orders_header_promote'}).text
                        print(itemname)
                    except: pass
    else:
        print("error")
ss_parse(base_url,headers)
#https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29
