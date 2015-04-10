# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428521036.209323
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.view.html'
_template_uri = '/products.view.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['breadcrumbs', 'content', 'line']


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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def line():
            return render_line(context._locals(__M_locals))
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def breadcrumbs():
            return render_breadcrumbs(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n<ol class="breadcrumb">\r\n    <li><a href="/products">Products</a></li>\r\n    <li><a href="/products/')
        __M_writer(str(item.category.id))
        __M_writer('">')
        __M_writer(str(item.category.name))
        __M_writer('</a></li>\r\n    <li><a href="/products/')
        __M_writer(str(item.category.id))
        __M_writer('/')
        __M_writer(str(item.subcategory.id))
        __M_writer('">')
        __M_writer(str(item.subcategory.name or ''))
        __M_writer('</a></li>\r\n</ol>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="main" class="photo">\r\n        <img class="main_photo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer(str( item.photo.image ))
        __M_writer('"/>\r\n    </div>\r\n    <div class="info">\r\n        <h4>')
        __M_writer(str( item.name ))
        __M_writer('</h4>\r\n        <div class="price">Price per day $')
        __M_writer(str(item.price_per_day))
        __M_writer('</div>\r\n        <div class="description">')
        __M_writer(str(item.description))
        __M_writer('</div>\r\n')
        if request.user.is_staff:
            __M_writer('        <select style="float:left" id="select">\r\n            <option value="0">Number of Days</option>\r\n            <option value="1">1</option>\r\n            <option value="2">2</option>\r\n            <option value="3">3</option>\r\n            <option value="4">4</option>\r\n            <option value="5">5</option>\r\n        </select>\r\n        <button rel="')
            __M_writer(str( item.id ))
            __M_writer('" disabled="true" id="add_to_cart" class="btn btn-warning">Add to Cart</button>\r\n')
        else:
            __M_writer('        <button disabled="true" class="btn">This item available to rent in store</button>\r\n')
        __M_writer('    </div>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'breadcrumbs'):
            context['self'].breadcrumbs(**pageargs)
        

        __M_writer('\r\n')
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
{"uri": "/products.view.html", "line_map": {"64": 29, "65": 29, "66": 29, "67": 29, "68": 30, "69": 30, "70": 30, "71": 30, "72": 30, "73": 30, "79": 2, "99": 9, "129": 123, "90": 2, "91": 4, "92": 4, "93": 4, "94": 7, "95": 7, "96": 8, "97": 8, "98": 9, "27": 0, "100": 10, "101": 11, "102": 19, "103": 19, "104": 20, "41": 1, "106": 23, "46": 34, "111": 33, "117": 35, "105": 21, "56": 25, "123": 35, "63": 25}, "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.view.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
