import time
import requests
from zillow_data_scraper import ZillowData
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Get current date and time, and format it
current_time = datetime.now()
formatted_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
print(formatted_time)


class GoogleSheet:
    def __init__(self, data: ZillowData):
        # URL for the API endpoint
        self.url = "https://api.sheety.co/63af58bc12d0333a6fd921b836f52de3/zillowDataCollector/formResponses1"
        # Initialize with ZillowData
        self.data = data
        # Fetch the data from the ZillowData object
        self.get_data = self.data.get_data()
        self.api_key = os.getenv("SHETTY_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    # Method to retrieve information (e.g., for debugging or testing)
    def get_info(self):
        response = requests.get(self.url, headers=self.headers)
        print(response.text)

    # Method to add data to the Google Sheet via the API
    def add_info(self):
        # Convert data to list for iteration
        data__ = list(self.get_data)
        # Loop through the data and post each entry to the Google Sheet
        for i in range(len(data__)):
            # Construct the body for the API request
            body = {
                "formResponses1": {
                    "price": data__[i]["price"],
                    "address": data__[i]["address"],
                    "link": data__[i]["link"],
                    "timestamp": formatted_time  # Add the timestamp for when the data is added
                }
            }

            # Send the POST request to the API
            response = requests.post(url=self.url, json=body, headers=self.headers)
            print(response.text)  # Print the response for debugging
            time.sleep(1)



