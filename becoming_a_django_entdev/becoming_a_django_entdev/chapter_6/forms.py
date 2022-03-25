from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_email
from django.forms import Form, ModelForm, formset_factory

from ..chapter_3.models import Engine, Seller, Vehicle, Vehicle_Model


class AddEngineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('AddEngineForm Initialized')
        super(AddEngineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'


class EngineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('EngineForm Initialized')
        super(EngineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'


class EngineSuperUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('EngineSuperUserForm Initialized')
        super(EngineSuperUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'


class AddSellerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('AddSellerForm Initialized')
        super(AddSellerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('SellerForm Initialized')
        super(SellerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerSuperUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('SellerSuperUserForm Initialized')
        super(SellerSuperUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seller
        fields = '__all__'
