''' Chapter 5 Forms Module '''
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_email
from django.forms import Form, ModelForm, formset_factory

from .fields import MultipleEmailField
from ..chapter_3.models import Vehicle


class ContactForm(Form):
    '''
    Form Object Class to capture contact form submissions.
    '''

    #pass
    template_name = 'chapter_5/forms/custom-form.html'
    success_url = '/default-contact-success/'

    full_name = forms.CharField(
        label = 'Full Name',
        widget = forms.TextInput(
            attrs = {
                'id': 'full-name',
                'class': 'form-input-class',
                'placeholder': 'Your Name, Written By...'
            }
        ),
        help_text = 'Enter your full name, first and last name please',
        min_length = 2,
        max_length = 300,
        required = True,
        error_messages = {
            'required': 'Please provide us with a name to address you as',
            'min_length': 'Please lengthen your name, min 2 characters',
            'max_length': 'Please shorten your name, max 300 characters'
        }
    )
    email_1 = forms.CharField(
        label = 'email_1 Field',
        min_length = 5,
        max_length = 254,
        required = False,
        help_text = 'Email address in example@example.com format for contacting you should we ' \
            'have questions about your message.',
        validators = [
            EmailValidator('Please enter a valid email address'),
        ],
        error_messages = {
            'min_length': 'Please lengthen your name, min 5 characters',
            'max_length': 'Please shorten your name, max 254 characters'
        }
    )
    email_2 = forms.EmailField(
        label = 'email_2 Field',
        min_length = 5,
        max_length = 254,
        required = True,
        help_text = 'Email address in example@example.com format for contacting you should we ' \
            'have questions about your message.',
        error_messages = {
            'required': 'Please provide us an email address should we need to reach you',
            'email': 'Please enter a valid email address',
            'min_length': 'Please lengthen your name, min 5 characters',
            'max_length': 'Please shorten your name, max 254 characters'
        }
    )
    email_3 = forms.CharField(
        label = 'email_3 Field',
        min_length = 5,
        max_length = 254,
        required = False,
        help_text = 'Email address in example@example.com format for contacting you should we ' \
            'have questions about your message.',
        error_messages = {
            'min_length': 'Please lengthen your name, min 5 characters',
            'max_length': 'Please shorten your name, max 254 characters'
        }
    )
    conditional_required = forms.CharField(
        label = 'Required only if field labeled "email_3" has a value',
        widget = forms.TextInput(
            attrs = {
                'id': 'required-test-field',
                'class': 'form-input-class',
                'placeholder': 'Enter Any Value...'
            }
        ),
        help_text = 'This field is only required if the field labeled "email_3 Field" has a value',
        min_length = 2,
        max_length = 100,
        required = False,
        error_messages = {
            'min_length': 'Please lengthen your name, min 2 characters',
            'max_length': 'Please shorten your name, max 100 characters'
        }
    )
    multiple_emails = MultipleEmailField(
        label = 'Multiple Email Field',
        help_text = 'Please enter one or more email addresses, each separated by a comma with ' \
            'NO spaces',
        required = True,
        error_messages = {
            #'required': 'This multiple_emails field is required.',,
            #'email': 'Custom email message, overrides default_error_messages'
        }
    )

    # Extra Practice - Text Area Field
    message = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(
            attrs = {'rows': 10, 'cols': 50}
        ),
        required = True,
        help_text = 'Please provide a message',
        max_length = 5000,
        error_messages = {
            'required': 'Please provide us a message',
            'max_length': 'Please shorten your name, max 5000 characters'
        }
    )

    def __init__(self, *args, **kwargs):
    #def __init__(self, excluded, *args, **kwargs):
        '''
        Initialize Form Fields
        '''
        super(ContactForm, self).__init__(*args, **kwargs)
        #self.error_class = DivErrorList

        #for field in excluded:
        #    try:
        #        del self.fields[field]
        #    except KeyError as e:
        #        print('Field %s does not exist' % str(e))

    def is_valid(self):
        '''
        Add Error Class to Field Objects
        '''
        ret = forms.Form.is_valid(self)

        for f in self.errors:
            self.fields[f].widget.attrs.update(
                {'class': self.fields[f].widget.attrs.get('class', '') + ' field-error'}
            )

        return ret

    def clean(self):
        '''
        Validation - Compares Two or More Fields Against Each Other
        '''
        #print('clean()')
        #print(self.data)
        #print(self.cleaned_data)

        # Instead of writing self.cleaned_data over and over again, this can also be written as.
        #cleaned_data = super().clean()
        #print(cleaned_data)

        email = self.cleaned_data['email_3']
        text_field = self.cleaned_data['conditional_required']

        # For a more fail-safe approach with more checks and balances, use the example below
        #email = ''
        #text_field = ''

        #if 'email_3' in self.cleaned_data and self.cleaned_data['email_3'] != '':
        #    email = self.cleaned_data['email_3']

        #    if (
        #        'conditional_required' in self.cleaned_data and
        #        self.cleaned_data['conditional_required'] != ''
        #    ):
        #        text_field = self.cleaned_data['conditional_required']

        if email and not text_field:
            self.add_error(
                'conditional_required',
                'If there is a value in the field labeled "email_3" then this field is required'
            )

    # Validation - Compares a Single Field Only
    def clean_email_3(self):
        '''
        Validation - Compares a Single Field Only - email_3 field.
        '''
        #print('clean_email_3() Fired')
        #print(self.data)
        #print(self.cleaned_data)

        email = self.cleaned_data['email_3']

        if email != '':
            try:
                validate_email(email)
            except ValidationError:
                self.add_error(
                    'email_3',
                    f'The following is not a valid email address: {email}'
                )
                #raise ValidationError(
                #    'The following is not a valid email address: {0}'.format(email)
                #)
        else:
            self.add_error('email_3', 'This field is required')
            #raise ValidationError('This field is required')

        return email


class VehicleForm(ModelForm):
    '''
    Form Object Class to capture vehicle form submissions.
    '''

    #pass
    #template_name = 'chapter_5/forms/custom-model-form.html'

    class Meta:
        '''
        Vehicle Form Meta Sub-Class
        '''
        model = Vehicle
        fields = [
            'vin',
            'sold',
            'price',
            'make',
            'vehicle_model',
            'engine',
        ]


class ProspectiveBuyerForm(Form):
    '''
    Form Object Class to capture prospective buyers form submissions.
    '''
    first_name = forms.CharField(
        label = 'First Name',
        widget = forms.TextInput(
            attrs = {
                'id': 'first-name',
                'class': 'form-input-class',
                'placeholder': 'First Name, Prospective Buyer'
            }
        ),
        help_text = 'Enter your first name only',
        min_length = 2,
        max_length = 300,
        required = True,
        error_messages = {
            'required': 'Please provide us with a first name',
            'min_length': 'Please lengthen your name, min 2 characters',
            'max_length': 'Please shorten your name, max 300 characters'
        }
    )
    last_name = forms.CharField(
        label = 'Last Name',
        widget = forms.TextInput(
            attrs = {
                'id': 'last-name',
                'class': 'form-input-class',
                'placeholder': 'Last Name, Prospective Buyer'
            }
        ),
        help_text = 'Enter your last name only',
        min_length = 2,
        max_length = 300,
        required = True,
        error_messages = {
            'required': 'Please provide us with a last name',
            'min_length': 'Please lengthen your name, min 2 characters',
            'max_length': 'Please shorten your name, max 300 characters'
        }
    )


ProspectiveBuyerFormSet = formset_factory(
    ProspectiveBuyerForm,
    extra = 1
)
