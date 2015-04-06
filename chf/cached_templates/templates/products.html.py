# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428266156.344023
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.html'
_template_uri = '/products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div style="height:150px;">\r\n    <div class="search1" style="float:left">\r\n    <input id="search" placeholder="search"/>\r\n    <a id="searchbox" class="btn btn-primary">search</a>\r\n</div>\r\n<div class="search2" style="float:right">\r\n    <a id="returnbox" href="products.returnrental" class="btn btn-primary">return an item</a>\r\n</div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for product in products:
            __M_writer('\r\n    <div class="grid-container">\r\n        <div class="item_container">\r\n            <a href="products.view/')
            __M_writer(str(product.id))
            __M_writer('"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( product.photo ))
            __M_writer('"/></a>\r\n            <div>')
            __M_writer(str(product.name))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str(product.price))
            __M_writer('</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/products.html", "line_map": {"80": 19, "66": 13, "43": 12, "38": 1, "91": 85, "74": 13, "75": 15, "76": 16, "77": 19, "78": 19, "79": 19, "48": 25, "81": 19, "82": 20, "83": 20, "84": 21, "85": 21, "54": 2, "27": 0, "60": 2}, "source_encoding": "ascii", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.html"}
__M_END_METADATA
"""
