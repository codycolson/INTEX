# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428217246.547619
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/items.html'
_template_uri = '/items.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="search1">\r\n    <input id="search" placeholder="search"/>\r\n    <a id="searchbox" class="btn btn-primary">search</a>\r\n</div>\r\n')
        for productspecification in items:
            __M_writer('\r\n    <div class="grid-container">\r\n        <div class="item_container">\r\n            <a href="items.view/')
            __M_writer(str(productspecification.id))
            __M_writer('"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( productspecification.photo ))
            __M_writer('"/></a>\r\n            <div>')
            __M_writer(str(productspecification.name))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str(productspecification.price))
            __M_writer('</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/items.html", "line_map": {"64": 12, "65": 13, "66": 13, "27": 0, "36": 1, "72": 66, "41": 17, "47": 2, "55": 2, "56": 7, "57": 8, "58": 11, "59": 11, "60": 11, "61": 11, "62": 11, "63": 12}, "source_encoding": "ascii", "uri": "/items.html"}
__M_END_METADATA
"""
