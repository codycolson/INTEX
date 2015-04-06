# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428278553.557457
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.viewreturn.html'
_template_uri = '/products.viewreturn.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def line():
            return render_line(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'line'):
            context['self'].line(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="main" class="photo">\r\n        <img class="main_photo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer(str( item.rental_product.photo ))
        __M_writer('"/>\r\n    </div>\r\n    <div class="info">\r\n        <h4>')
        __M_writer(str( item.rental_product.name ))
        __M_writer('</h4>\r\n        <div class="price">Price per day $')
        __M_writer(str(item.rental_product.price_per_day))
        __M_writer('</div>\r\n        <div class="description"><b>Date Rented:</b> ')
        __M_writer(str(item.date_out.strftime('%B %d, %Y')))
        __M_writer('</div>\r\n        <div class="description"><b>Date Due:</b> ')
        __M_writer(str(item.date_due.strftime('%B %d, %Y')))
        __M_writer('</div>\r\n        <div class="description">Damage notes: </br><textarea rows="4" cols="50">')
        __M_writer(str(item.rental_product.notes))
        __M_writer('</textarea></div>\r\n        <div class="description">Damage fee: <input rows="4" cols="50"/></div>\r\n        <div class="description"><a href="products.return/')
        __M_writer(str( item.id ))
        __M_writer('" class="btn btn-warning">Return this Item</a></div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def line():
            return render_line(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "/products.viewreturn.html", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.viewreturn.html", "line_map": {"64": 4, "65": 7, "66": 7, "67": 8, "68": 8, "69": 9, "70": 9, "71": 10, "72": 10, "73": 11, "74": 11, "75": 13, "76": 13, "82": 18, "88": 18, "27": 0, "94": 88, "38": 1, "43": 17, "53": 2, "61": 2, "62": 4, "63": 4}}
__M_END_METADATA
"""
