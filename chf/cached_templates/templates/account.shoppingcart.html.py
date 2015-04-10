# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428611815.384179
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.shoppingcart.html'
_template_uri = '/account.shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<table class="table-responsive table-striped">\r\n    <th></th>\r\n    <th>#</th>\r\n    <th>Name</th>\r\n    <th>Price</th>\r\n    <th>Quantity</th>\r\n')
        for item in items:
            __M_writer('    <tr>\r\n        <td><button rel="')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-danger btn-sm deleter">Remove</button></td>\r\n        <td class="img-col"><img class="shopping_cart_image" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( item.photo.image ))
            __M_writer('"/></td>\r\n        <td class="name-col">')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n        <td class="price-col">')
            __M_writer(str( item.price ))
            __M_writer('</td>\r\n        <td class="qty-col">')
            __M_writer(str( request.session['shopping_cart'][str(item.id)] ))
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
{"filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.shoppingcart.html", "uri": "/account.shoppingcart.html", "line_map": {"64": 12, "65": 12, "66": 12, "67": 13, "68": 13, "69": 14, "70": 14, "71": 15, "72": 15, "73": 18, "74": 22, "75": 23, "76": 24, "77": 25, "78": 27, "84": 78, "27": 0, "38": 1, "43": 29, "49": 2, "59": 2, "60": 9, "61": 10, "62": 11, "63": 11}, "source_encoding": "ascii"}
__M_END_METADATA
"""
