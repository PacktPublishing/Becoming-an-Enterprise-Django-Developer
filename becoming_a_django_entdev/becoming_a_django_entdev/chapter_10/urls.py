"""
becoming_a_django_entdev.chapter_4 URL Configuration

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
from django.urls import path
from django.views.generic import TemplateView

from .views import SellersView, VehiclesView, VehicleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='chapter_10/index.html')),

    path('all-vehicles/', VehiclesView.as_view(), name='all-vehicles'),
    path('all-sellers/', SellersView.as_view(), name='all-sellers'),
    path('vehicle/<int:id>/', VehicleView.as_view(), name='vehicle-detail'),
]
