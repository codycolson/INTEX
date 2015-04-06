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
from django.contrib.auth.decorators import login_required


templater = get_renderer('chf')


@view_function
@login_required
def process_request(request):

    params = {}

    addresses = chfmod.Address.objects.all()
    params['addresses'] = addresses


    return templater.render_to_response(request, '/address.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        address = chfmod.Address.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/address')

    form = AddressEditForm(initial={
        'address1': address.address1,
        'address2': address.address2,
        'city': address.city,
        'state': address.state,
        'zip': address.zip,
    })
    if request.method == 'POST':
        form = AddressEditForm(request.POST)
        if form.is_valid():
            address.address1 = form.cleaned_data['address1']
            address.address2 = form.cleaned_data['address2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.zip = form.cleaned_data['zip']
            address.save()
            return HttpResponseRedirect('/address')


    params['form'] = form
    return templater.render_to_response(request, '/address.edit.html', params)

class AddressEditForm(forms.Form):
    address1 = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=True, max_length=30)
    state = forms.CharField(required=True, max_length=2)
    zip = forms.IntegerField(required=True)

    def clean_zip(self):
        zip = self.cleaned_data['zip']
        if len(str(zip)) > 5:
            raise forms.ValidationError("Please enter a valid zip code")
        return self.cleaned_data['zip']

############################################################################

@view_function
def create(request):
    '''Create new user'''
    address = chfmod.Address()
    address.address1 = ""
    address.address2 = ""
    address.city = ""
    address.state = ""
    address.zip = ""
    address.save()

    return HttpResponseRedirect('/address.edit/{}'.format(address.id))


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        address = chfmod.Address.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/address')

    address.delete()
    return HttpResponseRedirect('/address')


