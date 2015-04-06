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
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings


templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}
    i = datetime.now() - timedelta(days=30)
    ii = datetime.now() - timedelta(days=60)
    iii = datetime.now() - timedelta(days=90)
    batch1 = chfmod.RentalItem.objects.filter(date_due__lte=i).filter(date_in=None)
    batch2 = chfmod.RentalItem.objects.filter(date_due__lte=ii).filter(date_in=None)
    batch3 = chfmod.RentalItem.objects.filter(date_due__lte=iii).filter(date_in=None)
    params['batch1'] = batch1
    params['batch2'] = batch2
    params['batch3'] = batch3
    print(i,ii,iii)
    return templater.render_to_response(request, '/report.html', params)

@view_function
def send(request):

    params = {}

    i = datetime.now()
    overdue = chfmod.RentalItem.objects.filter(date_due__lte=i).filter(date_in=None)
    for o in overdue:

        params['items'] = o
        emailbody = templater.render(request, 'overdue_items.html',params)

        email = o.transaction.customer.email
        send_mail('Notice of Overdue Items', emailbody, settings.EMAIL_HOST_USER, [email],html_message=emailbody, fail_silently=False)

    return HttpResponseRedirect('/')
