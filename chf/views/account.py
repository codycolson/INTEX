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
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta

templater = get_renderer('chf')

@view_function
@login_required
def edit2(request):

    params = {}


    return templater.render_to_response(request, '/account.edit.html', params)

###############################################################

@view_function
@login_required
def process_request(request):

    params = {}


    return templater.render_to_response(request, '/account.html', params)

###############################################################

@view_function
@login_required
def edit(request):

    params = {}

    user = request.user

    form = AccountEditForm(initial={

        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'organization_name': user.organization_name,
        'organization_type': user.organization_type,
        'emergency_contact': user.emergency_contact,
        'emergency_phone': user.emergency_phone,
        'emergency_relationship': user.emergency_relationship,
        #'photo': user.photo,
        # 'street1': user.address.street1,
        # 'street2': user.address.street2,
        # 'city': user.address.city,
        # 'state': user.address.state,
        # 'zip_code': user.address.zip_code,
        #'username': user.username,
        #'security_question': user.security_question,
        #'security_answer': user.security_answer,
    })

    if request.method == 'POST':
        form = AccountEditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            #user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            user.organization_name = form.cleaned_data['organization_name']
            user.organization_type = form.cleaned_data['organization_type']
            user.emergency_contact = form.cleaned_data['emergency_contact']
            user.emergency_phone = form.cleaned_data['emergency_phone']
            user.emergency_relationship = form.cleaned_data['emergency_relationship']
            #user.photo = form.cleaned_data['photo']
            # user.street1 = form.cleaned_data['street1']
            # user.street2 = form.cleaned_data['street2']
            # user.city = form.cleaned_data['city']
            # user.state = form.cleaned_data['state']
            # user.zip_code = form.cleaned_data['zip_code']
            #user.security_question = form.cleaned_data['security_question']
            # user.security_answer = form.cleaned_data['security_answer']
            print(">>>>>>>>>>>>>>>>> Got here")
            user.save()
            return HttpResponse('''
                <script>
                window.location.href = window.location.href;
                </script>
            ''')


    params['form'] = form
    return templater.render_to_response(request, '/account.edit.html', params)

class AccountEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    #username = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)
    phone = forms.CharField(required=True, max_length=20)
    organization_name = forms.CharField(required=False, max_length=100)
    organization_type = forms.CharField(required=False, max_length=100)
    emergency_contact = forms.CharField(required=False, max_length=100)
    emergency_phone = forms.CharField(required=False, max_length=20)
    emergency_relationship = forms.CharField(required=False, max_length=100)
    #photo = forms.CharField(required=False, max_length=100)
    # street1 = forms.CharField(required=True, max_length=100)
    # street2 = forms.CharField(required=False, max_length=100)
    # city = forms.CharField(required=True, max_length=100)
    # state = forms.CharField(required=True, max_length=2)
    # zip_code = forms.CharField(required=True, max_length=5)
    # security_question = forms.CharField(required=False, max_length=100)
    # security_answer = forms.CharField(required=False, max_length=100)

class AccountCreateForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    username = forms.CharField(required=True, max_length=100)
    password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(required=True, max_length=100)
    phone = forms.CharField(required=True, max_length=20)
    organization_name = forms.CharField(required=False, max_length=100)
    organization_type = forms.CharField(required=False, max_length=100)
    #photo = forms.CharField(required=False, max_length=100)
    # street1 = forms.CharField(required=True, max_length=100)
    # street2 = forms.CharField(required=False, max_length=100)
    # city = forms.CharField(required=True, max_length=100)
    # state = forms.CharField(required=True, max_length=2)
    # zip_code = forms.CharField(required=True, max_length=5)
    security_question = forms.CharField(required=False, max_length=100)
    security_answer = forms.CharField(required=False, max_length=100)

    def clean_username(self):
        user_count = chfmod.User.objects.filter(username=self.cleaned_data['username']).count()
        if user_count >=1:
            raise forms.ValidationError("This username is already taken.")
        username=self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError("Username needs to have at least 4 characters.")

        return self.cleaned_data['username']


class PasswordResetForm(forms.Form):

    email = forms.EmailField(required=True, max_length=100)


###########################################################################

@view_function
def delete(request):

    params = {}

    try:
        user = request.user
    except:
        return HttpResponseRedirect('/mylogin.html')

    user.delete()
    return HttpResponseRedirect('/')

###########################################################################

@view_function
def create(request):
    '''Create new user'''

    params = {}

    form = AccountCreateForm()
    if request.method =='POST':
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            user = chfmod.User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            user.organization_name = form.cleaned_data['organization_name']
            user.organization_type = form.cleaned_data['organization_type']
            user.security_answer = form.cleaned_data['security_answer']
            user.security_question = form.cleaned_data['security_question']
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)

            return HttpResponseRedirect('/')
    params['form'] = form


    return templater.render_to_response(request,'/account.create.html', params)

#############################################################

@view_function
def passwordreset(request):

    params = {}

    form = PasswordResetForm()
    if request.method =='POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = chfmod.User.objects.get(email=email)
            password = chfmod.User.objects.make_random_password(length=12)
            user.set_password(password)
            user.save()
            email_body = templater.render(request, 'passwordreset.html', params)
            #send_mail('test', 'just work', 'cody@colonialheritagefoundation.com', ['cody.colson@mozenda.com'], html_message=None, fail_silently=False)
            #send_mail(emailsubject, emailbody, from_email, to_email, html_message=emailbody, fail_silently=False)
            #send_mail('Password Reset', email_body, 'codymcolson@gmail.com', ['cody.colson@mozenda.com'], html_message= email_body,fail_silently=False)
            send_mail('Password Reset', 'Here is your new password ' + password + '. Please contact support@colonialheritagefoundation.com if you did not initiate this request.', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            params['password'] = password
            return templater.render_to_response(request,'/account.newpassword.html', params)
    params['form'] = form


    return templater.render_to_response(request,'/account.passwordreset.html', params)

@view_function
def newpassword(request):

    params = {}

    templater.render_to_response(request,'/account.newpassword.html', params)

#################################################################

@view_function
def rentalcart(request):

    params = {}

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = {}

    request.session['rental_cart'][request.urlparams[0]] = int(request.urlparams[1])

    # Save session variable changes
    request.session.modified = True

    keys = request.session['rental_cart'].keys()
    rental = chfmod.RentalProduct.objects.filter(id__in=keys)

    keys = request.session['shopping_cart'].keys()
    item = chfmod.RentalProduct.objects.filter(id__in=keys)

    params['items'] = item
    params['rentals'] = rental
    return templater.render_to_response(request, '/account.rentalcart.html', params)

@view_function
def shoppingcart(request):

    params = {}

    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = {}

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    if request.urlparams[0] in request.session['shopping_cart'].keys():
        request.session['shopping_cart'][request.urlparams[0]] = int(request.session['shopping_cart'][request.urlparams[0]]) + int(request.urlparams[1])

    else:
        request.session['shopping_cart'][request.urlparams[0]] = int(request.urlparams[1])

    # Save session variable changes
    request.session.modified = True

    keys = request.session['shopping_cart'].keys()
    item = chfmod.ProductSpecification.objects.filter(id__in=keys)

    keys = request.session['rental_cart'].keys()
    rental = chfmod.ProductSpecification.objects.filter(id__in=keys)

    params['rentals'] = rental
    params['items'] = item
    return templater.render_to_response(request, '/account.shoppingcart.html', params)

@view_function
def deletecartitems(request):

    params = {}

    item = request.urlparams[0]
    del request.session['shopping_cart'][str(item)]
    request.session.modified = True
    keys = request.session['shopping_cart'].keys()
    return HttpResponse('''
                <script>
                window.location.href = window.location.href;
                </script>
            ''')

@view_function
@login_required
def checkout(request):

    params = {}

    if request.session['shopping_cart'] or request.session['rental_cart']:

        keys = request.session['shopping_cart'].keys()
        item = chfmod.ProductSpecification.objects.filter(id__in=keys)

        keys = request.session['rental_cart'].keys()
        rental = chfmod.ProductSpecification.objects.filter(id__in=keys)

        params['items'] = item
        params['rentals'] = rental

        return templater.render_to_response(request, '/account.checkout.html', params)

    else:
        return HttpResponseRedirect('items')


@view_function
def confirmation(request):

    params = {}
    keys = request.session['shopping_cart'].keys()
    item = chfmod.ProductSpecification.objects.filter(id__in=keys)

    params['items'] = item


    if request.method=='POST':

        return HttpResponse('''
                <script>
                window.location.href = window.location.href;
                </script>
            ''')

    import requests

    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = 'b6a57a6b718b756064393dd12588130d'

    r = requests.post(API_URL, data={
        'apiKey' : API_KEY,
        'currency': 'usd',
        'amount': '5.99',
        'type': 'Visa',
        'number': '4732817300654',
        'exp_month': '10',
        'exp_year': '15',
        'cvc': '411',
        'name': 'Cosmo Limesandal',
        'description': 'Charge for nothing at all!!!',
    })

    print(r)

    resp = r.json()
    if 'error' in resp:
        print(resp['error'])

    else:
        print(resp['ID'])

    emailbody = templater.render(request, 'checkout_email.html',params)

    email = request.user.email
    send_mail('Confirmation of Your Order #' +resp['ID'], emailbody, settings.EMAIL_HOST_USER, [email],html_message=emailbody, fail_silently=False)


    del request.session['shopping_cart']
    del request.session['rental_cart']
    return templater.render_to_response(request, 'account.confirmation.html', params)