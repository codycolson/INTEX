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
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}

    events = chfmod.Event.objects.all()
    params['events'] = events

    print(events)

    return templater.render_to_response(request, '/events.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        event = chfmod.Event.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/events')

    form = EventEditForm(initial={
        'name': event.name,
        'end_date': event.end_date,
        'start_date': event.start_date,
        'description': event.description,
        'map_file_name': event.map_file_name,
    })
    if request.method == 'POST':
        form = EventEditForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.description = form.cleaned_data['description']
            event.map_file_name = form.cleaned_data['map_file_name']
            event.save()
            return HttpResponseRedirect('/events')


    params['form'] = form
    return templater.render_to_response(request, '/events.edit.html', params)

class EventEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    start_date = forms.DateField(required=False, widget=SelectDateWidget())
    end_date = forms.DateField(required=False, widget=SelectDateWidget())
    description = forms.CharField(required=False, max_length=400)
    map_file_name = forms.CharField(required=False, max_length=100)



@view_function
@permission_required('chf.add_event', login_url='/mylogin')
def create(request):
    '''Create new user'''
    event = chfmod.Event()
    event.name = ""
    event.description = ""
    event.map_file_name = ""
    event.save()

    return HttpResponseRedirect('/events.edit/{}'.format(event.id))


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        event = chfmod.Event.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/events')

    event.delete()
    return HttpResponseRedirect('/events')

@view_function
def details(request):

    params = {}

    try:
        event = chfmod.Event.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/events')

    params['event'] = event
    params['areas'] = chfmod.Area.objects.filter(event_id=event.id)
    params['products'] = chfmod.ExpectedSaleItem.objects.filter(event_id=event.id)

    return templater.render_to_response(request, '/events.details.html', params)
