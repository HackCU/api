import os
SLACK = os.environ.get('SLACK', None)
SENDGRID = os.environ.get('SENDGRID', None)
DEBUG = os.environ.get('DEBUG', 'true') == 'true'

# CORS config

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?hackcu\.org$', )
