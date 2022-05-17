''' Chapter 8 Serializer Module '''
#from django.contrib.auth.models import Group, Permission, User
#from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)
from ..chapter_3.models import Seller, Vehicle, Engine, VehicleModel


#class EngineSerializer(ModelSerializer):
class EngineSerializer(HyperlinkedModelSerializer):
    '''
    Serializer for Engine Model
    '''
    class Meta:
        '''
        Meta Sub-Class for Engine Model Serializer
        '''
        model = Engine
        #fields = ['name', 'vehicle_model']
        fields = '__all__'
        #depth = 3


#class VehicleModelSerializer(ModelSerializer):
class VehicleModelSerializer(HyperlinkedModelSerializer):
    '''
    Serializer for VehicleModel Model
    '''
    class Meta:
        '''
        Meta Sub-Class for VehicleModel Model Serializer
        '''
        model = VehicleModel
        #fields = ['name', 'make']
        fields = '__all__'
        #depth = 3


#class VehicleSerializer(ModelSerializer):
class VehicleSerializer(HyperlinkedModelSerializer):
    '''
    Serializer for Vehicle Model
    '''
    class Meta:
        '''
        Meta Sub-Class for Vehicle Model Serializer
        '''
        model = Vehicle
        #fields = ['vin', 'sold', 'price', 'make', 'vehicle_model', 'engine']
        fields = '__all__'
        #depth = 3


#class SellerSerializer(ModelSerializer):
class SellerSerializer(HyperlinkedModelSerializer):
    '''
    Serializer for Seller Model
    '''
    class Meta:
        '''
        Meta Sub-Class for Seller Model Serializer
        '''
        model = Seller
        #fields = ['name', 'vehicles']
        #fields = '__all__'
        exclude = ['groups', 'user_permissions']
        #depth = 3


#class UserSerializer(ModelSerializer):
#class UserSerializer(HyperlinkedModelSerializer):
#    '''
#    Serializer for User Model
#    '''
#    class Meta:
#        '''
#        Meta Sub-Class for User Model Serializer
#        '''
#        model = User
#        fields = '__all__'
#        #depth = 3


#class GroupSerializer(ModelSerializer):
#class GroupSerializer(HyperlinkedModelSerializer):
#    '''
#    Serializer for Group Model
#    '''
#    class Meta:
#        '''
#        Meta Sub-Class for Group Model Serializer
#        '''
#        model = Group
#        fields = '__all__'
#        #depth = 3


##class PermissionSerializer(ModelSerializer):
#class PermissionSerializer(HyperlinkedModelSerializer):
#    '''
#    Serializer for Permission Model
#    '''
#    class Meta:
#        '''
#        Meta Sub-Class for Permission Model Serializer
#        '''
#        model = Permission
#        fields = '__all__'
#        #depth = 3


##class ContentTypeSerializer(ModelSerializer):
#class ContentTypeSerializer(HyperlinkedModelSerializer):
#    '''
#    Serializer for ContentType Model
#    '''
#    class Meta:
#        '''
#        Meta Sub-Class for ContentType Model Serializer
#        '''
#        model = ContentType
#        fields = '__all__'
#        #depth = 3
