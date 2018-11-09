from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from slackclient import SlackClient

# Create your views here.


def _get_client():
    token = getattr(settings, 'SLACK', None)
    if not token:
        raise MethodNotAllowed('Slack Invite', 'Slack token is not set')
    return SlackClient(token)


@api_view(['POST', ])
def slack_invite(request, format='json'):
    """
    Send slack invite. Only POST request. Example body: `{"email":"test@hackcu.org"}`
    """
    email = request.data.get('email', None)
    if not email:
        raise ValidationError('\'email\' field is needed')
    sc = _get_client()
    r = sc.api_call("users.admin.invite", email=email, active=True)
    return Response(r)
