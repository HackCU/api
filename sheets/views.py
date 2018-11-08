
# from django.conf import settings
from rest_framework.decorators import api_view
import sheets.spreadsheet as ss
from django.http import JsonResponse


# name is in first column
@api_view(['GET', ])
# takes care of any invalid responses
def eventsRep(request):
    res = ss.sheet()
    return JsonResponse(res)
# straightforward API
# return a JsonResponse here based on the result of the request to the live page.
