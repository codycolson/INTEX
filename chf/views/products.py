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
from datetime import *


templater = get_renderer('chf')

@view_function
def process_request(request):

    params = {}

    categories = chfmod.Category.objects.all()
    params['categories'] = categories

    if (request.urlparams[0] == 'search'):
        products = chfmod.RentalProduct.objects.filter(name__icontains=request.urlparams[1])
        params['products'] = products
        params['search'] = request.urlparams[1]
        return templater.render_to_response(request, '/products.html', params)

    if request.urlparams[0]:
        products = chfmod.RentalProduct.objects.filter(category=request.urlparams[0])
        category = chfmod.Category.objects.get(id=request.urlparams[0])
        subcategories = chfmod.SubCategory.objects.filter(category=request.urlparams[0])
        params['products'] = products
        params['cat'] = category
        params['subcategories'] = subcategories

        if request.urlparams[1]:
            products = chfmod.RentalProduct.objects.filter(subcategory=request.urlparams[1])
            subcategory = chfmod.SubCategory.objects.get(id=request.urlparams[1])
            params['products'] = products
            params['sub'] = subcategory
            print(params)
            params['not_found'] = "We're sorry, the category you searched was not found. Please try another."
            return templater.render_to_response(request, '/products.html', params)
        return templater.render_to_response(request, '/products.html', params)

    products = chfmod.RentalProduct.objects.all()
    params['products'] = products

    categories = chfmod.Category.objects.all()
    params['categories'] = categories

    return templater.render_to_response(request, '/products.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        product = chfmod.RentalProduct.objects.get(id=request.urlparams[0])
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

    categories = chfmod.Category.objects.all()
    params['categories'] = categories

    if (request.urlparams[0] == 'search'):
        products = chfmod.RentalItem.objects.filter(name__icontains=request.urlparams[1]).filter(date_in=None)
        params['products'] = products
        params['search'] = request.urlparams[1]
        return templater.render_to_response(request, '/rentalreturn.html', params)

    if request.urlparams[0]:
        products = chfmod.RentalItem.objects.filter(category=request.urlparams[0]).filter(date_in=None)
        category = chfmod.Category.objects.get(id=request.urlparams[0])
        subcategories = chfmod.SubCategory.objects.filter(category=request.urlparams[0])
        params['products'] = products
        params['cat'] = category
        params['subcategories'] = subcategories

        if request.urlparams[1]:
            products = chfmod.RentalItem.objects.filter(subcategory=request.urlparams[1]).filter(date_in=None)
            subcategory = chfmod.SubCategory.objects.get(id=request.urlparams[1])
            params['products'] = products
            params['sub'] = subcategory
            print(params)
            params['not_found'] = "We're sorry, the category you searched was not found. Please try another."
            return templater.render_to_response(request, '/rentalreturn.html', params)
        return templater.render_to_response(request, '/rentalreturn.html', params)

    products = chfmod.RentalItem.objects.all().filter(date_in=None)
    params['products'] = products

    categories = chfmod.Category.objects.all()
    params['categories'] = categories

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

@view_function
def processreturn(request):

    item = chfmod.RentalItem.objects.filter(date_in=None).get(id=request.urlparams[0])

    w = datetime.now()

    item.date_in = w
    item.save()
    print(item.date_in)
    return HttpResponseRedirect('/products.returnrental')

