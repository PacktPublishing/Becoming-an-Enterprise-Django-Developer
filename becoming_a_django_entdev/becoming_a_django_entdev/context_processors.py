from django.conf import settings

def global_context(request):
    return {
        'base_url': request.build_absolute_uri('/')[:-1].strip('/'),           # E.g. http://localhost:8000
        'absolute_full': request.build_absolute_uri().partition('?')[0].strip('/'), # E.g. http://localhost:8000/about-corcoran-pacific-properties
        'debug': settings.DEBUG,
    }
