# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428475191.858965
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.view.html'
_template_uri = '/products.view.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['line', 'content', 'breadcrumbs']


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
        item = context.get('item', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        def line():
            return render_line(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        def breadcrumbs():
            return render_breadcrumbs(context)
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


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n<ol class="breadcrumb">\r\n    <li><a href="/products">Products</a></li>\r\n    <li><a href="/products/')
        __M_writer(str(item.category.id))
        __M_writer('">')
        __M_writer(str(item.category.name))
        __M_writer('</a></li>\r\n    <li><a href="/products/')
        __M_writer(str(item.subcategory.id))
        __M_writer('">')
        __M_writer(str(item.subcategory.name or ''))
        __M_writer('</a></li>\r\n</ol>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"68": 2, "79": 2, "80": 4, "81": 4, "82": 4, "83": 7, "84": 7, "85": 8, "86": 8, "87": 9, "88": 9, "89": 10, "90": 11, "91": 19, "92": 19, "93": 20, "94": 21, "95": 23, "27": 0, "100": 33, "120": 30, "41": 1, "106": 25, "46": 34, "113": 25, "114": 29, "115": 29, "116": 29, "117": 29, "118": 30, "119": 30, "56": 35, "121": 30, "62": 35, "127": 121}, "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.view.html", "uri": "/products.view.html"}
__M_END_METADATA
"""
