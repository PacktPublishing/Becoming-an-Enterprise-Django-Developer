from django.conf import settings

def global_context(request):
    return {
        'base_url': request.build_absolute_uri('/')[:-1].strip('/'),                # E.g. http://localhost:8000

        # Additional Practice
        'absolute_full': request.build_absolute_uri().partition('?')[0].strip('/'), # E.g. http://localhost:8000/sub-page
        'debug': settings.DEBUG,
    }
