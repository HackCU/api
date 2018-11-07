# HACK CU Api supplementary function
import requests
import json
import time
# keep track of time when request is made to return json of the next few events
import pandas as pd

# google sheets export creation in python
def sheet():
    # need to export json   
    sheetURL = "https://docs.google.com/spreadsheets/d/1MkLve58YjYuJdRrmG8-7rpTCaa7v9mspzmMninApx5g/export?format=csv"
    # export csv link for the schedule
    df = pd.read_csv(sheetURL)
    x = df.index[df['Start'] == 'Day 2'].tolist()[0]
    d1 = (df.iloc[0:x])
    d2 = (df.iloc[x+2:])
    ret = {'events': []}
    first = d1.T.to_dict()
    second = d2.T.to_dict()
    for i in first:
        ret['events'].append(first[i])
    for i in second:
        ret['events'].append(second[i])

    return ret

# slower way (commented out) - Google Sheets api
'''
f = time.time()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.


sheet = client.open("live_schedule").sheet1

# Extract and print all of the values

all_cells = sheet.range('A1:C19')
b = time.time()
print(b-f)
for i in all_cells:
    print(i.value)
'''
