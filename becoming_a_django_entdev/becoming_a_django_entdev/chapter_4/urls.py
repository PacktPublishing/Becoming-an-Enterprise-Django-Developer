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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path, register_converter
from django.views.generic import TemplateView, RedirectView

from .converters import YearConverter
from .views import TestPageView, VehicleView, VehicleView2, practice_year_view, practice_view, vehicle_view


register_converter(YearConverter, 'year')

urlpatterns = [
    path('', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('', TemplateView.as_view(template_name='chapter_4/index.html'), kwargs={'sub_title': 'I am the sub title.'}),
    #path('chapter-4/', TemplateView.as_view(template_name='chapter_4/chapter_4.html')),

    #path('chapter-4/', HttpResponse('This is the Chapter 4 Page')),
    #path('my_path/my_unwanted_url/', RedirectView.as_view(url='http://localhost:8000/my_wanted_url/', permanent=True)),
    #path('my_path/<path:my_pattern>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_path/<path:my_pattern>/', TemplateView.as_view(template_name='chapter_4/index.html'), kwargs={'sub_title': 'My new subtitle.'}),
    #re_path(r'^my_path/(?P<slug>[0-9A-Za-z-_.//]+)/$', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/2022/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/<int:my_year>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/<year>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #re_path('my_year_path/(?P<year>[0-9]{4})/$', TemplateView.as_view(template_name='chapter_4/index.html')),
    #re_path('my_year_path/(?P<year>[0-9]{4})/$', practice_year_view),
    #path('my_year_path/<year:year>/', practice_view),
    #path('my_year_path/<year:year>/', practice_year_view),
    #path('my_year_path/<year:year>/', practice_year_view, name='year_url'),
    #re_path(r'^my_year_path/(?P<year:year>[0-9]+)/?$', practice_view),
    #path('vehicle/<int:id>/', vehicle_view, name='vehicle-detail'),
    #path('vehicle/<str:vin>/', vehicle_view, name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView.as_view(), name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView.as_view(template_name='chapter_4/my_vehicle_class_2.html'), name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView2.as_view(), name='vehicle-detail'),
    #path('test_page_1/', TestPageView.as_view(), name='test-page'),
    #path('vehicle/', VehicleView.as_view(), name='vehicle-detail'),
]
