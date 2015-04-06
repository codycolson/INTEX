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
from django.contrib.auth.decorators import permission_required


templater = get_renderer('chf')

@view_function
#@permission_required('chf.add_item', login_url='/mylogin')
def process_request(request):

    params = {}

    if (request.urlparams[0]):
        items = chfmod.ProductSpecification.objects.filter(name__icontains=request.urlparams[0])
        params['items'] = items
        return templater.render_to_response(request, '/items.html', params)


    items = chfmod.ProductSpecification.objects.all()
    params['items'] = items

    print(items)

    return templater.render_to_response(request, '/items.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        item = chfmod.Item.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/items')

    form = ItemEditForm(initial={

        'name': item.name,
        'description': item.description,
        'value': item.value,
        'standard_rental_price': item.standard_rental_price,
        'is_rentable': item.is_rentable,
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.standard_rental_price_price = form.cleaned_data['standard_rental_price']
            item.is_rentable = form.cleaned_data['is_rentable']
            item.save()
            return HttpResponseRedirect('/items')


    params['form'] = form
    return templater.render_to_response(request, '/items.edit.html', params)

class ItemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, max_length=400)
    value = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
    standard_rental_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
    is_rentable = forms.BooleanField(required=False)

    def clean_username(self):
        user_count = chfmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >=1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']

@view_function
def create(request):
    '''Create new user'''
    item = chfmod.Item()
    item.name = ""
    item.description = ""
    item.is_rentable = False
    item.save()

    return HttpResponseRedirect('/items.edit/{}'.format(item.id))


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        item = chfmod.Item.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/items')

    item.delete()
    return HttpResponseRedirect('/items')

###########################################################################

@view_function
def view(request):

    params = {}

    try:
        item = chfmod.ProductSpecification.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/items')

    params['item'] = item

    return templater.render_to_response(request, '/items.view.html', params)