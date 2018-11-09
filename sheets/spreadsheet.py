# CU Api supplementary function
# import time
# keep track of time when request is made to return json of the next few events
# import pandas as pd
import csv

import requests

# use the csv module here!
# google sheets export creation in python


def event_parse(sheets_id):
    sheets_url = 'https://docs.google.com/spreadsheets/d/%s/export?format=csv' % sheets_id
    decoded_csv = requests.get(sheets_url).content.decode('utf-8')
    reader = csv.DictReader(decoded_csv.splitlines(), delimiter=',')
    r = {'day1': [], 'day2': []}
    day = 'day1'

    for row in reader:

        if row['Start'] == "Day 2":
            day = 'day2'
            continue

        if row['Start'] == "Start":
            continue

        r[day].append(row)
    return r
