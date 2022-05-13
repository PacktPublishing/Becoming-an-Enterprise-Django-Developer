''' Chapter 6 Forms Module '''
#from django import forms
#from django.core.exceptions import ValidationError
#from django.core.validators import EmailValidator, validate_email
from django.forms import (
    #Form,
    ModelForm,
    #formset_factory
)

from ..chapter_3.models import (
    Engine,
    Seller,
    #Vehicle,
    #VehicleModel
)


class AddEngineForm(ModelForm):
    '''
    ModelForm = Add Engine
    '''
    def __init__(self, *args, **kwargs):
        print('AddEngineForm Initialized')
        super(AddEngineForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Add Engine Form Meta Sub-Class
        '''
        model = Engine
        fields = '__all__'


class EngineForm(ModelForm):
    '''
    ModelForm = Change Engine
    '''
    def __init__(self, *args, **kwargs):
        print('EngineForm Initialized')
        super(EngineForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Change Engine Form Meta Sub-Class
        '''
        model = Engine
        fields = '__all__'


class EngineSuperUserForm(ModelForm):
    '''
    ModelForm = Change Engine, with Super User Status
    '''
    def __init__(self, *args, **kwargs):
        print('EngineSuperUserForm Initialized')
        super(EngineSuperUserForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Change Engine, with Super User Status Form Meta Sub-Class
        '''
        model = Engine
        fields = '__all__'


class AddSellerForm(ModelForm):
    '''
    ModelForm = Add Seller
    '''
    def __init__(self, *args, **kwargs):
        print('AddSellerForm Initialized')
        super(AddSellerForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Add Seller Form Meta Sub-Class
        '''
        model = Seller
        fields = '__all__'


class SellerForm(ModelForm):
    '''
    ModelForm = Change Seller
    '''
    def __init__(self, *args, **kwargs):
        print('SellerForm Initialized')
        super(SellerForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Change Seller Form Meta Sub-Class
        '''
        model = Seller
        fields = '__all__'


class SellerSuperUserForm(ModelForm):
    '''
    ModelForm = Change Seller, with Super User Status
    '''
    def __init__(self, *args, **kwargs):
        print('SellerSuperUserForm Initialized')
        super(SellerSuperUserForm, self).__init__(*args, **kwargs)

    class Meta:
        '''
        Change Seller, with Super User Status Form Meta Sub-Class
        '''
        model = Seller
        fields = '__all__'
