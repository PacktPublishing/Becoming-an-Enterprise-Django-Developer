from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EngineSerializer, SellerSerializer, VehicleSerializer, Vehicle_ModelSerializer, GroupSerializer, PermissionSerializer, ContentTypeSerializer
#from .serializers import UserSerializer
from ..chapter_3.models import Engine, Seller, Vehicle, Vehicle_Model


class EngineViewSet(ModelViewSet):
    '''
    API endpoint that allows Engine to be viewed or edited.
    '''
    queryset = Engine.objects.all().order_by('name')
    serializer_class = EngineSerializer
    permission_classes = [
        IsAuthenticated
    ]


class Vehicle_ModelViewSet(ModelViewSet):
    '''
    API endpoint that allows Vehicle_Model to be viewed or edited.
    '''
    queryset = Vehicle_Model.objects.all().order_by('name')
    serializer_class = Vehicle_ModelSerializer
    permission_classes = [
        IsAuthenticated
    ]


class VehicleViewSet(ModelViewSet):
    '''
    API endpoint that allows Vehicle to be viewed or edited.
    '''
    queryset = Vehicle.objects.all().order_by('price')
    serializer_class = VehicleSerializer
    permission_classes = [
        IsAuthenticated
    ]


class SellerViewSet(ModelViewSet):
    '''
    API endpoint that allows Seller to be viewed or edited.
    '''
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [
        IsAuthenticated
    ]


# Optional View - Needed if you are logged in with a user/seller who has Group or Permission related objects.
#class UserViewSet(ModelViewSet):
#    '''
#    API endpoint that allows User to be viewed or edited.
#    '''
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [
#        IsAuthenticated
#    ]


# Optional View - Needed if you are logged in with a user/seller who has Group or Permission related objects.
class GroupViewSet(ModelViewSet):
    '''
    API endpoint that allows Group to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthenticated
    ]


# Optional View - Needed if you are logged in with a user/seller who has Group or Permission related objects.
class PermissionViewSet(ModelViewSet):
    '''
    API endpoint that allows Permission to be viewed or edited.
    '''
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [
        IsAuthenticated
    ]


# Optional View - Needed if you are logged in with a user/seller who has Group or Permission related objects and the user/seller serializer has a Meta depth property >= 2
class ContentTypeViewSet(ModelViewSet):
    '''
    API endpoint that allows ContentType to be viewed or edited.
    '''
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [
        IsAuthenticated
    ]


class GetSellerView(View):
    '''
    This is a custom view used to get Seller data by ID using an input field to capture that ID by the User.
    '''
    template_name = 'chapter_8/spa_pages/get_seller.html'

    def get(self, request, *args, **kwargs):
        context = {
            'custom_message': 'Extra Context Goes Here'
        }

        #print(context)

        return TemplateResponse(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Not Used In This View
        pass


class GetSellerHTMLView(View):
    '''
    This is an AJAX only view.
    Used to serve up the Seller with the id provided and rendered as preformatted HTML
    '''
    template_name = 'chapter_8/details/seller.html'

    def get(self, request, id, *args, **kwargs):
        print('ID = ', id)
        print(type(id))

        print('User = ', request.user)
        print('Is User Authenticated ', request.user.is_authenticated)
        print('Does User Have Permission? ', request.user.has_perm('chapter_3.view_seller'))

        if request.user.is_authenticated and request.user.has_perm('chapter_3.view_seller'):
            print('AUTHENTICATED')
            
            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                print('SELLER NOT FOUND')
                seller = None
        else:
            print('NOT AUTHENTICATED')
            seller = None

        context = {
            'seller': seller,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        # Not Used In This View
        pass


class HelloWorldView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class GetSellerWithTokenView(APIView):
    '''
    This is an AJAX only view.
    Used to serve up the Seller with the id provided and rendered as preformatted HTML
    This also uses an Authentication token that is needed for security measures.
    '''
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
    template_name = 'chapter_8/details/seller.html'

    def get(self, request, format=None, id=0, *args, **kwargs):
        print(request.__dict__)
        print('id = ', id)
        print('request.user = ',request.user)
        print('request.auth = ', request.auth)
        print('format = ', format)
        print('HTTP_USER = ', request.META['HTTP_USER'])
        print('HTTP_AUTHORIZATION = ', request.META['HTTP_AUTHORIZATION'])

        req_username = request.META['HTTP_USER']

        try:
            req_user = Seller.objects.get(username=req_username)
        except Seller.DoesNotExist:
            print('REQ USER NOT FOUND')
            req_user = None
            seller = None
        else:
            if req_user.has_perm('chapter_3.view_seller'):
                print('PERM CHECK PERMITTED')

                try:
                    seller = Seller.objects.get(id=id)
                except Seller.DoesNotExist:
                    print('SELLER NOT FOUND')
                    seller = None
            else:
                print('PERM CHECK NOT PERMITTED')
                seller = None

        context = {
            'seller': seller,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        # Not Used In This View
        pass


# Same as the GetSellerView class but in method form.
def get_seller(request):
    '''
    This is a custom view used to get Seller data by ID using an input field to capture that ID by the User.
    '''
    return render(request, 'chapter_8/spa_pages/get_seller.html', context={})


# Same as the GetSellerHTMLView class but in method form
def seller_HTML(request, id):
    '''
    This is an AJAX only view.
    Used to serve up the Seller with the id provided
    '''
    print(id)
    print(type(id))

    seller = Seller.objects.get(id=id)

    context = {
        'seller': seller,
    }

    return render(request, 'chapter_8/details/seller.html', context=context)