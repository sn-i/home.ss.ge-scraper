import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)

if __name__ == "__main__":
    url = "https://www.myhome.ge/s/iyideba-bina-Tbilisshi/?deal_types=1&real_estate_types=1&cities=1&currency_id=1&CardView=2&page=1"
    scraper = Scraper(url)
    scraper.fetch_data()
