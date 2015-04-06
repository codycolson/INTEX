__author__ = 'Cody'

from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from django.http import HttpResponse
from .. import dmp_render, dmp_render_to_response
import chf.models as chfmod

@view_function
def process_request(request):
  template_vars = {}
  return dmp_render_to_response(request, 'index.html', template_vars)

@view_function
def check_username(request):

    username = request.REQUEST.get('username')

    user = chfmod
    return HttpResponse("1")
