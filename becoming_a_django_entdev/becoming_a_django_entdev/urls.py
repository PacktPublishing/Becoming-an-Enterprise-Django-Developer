"""
becoming_a_django_entdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, register_converter
from django.views.generic import TemplateView, RedirectView
from . import converters
from .chapter_4 import views
from .chapter_4.views import TestPage_View, VehicleView, VehicleView2


# CHAPTERS 1, 2 & 3 - Use this variable and comment out the rest
#urlpatterns = []


# CHAPTER 4 - Use these variables and comment out the rest
register_converter(converters.YearConverter, 'year')

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # Global Favicon Path Enabled
    re_path(r'^favicon\.ico$', favicon_view), # Can Still Use "<link rel="icon" href="{% static 'app_name/sub_folder/images/favicon.ico' %}">" For Custom Sub Page Favicons

    path('', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('', TemplateView.as_view(template_name='chapter_4/index.html'), kwargs={'sub_title': 'I am the sub title.'}),
    path('admin/', admin.site.urls),
    #path('my_path/my_unwanted_url/', RedirectView.as_view(url='http://localhost:8000/my_wanted_url/', permanent=True)),
    #path('my_path/<path:my_pattern>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_path/<path:my_pattern>/', TemplateView.as_view(template_name='chapter_4/index.html'), kwargs={'sub_title': 'My new subtitle.'}),
    #re_path(r'^my_path/(?P<slug>[0-9A-Za-z-_.//]+)/$', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/2022/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/<int:my_year>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #path('my_year_path/<year>/', TemplateView.as_view(template_name='chapter_4/index.html')),
    #re_path('my_year_path/(?P<year>[0-9]{4})/$', TemplateView.as_view(template_name='chapter_4/index.html')),
    #re_path('my_year_path/(?P<year>[0-9]{4})/$', views.practice_year_view),
    #path('my_year_path/<year:year>/', views.practice_view),
    #path('my_year_path/<year:year>/', views.practice_year_view),
    #path('my_year_path/<year:year>/', views.practice_year_view, name='year_url'),
    #re_path(r'^my_year_path/(?P<year:year>[0-9]+)/?$', views.practice_view),
    #path('vehicle/<int:id>/', views.vehicle_view, name='vehicle-detail'),
    #path('vehicle/<str:vin>/', views.vehicle_view, name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView.as_view(), name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView.as_view(template_name='chapter_4/my_vehicle_class_2.html'), name='vehicle-detail'),
    #path('vehicle/<int:id>/', VehicleView2.as_view(), name='vehicle-detail'),
    #path('test_page_1/', TestPage_View.as_view(), name='test-page'),
    #path('', include('becoming_a_django_entdev.chapter_4.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# CHAPTER 5 - Use these variables and comment out the rest
# Using the import statement allows us to bundle all future chapters in a clean way just like chapter 5. Whereas chapter 4 we were still explaining core concepts using this file before we introduced this way of organizing URL patterns.
urlpatterns = [
    path('', include('becoming_a_django_entdev.chapter_5.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# CHAPTER 9 - Used when discussing the Django Debug Toolbar, this is turned on throughout all chapters to allow the writer and the testers to use it and make sure things are working properly but this tool is not revealed to the reader until Chapter 9
# Debug/Development Mode Only
if settings.DEBUG:
    import debug_toolbar

    # Django Debug Toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
