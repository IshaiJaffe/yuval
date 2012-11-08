
from django.conf import settings # import the settings file

import os
BABLIC_SNIPPET = os.environ.get('BABLIC_SNIPPET','')

def bablic(request):
    return {'BABLIC_SNIPPET': BABLIC_SNIPPET, 'locale': BABLIC_SNIPPET and request.session and request.session.get('locale')}
