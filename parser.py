from bs4 import BeautifulSoup
import requests

def simple_search():
    url = ('https://time-in.ru/time/vladikavkaz?ysclid=miexcp4t9s791336017')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_text = soup.get_text()

    mydivs = soup.find_all("div", {"class": "time-city-time-value"})
    for el in soup.find_all('div', attrs={'class': 'time-city-time-value'}):
        parsed_time = el.get_text()
        return parsed_time
