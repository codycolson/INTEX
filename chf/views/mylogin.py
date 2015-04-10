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
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import re
from datetime import datetime
import json

templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}

    return templater.render_to_response(request, 'mylogin.html', params)

@view_function
def cartlogin(request):

    params = {}

    return templater.render_to_response(request, 'mylogincart.html', params)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        # try employee login
        if user == None:
            uid_clean = self.cleaned_data['username']
            pw = self.cleaned_data['password']
            uid = re.sub("$","@colonialheritagefoundation.local",uid_clean)

            from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO, SUBTREE, ObjectDef, AttrDef, Reader, Entry, Attribute, OperationalAttribute

            try:
                s = Server('colonialheritagefoundation.com', port=4567, get_info=GET_ALL_INFO)
                c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC,
                           user=uid, password=pw, authentication=AUTH_SIMPLE)
                search = c.search(
                                  search_base = 'CN=Users,DC=colonialheritagefoundation,DC=local',
                                  search_filter = '(samAccountName='+uid_clean+')',
                                  attributes = [
                                    'givenName',
                                    'sn',
                                    'mail',]
                                  )
                user_info = json.loads(c.response_to_json(search))['entries'][0]['attributes']
                uid = re.sub("@colonialheritagefoundation.local","@CHF",uid)
                u, created = chfmod.User.objects.get_or_create(username=uid)
                #update employee credentials
                u.set_password(pw)
                u.first_name = user_info['givenName']
                u.last_name = user_info['sn']
                u.is_staff = True
                if created == True:
                    u.date_appointed_agent = datetime.now()
                u.save()
                user = authenticate(username=self.cleaned_data['username'] + "@CHF", password=self.cleaned_data['password'])
            except:
                pass
        if user == None:
            raise forms.ValidationError('Not valid')
        return self.cleaned_data

######################################################

@view_function
def loginform(request):

    params = {}
    params['url'] = request.urlparams[0]
    print('>>>>>>>>>>>>>>>>',params['url'])
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=uid,password=pw)

            if user == None:
                uid = re.sub("$","@CHF",uid)
                user = authenticate(username=uid,password=pw)
                print(uid + ">>>>" + pw)
                login(request, user)

            else:
                login(request, user)

            return HttpResponse('''
                <script>
                window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form
    return templater.render_to_response(request, 'mylogin.loginform.html', params)

@view_function
def loginformcart(request):

    params = {}
    params['url'] = request.urlparams[0]
    print('>>>>>>>>>>>>>>>>',params['url'])
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=uid,password=pw)

            if user == None:
                uid = re.sub("$","@CHF",uid)
                user = authenticate(username=uid,password=pw)
                print(uid + ">>>>" + pw)
                login(request, user)

            else:
                login(request, user)

            return HttpResponseRedirect('account.checkout')

    params['form'] = form
    return templater.render_to_response(request, 'mylogin.loginformcart.html', params)

