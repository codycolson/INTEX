# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428224065.897427
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.view.html'
_template_uri = '/products.view.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['line', 'content']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
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
        __M_writer('</div>\r\n        <select style="float:left" id="select">\r\n            <option value="0">Number of Days</option>\r\n            <option value="1">1</option>\r\n            <option value="2">2</option>\r\n            <option value="3">3</option>\r\n            <option value="4">4</option>\r\n            <option value="5">5</option>\r\n        </select>\r\n        <button rel="')
        __M_writer(str( item.id ))
        __M_writer('" disabled="true" id="add_to_cart" class="btn btn-warning">Add to Cart</button>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/products.view.html", "line_map": {"65": 2, "27": 0, "38": 1, "81": 9, "73": 2, "74": 4, "75": 4, "76": 4, "77": 7, "78": 7, "79": 8, "80": 8, "43": 22, "82": 9, "83": 18, "84": 18, "53": 23, "90": 84, "59": 23}, "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/products.view.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
