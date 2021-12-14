"""
becoming_a_django_entdev.chapter_5 URL Configuration

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


from .views import FormClass_View, ModelFormClass_CreateView, ModelFormClass_UpdateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='chapter_5/index.html')),

    #path('chapter-5/form-class', FormClass_View.as_view(template_name='chapter_5/form-class.html')), # Non-Forward Slash Only
    #path('chapter-5/form-class/', FormClass_View.as_view(template_name='chapter_5/form-class.html')), # Forward Slash Only
    re_path(r'^chapter-5/form-class/?$', FormClass_View.as_view(template_name='chapter_5/form-class.html')), # Accepts Both Forward Slash and Non-Forward Slash
    #path('chapter-5/contact-form-success', TemplateView.as_view(template_name='chapter_5/contact-success.html')), # Non-Forward Slash Only
    #path('chapter-5/contact-form-success/', TemplateView.as_view(template_name='chapter_5/contact-success.html')), # Forward Slash Only
    re_path(r'^chapter-5/contact-form-success/?$', TemplateView.as_view(template_name='chapter_5/contact-success.html'), kwargs={
        'title': 'FormClass_View Success Page',
        'page_id': 'form-class-success',
        'page_class': 'form-class-success-page',
        'h1_tag': 'This is the FormClass_View Success Page Using ContactForm',
    }), # Accepts Both Forward Slash and Non-Forward Slash
    #path('chapter-5/model-form-class', ModelFormClass_CreateView.as_view(template_name='chapter_5/model-form-class.html')), # Non-Forward Slash Only
    #path('chapter-5/model-form-class/', ModelFormClass_CreateView.as_view(template_name='chapter_5/model-form-class.html')), # Forward Slash Only
    re_path(r'^chapter-5/model-form-class/?$', ModelFormClass_CreateView.as_view(template_name='chapter_5/model-form-class.html')), # Accepts Both Forward Slash and Non-Forward Slash
    #re_path('chapter-5/model-form-class/(?P<id>[0-9])', ModelFormClass_UpdateView.as_view(template_name='chapter_5/model-form-class.html'), name='vehicle_detail'), # Non-Forward Slash Only
    #re_path('chapter-5/model-form-class/(?P<id>[0-9])/', ModelFormClass_UpdateView.as_view(template_name='chapter_5/model-form-class.html'), name='vehicle_detail'), # Forward Slash Only
    re_path('chapter-5/model-form-class/(?P<id>[0-9])/?$', ModelFormClass_UpdateView.as_view(template_name='chapter_5/model-form-class.html'), name='vehicle_detail'), # Accepts Both Forward Slash and Non-Forward Slash
    #path('chapter-5/vehicle-form-success', TemplateView.as_view(template_name='chapter_5/vehicle-success.html')), # Non-Forward Slash Only
    #path('chapter-5/vehicle-form-success/', TemplateView.as_view(template_name='chapter_5/vehicle-success.html')), # Forward Slash Only
    re_path(r'^chapter-5/vehicle-form-success/?$', TemplateView.as_view(template_name='chapter_5/vehicle-success.html'), kwargs={
        'title': 'ModelFormClass_View Success Page',
        'page_id': 'model-form-class-success',
        'page_class': 'model-form-class-success-page',
        'h1_tag': 'This is the ModelFormClass_View Success Page Using VehicleForm',
    }), # Accepts Both Forward Slash and Non-Forward Slash
]
