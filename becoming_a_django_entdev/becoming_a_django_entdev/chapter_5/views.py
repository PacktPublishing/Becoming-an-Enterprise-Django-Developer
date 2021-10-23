from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms import formset_factory, inlineformset_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


from .forms import ContactForm, VehicleForm, ProspectiveBuyerForm, ProspectiveBuyerFormSet
from ..chapter_3.models import Vehicle, Engine, Vehicle_Model


class FormClass_View(FormView):
    template_name = 'chapter_5/form-class.html'
    form_class = ContactForm
    success_url = '/chapter-5/contact-form-success/'

    #def get_success_url(self, **kwargs):
    #    return reverse('pattern_name', args=(value,))

    def get(self, request, *args, **kwargs):
        '''
        GET Response Method
        '''
        initial = {
            'full_name': 'FirstName LastName',
            'email_1': 'example1@example.com',
            'email_2': 'example2@example.com',
            'email_3': 'example3@example.com',
            'conditional_required': 'My Required Value',
            'multiple_emails': 'example4@example.com,example5@example.com,example6@example.com',
            'message': 'My Message',
        }

        return TemplateResponse(request, self.template_name, {
            'title': 'FormClass_View Page',
            'page_id': 'form-class-id',
            'page_class': 'form-class-page',
            'h1_tag': 'This is the FormClass_View Page Using ContactForm',
            'form': self.form_class(initial),
        })

    def post(self, request, *args, **kwargs):
        '''
        POST Response Method
        '''
        #return redirect(self.success_url)
        form = self.form_class(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'FormClass_View Page - Please Correct The Errors Below',
                'page_id': 'form-class-id',
                'page_class': 'form-class-page errors-found',
                'h1_tag': 'This is the FormClass_View Page Using ContactForm<br /><small class="error-msg">Errors Found</small>',
                'form': form,
            })

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        '''

        # Perform Additional Actions, such as sending an email or custom business logic validation checking.
        #form.send_email()
        return super().form_valid(form)


class ModelFormClass_CreateView(CreateView):
    template_name = 'chapter_5/model-form-class.html'
    form_class = VehicleForm
    success_url = '/chapter-5/vehicle-form-success/'

    def get(self, request, *args, **kwargs):
        '''
        GET Response Method
        '''

        # For use with Inline Formset Exercise
        buyer_formset = ProspectiveBuyerFormSet()

        # Determine Number of Inlines by querystring localhost:8000/chapter-5/model-form-class?forms=3
        #if 'forms' in request.GET:
        #    num = int(request.GET.get('forms', '1'))

        #    buyer_formset = formset_factory(
        #        ProspectiveBuyerForm,
        #        extra = num
        #    )
        #else:
        #    buyer_formset = ProspectiveBuyerFormSet()

        return TemplateResponse(request, self.template_name, {
            'title': 'ModelFormClass_CreateView Page',
            'page_id': 'model-form-class-id',
            'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClass_CreateView Class Page Using VehicleForm',
            'form': self.form_class(),
            'buyer_formset': buyer_formset,
        })

    def post(self, request, *args, **kwargs):
        '''
        POST Response Method
        '''
        #return redirect(self.success_url)
        form = self.form_class(request.POST)

        # For use with Inline Formset Exercise
        buyer_formset = ProspectiveBuyerFormSet(request.POST)

        if form.is_valid():
            vehicle = form.instance
            vehicle.save()

            # If you need to manipulate fields individually
            #vehicle = Vehicle(
            #    vin = form.instance.vin,
            #    sold = form.instance.sold,
            #    price = form.instance.price,
            #    make = form.instance.make,
            #    model = form.instance.model,
            #    engine = form.instance.engine,
            #)
            #vehicle.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClass_CreateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClass_CreateView Page Using VehicleForm<br /><small class="error-msg">Errors Found</small>',
                'form': form,
                'buyer_formset': buyer_formset,
            })

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        '''

        # Perform Additional Actions, such as sending an email or custom business logic validation checking.
        #form.send_email()
        return super().form_valid(form)


class ModelFormClass_UpdateView(UpdateView):
    template_name = 'chapter_5/model-form-class.html'
    form_class = VehicleForm
    success_url = '/chapter-5/vehicle-form-success/'

    def get(self, request, id, *args, **kwargs):
        '''
        GET Response Method
        '''
        try:
            vehicle = Vehicle.objects.get(pk=id)
        except ObjectDoesNotExist:
            form = self.form_class()
        else:
            form = self.form_class(instance=vehicle)

        # For use with Inline Formset Exercise
        #buyer_formset = ProspectiveBuyerFormSet()

        return TemplateResponse(request, self.template_name, {
            'title': 'ModelFormClass_UpdateView Page',
            'page_id': 'model-form-class-id',
            'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClass_UpdateView Class Page Using VehicleForm',
            'form': form,
            #'buyer_formset': buyer_formset,
        })

    def post(self, request, id, *args, **kwargs):
        '''
        POST Response Method
        '''
        #return redirect(self.success_url)
        form = self.form_class(request.POST)

        # For use with Inline Formset Exercise
        #buyer_formset = ProspectiveBuyerFormSet(request.POST)

        if form.is_valid():
            vehicle = form.instance
            vehicle.save()

            # If you need to manipulate fields individually
            #vehicle = Vehicle(
            #    vin = form.instance.vin,
            #    sold = form.instance.sold,
            #    price = form.instance.price,
            #    make = form.instance.make,
            #    model = form.instance.model,
            #    engine = form.instance.engine,
            #)
            #vehicle.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClass_UpdateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClass_UpdateView Page Using VehicleForm<br /><small class="error-msg">Errors Found</small>',
                'form': form,
                #'buyer_formset': buyer_formset,
            })

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        '''

        # Perform Additional Actions, such as sending an email or custom business logic validation checking.
        #form.send_email()
        return super().form_valid(form)
