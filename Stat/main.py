from scipy import stats
import numpy as np
import gspread
from oauth2client.service_account import  ServiceAccountCredentials
import re


np.seterr(divide='ignore', invalid='ignore')
def estimate_cdf (col,bins=10,):
    print (col)
    # 'col'
    # 'bins'

    hist, edges = np.histogram(col)
    csum = np.cumsum(hist)



    return csum/csum[-1], edges
    print (csum)

# link to spreadsheet https://docs.google.com/spreadsheets/d/1_9wfZPiP8cZRZ4FFtAPNcuiygB6oBFthqah5fZS9XMQ/edit?usp=sharing

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("ramp").sheet1  # Opens the spreadhseet

data = sheet.get_all_records()


row = sheet.row_values(3)  # Grab a specific row




number_regex = r'^-?\d+\.?\d*$'





col = sheet.col_values(3)  # Get a specific column print (col)

col2= sheet.col_values(7)
floatdigits= estimate_cdf(adjusted := [float(i) for i in col if re.match(i, number_regex)], len(adjusted))



print(col)
print(col2)




shtest =stats.shapiro(col)
print(shtest)





k2test =stats.ks_2samp(col, lol, alternative='two-sided', mode='auto')
print(k2test)







