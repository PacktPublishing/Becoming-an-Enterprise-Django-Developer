from django.conf import settings
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib import messages
from django.forms import formset_factory, inlineformset_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


from .forms import ContactForm, VehicleForm, ProspectiveBuyerForm, ProspectiveBuyerFormSet
from ..chapter_3.models import Seller, Vehicle, Engine, Vehicle_Model


class FormClassView(FormView):
    template_name = 'chapter_7/form-class.html'
    form_class = ContactForm
    success_url = '/chapter-7/contact-form-success/'

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
            'title': 'FormClassView Page',
            'page_id': 'form-class-id',
            'page_class': 'form-class-page',
            'h1_tag': 'This is the FormClassView Page Using ContactForm',
            'form': self.form_class(initial),
        })

    def post(self, request, *args, **kwargs):
        '''
        POST Response Method
        '''
        #return redirect(self.success_url)
        form = self.form_class(request.POST)

        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your contact form submitted successfully', extra_tags='bold', fail_silently=True)
            #messages.success(request, 'Your contact form submitted successfully', extra_tags='bold', fail_silently=True)
            #messages.add_message(request, settings.CRITICAL, 'This is critical!')

            #return HttpResponseRedirect(self.success_url)

            context = {
                'title': 'FormClassView Page',
                'page_id': 'form-class-id',
                'page_class': 'form-class-page',
                'h1_tag': 'This is the FormClassView Page Using ContactForm',
                'form': form,
            }
        else:
            messages.add_message(request, messages.ERROR, 'There was a problem submitting your contact form.<br />Please review the highlighted fields below.', fail_silently=True)
            #messages.error(request, 'There was a problem submitting your contact form.<br />Please review the highlighted fields below.', fail_silently=True)

            context = {
                'title': 'FormClassView Page - Please Correct The Errors Below',
                'page_id': 'form-class-id',
                'page_class': 'form-class-page errors-found',
                'h1_tag': 'This is the FormClassView Page Using ContactForm<br /><small class="error-msg">Errors Found</small>',
                'form': form,
            }

        #form.send_email(request)
        #form.generate_pdf(request)

        return TemplateResponse(request, self.template_name, context)

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        '''

        # Perform Additional Actions, such as sending an email or custom business logic validation checking.
        #form.send_email()
        return super().form_valid(form)


class ModelFormClassCreateView(CreateView):
    template_name = 'chapter_7/model-form-class.html'
    form_class = VehicleForm
    success_url = '/chapter-7/vehicle-form-success/'

    def get(self, request, *args, **kwargs):
        '''
        GET Response Method
        '''

        # For use with Inline Formset Exercise
        buyer_formset = ProspectiveBuyerFormSet()

        # Determine Number of Inlines by querystring localhost:8000/chapter-7/model-form-class?forms=3
        #if 'forms' in request.GET:
        #    num = int(request.GET.get('forms', '1'))

        #    buyer_formset = formset_factory(
        #        ProspectiveBuyerForm,
        #        extra = num
        #    )
        #else:
        #    buyer_formset = ProspectiveBuyerFormSet()

        return TemplateResponse(request, self.template_name, {
            'title': 'ModelFormClassCreateView Page',
            'page_id': 'model-form-class-id',
            'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassCreateView Class Page Using VehicleForm',
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
            #    vehicle_model = form.instance.model,
            #    engine = form.instance.engine,
            #)
            #vehicle.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClassCreateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClassCreateView Page Using VehicleForm<br /><small class="error-msg">Errors Found</small>',
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


class ModelFormClassUpdateView(UpdateView):
    template_name = 'chapter_7/model-form-class.html'
    form_class = VehicleForm
    success_url = '/chapter-7/vehicle-form-success/'

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
            'title': 'ModelFormClassUpdateView Page',
            'page_id': 'model-form-class-id',
            'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassUpdateView Class Page Using VehicleForm',
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
            #    vehicle_model = form.instance.model,
            #    engine = form.instance.engine,
            #)
            #vehicle.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClassUpdateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClassUpdateView Page Using VehicleForm<br /><small class="error-msg">Errors Found</small>',
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
