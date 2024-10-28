import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self, pages=1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        all_data = []
        for page in range(1, pages + 1):
            current_url = f"{self.url}&page={page}"
            response = requests.get(current_url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                listings = soup.find_all('div', class_='sc-bc0f943e-0')

                for listing in listings:
                    name = listing.find('h2', class_='sc-6e54cb25-3 gxoxbm listing-detailed-item-title').text.strip()
                    price = listing.find('span', class_='sc-6e54cb25-2 cikpcz listing-detailed-item-price').text.strip()
                    price_per_sq_meter = listing.find('span', class_='sc-6e54cb25-12 cdnEqa').text.strip()
                    address = listing.find('h5', class_='sc-bc0f943e-12 kIDemC listing-detailed-item-address').text.strip()
                    listed = listing.find('div', class_='create-date').text.strip()
                    link_div = soup.find('div', class_='sc-1384a2b8-6 jlmink')
                    if link_div:

                        link_tag = link_div.find('a')
                        link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else None
                        full_link = f"https://home.ss.ge{link}" if link and link.startswith("/") else link
                    else:
                        full_link = "No link available"

                    all_data.append({
                        'Name': name,
                        'Address': address,
                        'Price_per_sq_meter': price_per_sq_meter,
                        'Price': price,
                        'Listing_date': listed,
                        'Link': full_link


                    })

            else:
                print("Failed to retrieve the page. Status code:", response.status_code)
        return all_data

