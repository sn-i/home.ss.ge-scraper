from flask import Flask, render_template, request, jsonify, url_for
from scraper import Scraper
from data_processor import DataProcessor
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    if not url:
        return jsonify({"error": "Url is required"}), 400
    try:
        scraper = Scraper(url)
        data = scraper.fetch_data(3)
        df = pd.DataFrame(data)
        df.to_csv("scraped_data.csv", index=False)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Scraping failed: {str(e)}"}), 500


@app.route('/show_homes')
def show_homes():
    if not os.path.exists("scraped_data.csv"):
        return jsonify({"error": "No data available. Please scrape data first."}), 400
    data = pd.read_csv("scraped_data.csv").to_dict(orient='records')
    return jsonify(data)


@app.route('/show_chart')
def show_chart():
    if not os.path.exists("scraped_data.csv"):
        return jsonify({"error": "No data available. Please scrape data first."}), 400
    processor = DataProcessor("scraped_data.csv")
    processor.plot_price_distribution()
    chart_url = url_for('static', filename='price_chart.png')
    return jsonify({"chart_url": chart_url})

@app.route('/show_advanced_data')
def show_advanced_data():
    if not os.path.exists("scraped_data.csv"):
        return jsonify({"error": "No data available. Please scrape data first."}), 400
    processor = DataProcessor("scraped_data.csv")
    stats = processor.calculate_statistics()
    return jsonify(stats)


if __name__ == "__main__":
    app.run(debug=True)
