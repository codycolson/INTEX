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
import datetime


templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}
    i = datetime.datetime.now()
    #i.strftime()
    batch = chfmod.RentalItem.objects.all()
    params['batch'] = batch
    print(batch)
    return templater.render_to_response(request, '/batch.html', params)

