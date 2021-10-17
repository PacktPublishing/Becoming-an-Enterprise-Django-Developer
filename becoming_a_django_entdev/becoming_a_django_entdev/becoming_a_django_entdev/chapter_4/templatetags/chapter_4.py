from django.template import Library


register = Library()


@register.filter(name='vehicle_make')
def vehicle_make(value):
    '''
    Takes in a numeric (int) ID and returns a string representation of that value
    '''
    from ...chapter_3.models import MAKE_CHOICES

    print(value)
    print(MAKE_CHOICES)

    for i, choice in enumerate(MAKE_CHOICES):
        print(i)
        print(choice)

        if i == value:
            try:
                print(choice[1])
                return choice[1]
            except ValueError:
                pass

    return ''
