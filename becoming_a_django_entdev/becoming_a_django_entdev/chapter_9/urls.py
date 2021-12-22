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
from django.urls import include, path, re_path, register_converter
from django.views.generic import TemplateView, RedirectView
from rest_framework import routers
from ..chapter_4.converters import YearConverter
from ..chapter_4.views import practice_year_view, VehicleView


register_converter(YearConverter, 'year')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='chapter_9/index.html')),
    path('my_year_path/<year:year>/', practice_year_view, name='year_url'),
    path('vehicle/<int:id>/', VehicleView.as_view(), name='vehicle-detail'),
]
