import pandas as pd
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.clean_data()

    def clean_data(self):
        self.data['Price'] = self.data['Price'].replace('[\$,]', '', regex=True).astype(float)
        self.data['Price_per_sq_meter'] = (
            self.data['Price_per_sq_meter']
            .replace('1 m² - ', '', regex=True)
            .replace('[\$,]', '', regex=True)
            .astype(float)
        )

    def display_data(self):
        print(self.data.head())

    def filter_greater_than(self, column, value):
        filtered_data = self.data[self.data[column] > value]
        return filtered_data

    def filter_less_than(self, column, value):
        filtered_data = self.data[self.data[column] < value]
        return filtered_data

    def calculate_statistics(self):
        lowest_price = round(float(self.data['Price'].min()), 1)
        highest_price = round(float(self.data['Price'].max()), 1)
        avg_price = round(float(self.data['Price'].mean()), 1)
        avg_price_per_sqm = round(float(self.data['Price_per_sq_meter'].mean()), 1)
        return {
            "Lowest Price": lowest_price,
            "Highest Price": highest_price,
            "Average Price": avg_price,
            "Average Price per Sq Meter": avg_price_per_sqm
        }

    def plot_price_distribution(self):
        plt.hist(self.data['Price'].dropna(), bins=20)
        plt.title("Price distribution")
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.show()

    def plot_price_per_sqm_distribution(self):
        plt.hist(self.data["Price_per_sq_meter"].dropna(), bins=20)
        plt.title("Price Per Sq Meter Distribution")
        plt.xlabel("Price per sq Meter")
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    processor = DataProcessor("scraped_data.csv")
    processor.display_data()

    print("Properties with price greater than 100,000:")
    print(processor.filter_greater_than("Price", 100000))

    print("Statistics:")
    print(processor.calculate_statistics())

    processor.plot_price_distribution()
    processor.plot_price_per_sqm_distribution()
