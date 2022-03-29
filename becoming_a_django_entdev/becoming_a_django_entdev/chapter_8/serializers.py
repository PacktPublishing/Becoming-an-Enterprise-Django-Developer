from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from ..chapter_3.models import Seller, Vehicle, Engine, Vehicle_Model


class EngineSerializer(ModelSerializer):
#class EngineSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Engine
        #fields = ['name', 'vehicle_model']
        fields = '__all__'
        #depth = 3


class Vehicle_ModelSerializer(ModelSerializer):
#class Vehicle_ModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle_Model
        #fields = ['name', 'make']
        fields = '__all__'
        #depth = 3


class VehicleSerializer(ModelSerializer):
#class VehicleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        #fields = ['vin', 'sold', 'price', 'make', 'vehicle_model', 'engine']
        fields = '__all__'
        #depth = 3


class SellerSerializer(ModelSerializer):
#class SellerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        #fields = ['name', 'vehicles']
        fields = '__all__'
        #depth = 3


#class UserSerializer(ModelSerializer):
#class UserSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = '__all__'
#        depth = 3


#class GroupSerializer(ModelSerializer):
#class GroupSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = '__all__'
#        depth = 3


##class PermissionSerializer(ModelSerializer):
#class PermissionSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = Permission
#        fields = '__all__'
#        depth = 3


##class ContentTypeSerializer(ModelSerializer):
#class ContentTypeSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = ContentType
#        fields = '__all__'
#        depth = 3
