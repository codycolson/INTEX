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


templater = get_renderer('chf')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user == None:
            raise forms.ValidationError('Not valid')
        return self.cleaned_data

@view_function
def loginform(request):

    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            print(next)
            return HttpResponse('''
                <script>
                window.location.href = window.location.href;
                </script>
            ''')
    params['form'] = form
    return templater.render_to_response(request, 'mylogin.loginform.html', params)
