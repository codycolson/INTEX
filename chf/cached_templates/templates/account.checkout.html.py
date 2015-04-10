# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428634392.317029
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.checkout.html'
_template_uri = '/account.checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'line']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def line():
            return render_line(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'line'):
            context['self'].line(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h3 class="head">Confirm Your Order</h3>\r\n')
        if request.user.is_staff:
            __M_writer('    <div>')
            __M_writer(str(form))
            __M_writer('</div>\r\n')
        if request.session['shopping_cart']:
            __M_writer('<div class="col-md-6" style="margin-top:30px;"><h4>Shopping Cart</h4>\r\n<table class="table-responsive table-striped left">\r\n    <th>#</th>\r\n    <th>Name</th>\r\n    <th>Price</th>\r\n    <th>Quantity</th>\r\n')
            for item in items:
                __M_writer('    <tr>\r\n        <td class="img-col"><img class="shopping_cart_image" src="')
                __M_writer(str(STATIC_URL))
                __M_writer(str( item.photo.image ))
                __M_writer('"/></td>\r\n        <td class="name-col">')
                __M_writer(str( item.name ))
                __M_writer('</td>\r\n        <td class="price-col">')
                __M_writer(str( item.price ))
                __M_writer('</td>\r\n        <td class="qty-col">')
                __M_writer(str( request.session['shopping_cart'][str(item.id)] ))
                __M_writer('</td>\r\n    </tr>\r\n')
            __M_writer('</table>\r\n</div>\r\n')
        if request.session['rental_cart']:
            __M_writer('<div class="col-md-6" style="margin-top:30px;float:right;"><h4>Rental Cart</h4>\r\n<table class="table-responsive table-striped left">\r\n    <th>#</th>\r\n    <th>Name</th>\r\n    <th>Price per Day</th>\r\n    <th># of Days Rented</th>\r\n')
            for rental in rentals:
                __M_writer('    <tr>\r\n        <td class="img-col"><img class="shopping_cart_image" src="')
                __M_writer(str(STATIC_URL))
                __M_writer(str( rental.photo.image ))
                __M_writer('"/></td>\r\n        <td class="name-col">')
                __M_writer(str( rental.name ))
                __M_writer('</td>\r\n        <td class="price-col">')
                __M_writer(str( rental.price_per_day ))
                __M_writer('</td>\r\n        <td class="qty-col">')
                __M_writer(str( request.session['rental_cart'][str(rental.id)] ))
                __M_writer('</td>\r\n    </tr>\r\n')
            __M_writer('</table>\r\n</div>\r\n')
        __M_writer('\r\n<table class="table-responsive right">\r\n    <th class="info-head">Please fill out your shipping information</th>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Street 1" type="text"/></td>\r\n        <td class="input"><input placeholder="Street 2" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="City" type="text"/></td>\r\n        <td class="input"><input placeholder="State" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Zip Code" type="text"/></td>\r\n        <td class="input"><input placeholder="Phone" type="text"/></td>\r\n    </tr>\r\n\r\n</table>\r\n\r\n<table id="table-billing" class="table-responsive right">\r\n    <th class="info-head">Please fill out your billing information</th>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Billing Street 1" type="text"/></td>\r\n        <td class="input"><input placeholder="Billing Street 2" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Billing City" type="text"/></td>\r\n        <td class="input"><input placeholder="Billing State" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Billing Zip Code" type="text"/></td>\r\n        <td class="input"><input placeholder="Billing Phone" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Name on Card" type="text"/></td>\r\n        <td class="input"><input placeholder="Credit Card Number" type="text"/></td>\r\n    </tr>\r\n    <tr class="roww">\r\n        <td class="input"><input placeholder="Expiration Date" type="text"/></td>\r\n        <td class="input"><input placeholder="CVV Code" type="text"/></td>\r\n    </tr>\r\n</table>\r\n\r\n<table>\r\n\r\n\r\n</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def line():
            return render_line(context)
        __M_writer = context.writer()
        __M_writer('\r\n<button id="checkout" method="POST" class="btn btn-warning">Place Order</button>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"70": 2, "71": 4, "72": 5, "73": 5, "74": 5, "75": 7, "76": 8, "77": 14, "78": 15, "79": 16, "80": 16, "81": 16, "82": 17, "83": 17, "84": 18, "85": 18, "86": 19, "87": 19, "88": 22, "89": 25, "90": 26, "27": 0, "92": 33, "93": 34, "94": 34, "95": 34, "96": 35, "97": 35, "98": 36, "91": 32, "100": 37, "101": 37, "102": 40, "103": 43, "42": 1, "109": 91, "47": 90, "99": 36, "115": 91, "52": 93, "121": 115, "58": 2}, "uri": "/account.checkout.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
