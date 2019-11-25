import os
SLACK = os.environ.get('SLACK', None)
SENDGRID = os.environ.get('SENDGRID', None)
DEBUG = os.environ.get('DEBUG', 'true') == 'true'
EVENTS_SPREADSHEETS_ID = '1R4KaIWxIWEFOcGP-O8ubPnUq6BnPVj9MVcZSo8D4RW4'
HARDWARELAB_MLHID = 'local-hack-day'

# CORS config

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?hackcu\.org$', r'^(https?://)?localhost(:[0-9]{0,4})?$',)
