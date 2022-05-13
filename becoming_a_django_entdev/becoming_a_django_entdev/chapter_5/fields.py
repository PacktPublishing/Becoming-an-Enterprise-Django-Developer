''' Chapter 5 Fields Module '''
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms.fields import Field
from django.forms.widgets import (
    #FILE_INPUT_CONTRADICTION,
    #CheckboxInput,
    #ClearableFileInput,
    #DateInput,
    #DateTimeInput,
    #EmailInput,
    #FileInput,
    #HiddenInput,
    #MultipleHiddenInput,
    #NullBooleanSelect,
    #NumberInput,
    #Select,
    #SelectMultiple,
    #SplitDateTimeWidget,
    #SplitHiddenDateTimeWidget,
    #Textarea,
    TextInput,
    #TimeInput,
    #URLInput,
)


class MultipleEmailField(Field):
    '''
    Custom Multiple Email Field class
    '''
    widget = TextInput
    default_validators = []
    default_error_messages = {
        'required': 'Default Required Error Message',
        'email': 'Please enter a valid email address or addresses separated by a comma with ' \
            'NO spaces'
    }

    def to_python(self, value):
        '''
        Converts data to a list of strings, one string for each value separated by a comma
        '''
        if not value:
            return []

        value = value.replace(' ', '')

        return value.split(',')

    def validate(self, value):
        '''
        Performs self validation on each comma separated email address using the
        validate_email() function
        '''
        super().validate(value)

        for email in value:
            #validate_email(email)

            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError(self.error_messages['email'], code='email')
