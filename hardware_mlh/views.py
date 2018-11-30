import requests
from django.conf import settings
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response


@cache_page(60 * 5)
# name is in first column
@api_view(['GET', ])
# takes care of any invalid responses
def hardware_items(request, format='json'):
    res = requests.get('https://hardware.mlh.io/events/%s.json' % settings.HARDWARELAB_MLHID)
    return Response(res.json(), status=res.status_code)
