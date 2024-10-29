# Home.ss.ge Real Estate Scraper

This project is a web scraper and data analyzer for real estate listings from SS.GE. It provides users with tools to scrape data, filter results, and analyze pricing distributions. The project is built with Flask, BeautifulSoup, and Pandas.

## Features

- **Data Scraping**: Scrapes real estate listing data from SS.GE, including property details, prices, addresses, and listing dates.
- **Data Analysis**: Processes scraped data to provide insights like average price, price per square meter, and distribution of prices.
- **Chart Visualization**: Displays price distribution charts to help users visualize data trends.


## Prerequisites

Ensure you have the following installed:

- Python 3.6+
- Pip (Python package manager)

- ## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sn-i/home.ss.ge-scraper.git
   cd home.ss.ge-scraper
   python app.py

  Access the Application:

Open a web browser and go to http://127.0.0.1:5000


## Usage

- **Scrape Data**: Enter the SS.GE link and click on **Scrape Data**. The application will scrape the data and display it in a tabular format.
  
- **Show Advanced Data**: Click the **Show Advanced Data** button to view statistical information, such as the highest, lowest, and average prices.

- **View Price Chart**: Click **Show Price Chart** to view a distribution chart of property prices.

---

## Error Handling

The application includes error handling for:

- **Invalid Links**: Checks if the link format is supported and provides feedback if not.
- **Scraping Failures**: Displays an error message if scraping fails due to network issues or website changes.
- **Missing Data**: Gracefully handles cases where certain data fields might be missing from the scraped results.







