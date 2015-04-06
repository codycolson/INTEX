# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772717.349624
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/items.view.html'
_template_uri = '/items.view.html'
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
        item = context.get('item', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def line():
            return render_line(context._locals(__M_locals))
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
        item = context.get('item', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="main" class="photo">\r\n        <img class="main_photo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer(str( item.photo.image ))
        __M_writer('"/>\r\n    </div>\r\n    <div class="info">\r\n        <h4>')
        __M_writer(str( item.name ))
        __M_writer('</h4>\r\n        <div class="price">$')
        __M_writer(str(item.price))
        __M_writer('</div>\r\n        <div class="description">')
        __M_writer(str(item.description))
        __M_writer('</div>\r\n        <select id="select">\r\n            <option value="0">Select a Quantity</option>\r\n            <option value="1">1</option>\r\n            <option value="2">2</option>\r\n            <option value="3">3</option>\r\n            <option value="4">4</option>\r\n            <option value="5">5</option>\r\n        </select>\r\n        <button rel="')
        __M_writer(str( item.id ))
        __M_writer('" disabled="true" id="add_to_cart" class="btn btn-warning">Add to Cart</button>\r\n    </div>\r\n\r\n\r\n')
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
{"uri": "/items.view.html", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/items.view.html", "line_map": {"64": 4, "65": 7, "66": 7, "67": 8, "68": 8, "69": 9, "38": 1, "71": 18, "72": 18, "43": 22, "78": 23, "84": 23, "53": 2, "90": 84, "27": 0, "70": 9, "61": 2, "62": 4, "63": 4}, "source_encoding": "ascii"}
__M_END_METADATA
"""
