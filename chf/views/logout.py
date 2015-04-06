__author__ = 'Cody'

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
import chf.models as chfmod
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


@view_function
def process_request(request):
    try:
        logout(request)
    except:
        return HttpResponse("You're already logged out")
    return HttpResponseRedirect('/')