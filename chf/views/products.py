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

    products = chfmod.RentalProduct.objects.all()
    params['products'] = products

    return templater.render_to_response(request, '/products.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        product = chfmod.Product.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/products')

    form = ProductEditForm(initial={

        'name': product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,
    })
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']
            product.save()
            return HttpResponseRedirect('/products')


    params['form'] = form
    return templater.render_to_response(request, '/products.edit.html', params)

class ProductEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, max_length=400)
    category = forms.CharField(required=True, max_length=100)
    current_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)

@view_function
def create(request):
    '''Create new user'''
    product = chfmod.Product()
    product.name = ""
    product.description = ""
    product.category = ""
    product.save()

    return HttpResponseRedirect('/products.edit/{}'.format(product.id))


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        product = chfmod.Product.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/products')

    product.delete()
    return HttpResponseRedirect('/products')


###########################################################################

@view_function
def view(request):

    params = {}

    try:
        item = chfmod.RentalProduct.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/products')

    params['item'] = item

    return templater.render_to_response(request, '/products.view.html', params)

@view_function
def returnrental(request):

    params = {}

    products = chfmod.RentalItem.objects.filter(date_in=None)
    params['products'] = products

    return templater.render_to_response(request, '/products.rentalreturn.html', params)

@view_function
def viewreturn(request):

    params = {}

    try:
        item = chfmod.RentalItem.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/products')

    params['item'] = item

    return templater.render_to_response(request, '/products.viewreturn.html', params)
