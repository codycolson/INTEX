# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428612037.145222
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.rentalcart.html'
_template_uri = '/account.rentalcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']



from datetime import datetime, timedelta
now = datetime.now()
noww = now.strftime('%B %d, %Y')


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(nowww = noww - timedelta(days=3)))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<table class="table-responsive table-striped">\r\n    <th></th>\r\n    <th>#</th>\r\n    <th>Name</th>\r\n    <th>Price per Day</th>\r\n    <th># of Days Rented</th>\r\n')
        for item in rentals:
            __M_writer('    <tr>\r\n        <td><button rel="')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-danger btn-sm deleter">Remove</button></td>\r\n        <td class="img-col"><img class="shopping_cart_image" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( item.photo.image ))
            __M_writer('"/></td>\r\n        <td class="name-col">')
            __M_writer(str( noww ))
            __M_writer('</td>\r\n        <td class="price-col">')
            __M_writer(str( item.price_per_day ))
            __M_writer('</td>\r\n        <td class="qty-col">')
            __M_writer(str(int(request.session['rental_cart'][str(item.id)])))
            __M_writer('</td>\r\n    </tr>\r\n')
        __M_writer('</table>\r\n<table id="button-table" class="table-responsive">\r\n    <tr>\r\n        <td id="space"></td>\r\n')
        if request.user.is_authenticated():
            __M_writer('        <td id=\'checkout\'><a href="/account.checkout" class="btn btn-warning">Checkout</a></td>\r\n')
        else:
            __M_writer('        <td id=\'checkout\'><a href="/mylogin.cartlogin" class="btn btn-warning">Checkout</a></td>\r\n')
        __M_writer('    </tr>\r\n</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/account.rentalcart.html", "line_map": {"70": 8, "71": 16, "72": 17, "73": 18, "74": 18, "75": 19, "76": 19, "77": 19, "78": 20, "79": 20, "80": 21, "81": 21, "82": 22, "83": 22, "84": 25, "85": 29, "86": 30, "87": 31, "88": 32, "89": 34, "95": 89, "33": 0, "16": 2, "45": 1, "46": 6, "47": 7, "48": 7, "53": 36, "59": 8}, "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.rentalcart.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
