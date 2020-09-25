from scipy.stats import kstest
import numpy as np
import gspread
from oauth2client.service_account import  ServiceAccountCredentials
import re


def estimate_cdf (col,bins=10,):
    print (col)
    # 'col'
    # 'bins'

    hist, edges = np.histogram(col)
    csum = np.cumsum(hist)



    return csum/csum[-1], edges

# link to spreadsheet https://docs.google.com/spreadsheets/d/1_9wfZPiP8cZRZ4FFtAPNcuiygB6oBFthqah5fZS9XMQ/edit?usp=sharing

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("ramp").sheet1  # Opens the spreadhseet

data = sheet.get_all_records()


row = sheet.row_values(3)  # Grab a specific row




number_regex = r'^-?\d+\.?\d*$'

# python3.8+?



col = sheet.col_values(3)  # Get a specific column print (col)
dolphin= estimate_cdf(adjusted := [float(i) for i in col if re.match(i, number_regex)], len(adjusted))

print(col)


cell = sheet.cell(1,2).value  # Grab the value of a specific cell

cdf, values = estimate_cdf(col, bins=len(col))
teststat = kstest(values, cdf)


