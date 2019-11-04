from bs4 import BeautifulSoup
import requests

headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://steamcommunity.com/market/search?appid=730&q=#p1'


def ss_parse():
    urls = [base_url]
    session = requests.Session()
    request = session.get(url=base_url, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        try:
            count = int(1301)
            for i in range(count):
                url = 'https://steamcommunity.com/market/search?appid=730&q=#p{i}'
                if url not in urls:
                    urls.append(url)
        except:
            pass

        resultRows = soup.find_all('div', attrs={'id': 'searchResultsRows'})

        for row in resultRows:
            link = row.find_all('a', attrs={'class': 'market_listing_row_link'})
            for a in link:
                print("LINK: ", a["href"])

    else:
        print("error")


ss_parse()