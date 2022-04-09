import logging
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import View


from ..chapter_3.models import Vehicle


def practice_view(request, year):
    return TemplateResponse(request, 'chapter_4/my_practice_page.html', {'year': year})


def practice_year_view(request, year):
    # What Year Did The User Visit?
    #print(type(year))
    #print(year)

    # Relative URL Lookup
    #print(reverse('year_url', args=(2023,)))
    #print(reverse('year_url', args=(2024,)))
    #print(reverse('year_url', args=(2025,)))
    #print(reverse('year_url', args=(2026,)))
    #print(reverse('year_url', args=(2027,)))

    # Absolute URL Lookup (http://www.yourdomain.com and https://www.yourdomain.com)
    #print(request.build_absolute_uri(reverse('year_url', args=(2023,))))
    #print(request.build_absolute_uri(reverse('year_url', args=(2024,))))
    #print(request.build_absolute_uri(reverse('year_url', args=(2025,))))
    #print(request.build_absolute_uri(reverse('year_url', args=(2026,))))
    #print(request.build_absolute_uri(reverse('year_url', args=(2027,))))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logger.info('The Requested Year Is: %s' % year)

    if year >= 1900:
        return TemplateResponse(request, 'chapter_4/my_year.html', {'year': year})
    else:
        raise Http404('Year Not Found: %s' % year)


def vehicle_view(request, id):
#def vehicle_view(request, vin):
    # Search By ID
    try:
        vehicle = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        raise Http404('Vehicle ID Not Found: %s' % id)
    #else:
    #    print(vehicle.get_url())
    #    print(vehicle.get_absolute_url(request))

    # Search By VIN
    #try:
    #    vehicle = Vehicle.objects.get(vin=vin)
    #except Vehicle.DoesNotExist:
    #    raise Http404('Vehicle VIN Not Found: %s' % vin)
    #else:
    #    print(vehicle.get_url())
    #    print(vehicle.get_absolute_url(request))

    return TemplateResponse(request, 'chapter_4/my_vehicle.html', {'vehicle': vehicle})


class VehicleView(View):
    template_name = 'chapter_4/my_vehicle_class_1.html'

    def get(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            raise Http404('Vehicle ID Not Found: %s' % id)
        #else:
        #    print(vehicle.get_url())
        #    print(vehicle.get_absolute_url(request))

        return TemplateResponse(request, self.template_name, {'vehicle': vehicle})

    def post(self, request, *args, **kwargs):
        #return redirect('/success/')
        return HttpResponseRedirect('/success/')


class VehicleView2(VehicleView):
    template_name = 'chapter_4/my_vehicle_class_2.html'

    # Override As Necessary
    #def get(self, request, id, *args, **kwargs):
    #    try:
    #        vehicle = Vehicle.objects.get(id=id)
    #    except Vehicle.DoesNotExist:
    #        raise Http404('Vehicle ID Not Found: %s' % id)
    #    else:
    #        print(vehicle.get_url())
    #        print(vehicle.get_absolute_url(request))

    #    return TemplateResponse(request, self.template_name, {'vehicle': vehicle})

     # Override As Necessary
    #def post(self, request, *args, **kwargs):
    #    return redirect('/success/')
    #    return HttpResponseRedirect('/success/')


class TestPageView(View):
    template_name = 'chapter_4/pages/test_page_1.html'

    def get(self, request, *args, **kwargs):
        print(request.build_absolute_uri())
        return TemplateResponse(request, self.template_name, {
            'title': 'My Test Page 1',
            'page_id': 'test-id-1',
            'page_class': 'test-page-1',
            'h1_tag': 'This is Test Page 1'
        })

    def post(self, request, *args, **kwargs):
        #return redirect('/success/')
        return HttpResponseRedirect('/success/')
