# from django.conf import settings
from django.conf import settings
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sheets import spreadsheet


@cache_page(60 * 3)
# name is in first column
@api_view(['GET', ])
# takes care of any invalid responses
def events(request, format='json'):
    res = spreadsheet.event_parse(settings.EVENTS_SPREADSHEETS_ID)
    return Response(res)

# straightforward API
# return a JsonResponse here based on the result of the request to the live page.
