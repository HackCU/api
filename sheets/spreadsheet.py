# CU Api supplementary function
# import time
# keep track of time when request is made to return json of the next few events
# import pandas as pd
import csv
import requests
# use the csv module here!
# google sheets export creation in python


def sheet():
    sheetsURL = 'https://docs.google.com/spreadsheets/d/1MkLve58YjYuJdRrmG8-7rpTCaa7v9mspzmMninApx5g/export?format=csv'
    with requests.Session() as s:
        received = s.get(sheetsURL)
        decoded_csv = received.content.decode('utf-8')
        creader = csv.DictReader(decoded_csv.splitlines(), delimiter=',')
        my_list = list(creader)
        sheets = {'day1': [], 'day2': []}
        day1 = True
        for row in my_list:
            x = dict(row)
            if x['Start'] == "Day 2":
                day1 = False
            elif x['Start'] != "Start":
                if x['Location'] == "":
                    x['Location'] = "Idea Forge"
                if day1:
                    sheets['day1'].append(x)
                else:
                    sheets['day2'].append(x)
        return sheets

        '''
        pandas method
        # need to export json
        # export csv link for the schedule
        df = pd.read_csv(sheetURL)
        x = df.index[df['Start'] == 'Day 2'].tolist()[0]
        d1 = (df.iloc[0:x])
        d2 = (df.iloc[x + 2:])
        ret = {'events': []}
        first = d1.T.to_dict()
        second = d2.T.to_dict()
        print(second)
        for i in first:
            ret['events'].append(first[i])
        for i in second:
            ret['events'].append(second[i])
        print(ret)
        return ret'''
# slower way (commented out) - Google Sheets api
