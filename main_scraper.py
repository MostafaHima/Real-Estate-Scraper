# Import the necessary classes from the respective files
from google_form_submission import SendData
from zillow_data_scraper import ZillowData
from google_sheet_integration import GoogleSheet

# Create an instance of ZillowData to fetch the data
data = ZillowData()

# Send data to Google Drive using the SendData class
google_drive_method = SendData(data=data)
google_drive_method.post_data()

# Add the information to Google Sheets using the GoogleSheet class
request_method = GoogleSheet(data=data)
request_method.add_info()
