import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from zillow_data_scraper import ZillowData


class SendData:
    def __init__(self, data: ZillowData):
        # Initialize the data and set up Chrome options for Selenium
        self.data = data
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)  # Keeps the browser open after execution
        self.driver = webdriver.Chrome(options=self.option)  # Initialize Chrome WebDriver
        self.driver.implicitly_wait(10)  # Wait implicitly for elements to be found
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSdghq3wYNVPiAHuAtxNY83InWFxdz5rsCWfjf-G9sp0gRjWKQ/viewform"

    def post_data(self):
        # Open the Google Form URL
        self.driver.get(url=self.url)

        # Loop through the data and fill the form fields
        for i in range(len(self.data.get_data())):
            # Fill the address field
            address = self.driver.find_element(By.CSS_SELECTOR, ".Qr7Oae input")
            address.send_keys(self.data.get_data()[i]["address"])

            # Fill the price field
            price = self.driver.find_element(By.XPATH,
                                             "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price.send_keys(self.data.get_data()[i]["price"])

            # Fill the link field
            link = self.driver.find_element(By.XPATH,
                                            "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link.send_keys(self.data.get_data()[i]["link"])

            # Click the submit button
            send = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
            send.click()

            # Click to send another response (reset the form for next entry)
            another = self.driver.find_element(By.LINK_TEXT, "إرسال رد آخر")
            another.click()

            # Optional: Add a small delay to avoid form submission issues
            time.sleep(1)

