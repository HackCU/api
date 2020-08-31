# HackCU API supplementary function
# import time
# keep track of time when request is made to return json of the next few events
import csv
from django.http import HttpResponseServerError
from rest_framework.response import Response
import requests

# google sheets export creation in python


def event_parse(sheets_id):
    sheets_url = 'https://docs.google.com/spreadsheets/d/%s/export?format=csv' % sheets_id
    decoded_csv = requests.get(sheets_url).content.decode('utf-8')
    reader = csv.DictReader(decoded_csv.splitlines(), delimiter=',')
    data = {}
    day = None

    for row in reader:

        if row['Start'].startswith("Day "):
            # Day 1 -> day1
            day = row['Start'].replace("Day ", "day")
            data[day] = []
        else:
            if not day:
                return HttpResponseServerError('No day!')
            data[day].append(row)

    return Response(data)
