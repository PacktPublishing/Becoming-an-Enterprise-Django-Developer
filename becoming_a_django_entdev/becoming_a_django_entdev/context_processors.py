''' Global Context Processors Module '''
from django.conf import settings

def global_context(request):
    '''
    Global Context Method - Returns Common Items
    '''
    return {
        # E.g. http://localhost:8000
        'base_url': request.build_absolute_uri('/')[:-1].strip('/'),

        # Additional Practice
        # E.g. http://localhost:8000/sub-page
        'absolute_full': request.build_absolute_uri().partition('?')[0].strip('/'),
        'debug': settings.DEBUG,
    }
