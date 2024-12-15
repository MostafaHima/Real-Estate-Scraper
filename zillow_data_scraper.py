from bs4 import BeautifulSoup
import requests


class ZillowData:
    def __init__(self):
        # URL of the Zillow clone website
        self.url = "https://appbrewery.github.io/Zillow-Clone/"
        # Lists to store links, prices, and addresses
        self.links = []
        self.prices = []
        self.addresses = []
        self.result = []

    def get_data(self):
        # Make a request to the website
        response = requests.get(self.url)
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(markup=response.text, features="html.parser")

        # Find the main container that holds the property information
        page = soup.find(id="grid-search-results")
        all_properties = page.find(class_="List-c11n-8-84-3-photo-cards")

        # Extract all the links, prices, and addresses
        links = all_properties.find_all("a")
        prices = all_properties.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        addresses = all_properties.find_all("address")

        # Loop through the addresses and clean the text before adding to the list
        for address in addresses:
            self.addresses.append(address.text.strip())

        # Loop through the prices, clean and format them before adding to the list
        for price in prices:
            if "+" in price.text:
                the_new = price.text.split("+")
                self.prices.append(the_new[0].strip())  # Remove any extra whitespace
            elif "/" in price.text:
                new_price = price.text.split("/")
                self.prices.append(new_price[0].strip())  # Remove any extra whitespace

        # Loop through the links and extract the href attribute
        for link in links:
            self.links.append(link["href"])

        # Combine the links, prices, and addresses into a dictionary and append to the result list
        for link, price, addr in zip(self.links, self.prices, self.addresses):
            new_dict = {"price": price, "link": link, "address": addr}
            self.result.append(new_dict)

        # Return the combined result
        return self.result
