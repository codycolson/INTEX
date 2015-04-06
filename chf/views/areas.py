__author__ = 'Cody'

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import chf.models as chfmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django import forms


templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}

    areas = chfmod.Area.objects.all()
    params['areas'] = areas

    print(areas)

    return templater.render_to_response(request, '/areas.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        area = chfmod.Area.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/areas')

    form = AreaEditForm(initial={
        'name': area.name,
        'description': area.description,
    })
    if request.method == 'POST':
        form = AreaEditForm(request.POST)
        if form.is_valid():
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.save()
            return HttpResponseRedirect('/areas')


    params['form'] = form
    return templater.render_to_response(request, '/areas.edit.html', params)

class AreaEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=False, max_length=400)


@view_function
def create(request):
    '''Create new user'''
    area = chfmod.Area()
    area.name = ""
    area.description = ""
    area.save()

    return HttpResponseRedirect('/areas.edit/{}'.format(area.id))


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        area = chfmod.Area.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/areas')

    area.delete()
    return HttpResponseRedirect('/areas')