from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed, ValidationError
import requests

# Create your views here.

HACKCU_INTEREST_LIST = '2876597'
ADD_URL = "https://api.sendgrid.com/v3/contactdb/recipients"
LIST_URL = "https://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}"


@api_view(['POST', ])
def sendgrid_events(request):
    """
    Add email to promotional events sendgrid list. Example body: `{"email":"test@hackcu.org"}`
    """
    email = request.data.get('email', None)
    if not email:
        raise ValidationError('\'email\' field is needed')

    token = getattr(settings, 'SENDGRID', '')
    if not token:
        raise MethodNotAllowed('Sendgrid Events', 'Sendgrid token is not set')

    header = {'Authorization': "Bearer " + token}
    data = [{"email": email}]
    response = requests.post(ADD_URL, headers=header, json=data)
    recipient = response.json().get('persisted_recipients', [None, ])[0]
    if not recipient:
        Response({'ok':False, 'message':'Not able to connect'})
    requests.post(LIST_URL.format(list_id=HACKCU_INTEREST_LIST, recipient_id=recipient),
                  headers=header)
    return Response({'ok':True, 'message':'Added successfully'})
