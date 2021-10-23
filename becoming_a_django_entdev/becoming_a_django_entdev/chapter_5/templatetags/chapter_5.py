from django.template import Library


register = Library()


@register.filter('class_name')
def class_name(obj):
    return obj.__class__.__name__
