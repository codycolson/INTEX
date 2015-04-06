# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428267412.814173
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.rentalreturn.html'
_template_uri = '/products.rentalreturn.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title']


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
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for product in products:
            __M_writer('\r\n    <div class="grid-container">\r\n        <div class="item_container">\r\n            <a href="products.viewreturn/')
            __M_writer(str(product.id))
            __M_writer('"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( product.rental_product.photo ))
            __M_writer('"/></a>\r\n            <div>')
            __M_writer(str(product.rental_product.name))
            __M_writer('</div>\r\n            <div>')
            __M_writer(str(product.transaction.customer.first_name))
            __M_writer('</div>\r\n            <div>Due: ')
            __M_writer(str(product.date_due.strftime('%B %d, %Y')))
            __M_writer('</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div style="height:150px;">\r\n    <div class="search1">\r\n        <input id="search" placeholder="search"/>\r\n        <a id="searchbox" class="btn btn-primary">search</a>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.rentalreturn.html", "uri": "/products.rentalreturn.html", "line_map": {"64": 13, "65": 16, "66": 16, "67": 16, "68": 16, "69": 16, "70": 17, "71": 17, "72": 18, "73": 18, "74": 19, "75": 19, "81": 2, "87": 2, "27": 0, "93": 87, "38": 1, "43": 9, "48": 23, "54": 10, "62": 10, "63": 12}, "source_encoding": "ascii"}
__M_END_METADATA
"""
