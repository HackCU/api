import os
SLACK = os.environ.get('SLACK', None)
DEBUG = os.environ.get('DEBUG', 'true') == 'true'
