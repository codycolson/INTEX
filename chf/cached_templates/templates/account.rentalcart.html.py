# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428230005.744357
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/account.rentalcart.html'
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
        rentals = context.get('rentals', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def content():
            return render_content(context)
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        __M_writer('</table>\r\n<table id="button-table" class="table-responsive">\r\n    <tr>\r\n        <td id="space"></td>\r\n        <td id=\'checkout\'><a href="/account.checkout" class="btn btn-warning">Checkout</a></td>\r\n    </tr>\r\n</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/account.rentalcart.html", "line_map": {"70": 8, "71": 16, "72": 17, "73": 18, "74": 18, "75": 19, "76": 19, "77": 19, "78": 20, "79": 20, "80": 21, "81": 21, "82": 22, "83": 22, "84": 25, "90": 84, "33": 0, "16": 2, "45": 1, "46": 6, "47": 7, "48": 7, "53": 32, "59": 8}, "source_encoding": "ascii", "uri": "/account.rentalcart.html"}
__M_END_METADATA
"""
