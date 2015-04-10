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

    categories = chfmod.Category.objects.all()
    params['categories'] = categories

    if (request.urlparams[0] == 'search'):
        items = chfmod.ProductSpecification.objects.filter(name__icontains=request.urlparams[1])
        params['items'] = items
        params['search'] = request.urlparams[1]
        return templater.render_to_response(request, '/items.html', params)

    if request.urlparams[0]:
        items = chfmod.ProductSpecification.objects.filter(category=request.urlparams[0])
        category = chfmod.Category.objects.get(id=request.urlparams[0])
        subcategories = chfmod.SubCategory.objects.filter(category=request.urlparams[0])
        params['items'] = items
        params['cat'] = category
        params['subcategories'] = subcategories

        if request.urlparams[1]:
            items = chfmod.ProductSpecification.objects.filter(subcategory=request.urlparams[1])
            subcategory = chfmod.SubCategory.objects.get(id=request.urlparams[1])
            params['items'] = items
            params['sub'] = subcategory
            print(params)
            params['not_found'] = "We're sorry, the category you searched was not found. Please try another."
            return templater.render_to_response(request, '/items.html', params)
        return templater.render_to_response(request, '/items.html', params)

    items = chfmod.ProductSpecification.objects.all()
    params['items'] = items

    categories = chfmod.Category.objects.all()
    params['categories'] = categories


    return templater.render_to_response(request, '/items.html', params)


###############################################################

@view_function
def edit(request):

    params = {}

    try:
        item = chfmod.ProductSpecification.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/items')

    form = ItemEditForm(initial={

        'name': item.name,
        'description': item.description,
        'price': item.price,
        'manufacturer': item.manufacturer,
        'average_cost': item.average_cost,
        'sku': item.sku,
        'order_form_name': item.order_form_name,
        'production_time': item.production_time,
        'category': item.category.id,
        'subcategory': item.subcategory.id ,
        'photo': item.photo,
        'quantity_on_hand': item.quantity_on_hand,
        'shelf_location': item.shelf_location,
        'product_order_file': item.product_order_file,
    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.manufacturer = form.cleaned_data['manufacturer']
            item.price = form.cleaned_data['price']
            item.average_cost = form.cleaned_data['average_cost']
            item.sku = form.cleaned_data['sku']
            item.order_form_name = form.cleaned_data['order_form_name']
            item.production_time = form.cleaned_data['production_time']
            item.subcategory = chfmod.SubCategory.objects.get(id=form.cleaned_data['subcategory'])
            item.category = chfmod.Category.objects.get(id=form.cleaned_data['category'])
            item.photo = chfmod.Photograph.objects.get(image=form.cleaned_data['photo'])
            item.quantity_on_hand = form.cleaned_data['quantity_on_hand']
            item.shelf_location = form.cleaned_data['shelf_location']
            item.product_order_file = form.cleaned_data['product_order_file']

            item.save()
            return HttpResponseRedirect('/manage')


    params['form'] = form
    return templater.render_to_response(request, '/items.edit.html', params)

class ItemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, max_length=400)
    manufacturer = forms.CharField(required=False,max_length=80)
    price = forms.DecimalField(required=True)
    average_cost = forms.DecimalField(required=False,max_digits=10, decimal_places=2)
    sku = forms.CharField(required=False,max_length=20)
    order_form_name = forms.CharField(required=False,max_length=200)
    production_time = forms.CharField(required=False,max_length=200)
    category = forms.ChoiceField(choices=[(x.id,x.name) for x in chfmod.Category.objects.all()])
    subcategory = forms.ChoiceField(choices=[(x.id,x.name) for x in chfmod.SubCategory.objects.all()])
    photo = forms.CharField(required=False)
    quantity_on_hand = forms.IntegerField(required=False)
    shelf_location = forms.CharField(required=False,max_length=40)
    product_order_file = forms.CharField(required=False)


@view_function
def create(request):
    '''Create new user'''
    item = chfmod.ProductSpecification()
    item.name = ''
    item.description = ''
    item.shelf_location = ''
    item.category = chfmod.Category.objects.get(id=1)
    item.subcategory = chfmod.SubCategory.objects.get(id=1)
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