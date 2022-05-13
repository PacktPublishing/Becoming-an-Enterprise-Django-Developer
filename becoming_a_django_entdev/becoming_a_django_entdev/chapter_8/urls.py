"""
becoming_a_django_entdev.chapter_8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    include,
    path,
    #re_path,
    #register_converter,
)
from django.views.generic import (
    TemplateView,
    #RedirectView,
)
from rest_framework import routers
from .views import (
    #HelloWorldView,
    EngineViewSet,
    SellerViewSet,
    VehicleViewSet,
    VehicleModelViewSet,
    #GroupViewSet,
    #PermissionViewSet,
    #ContentTypeViewSet,
    GetSellerView,
    GetSellerHTMLView,
    GetSellerWithTokenView
)
# Use if you are still using the Django User model class instead of the Seller model class.
#from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'engines', EngineViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'vehicle-models', VehicleModelViewSet)
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#router.register(r'permissions', PermissionViewSet)
#router.register(r'content-types', ContentTypeViewSet)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        TemplateView.as_view(template_name='chapter_8/index.html')
    ),
    path(
        'chapter-8/',
        include(router.urls)
    ),
    path(
        'api-auth/',
        include('rest_framework.urls')
    ),
    #path(
    #    'chapter-8/hello-world/',
    #    HelloWorldView.as_view(),
    #    name = 'hello-world'
    #),
    path(
        'chapter-8/get-seller/',
        GetSellerView.as_view(),
        name = 'get-seller'
    ),
    path(
        'chapter-8/seller/<int:id>/',
        GetSellerHTMLView.as_view(),
        name = 'seller-detail'
    ),
    path(
        'chapter-8/sellertoken/<int:id>/',
        GetSellerWithTokenView.as_view(),
        name = 'seller-token-detail'
    ),
]
