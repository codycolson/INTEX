# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428193916.031217
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/events.details.html'
_template_uri = '/events.details.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'alt', 'line']


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
        areas = context.get('areas', UNDEFINED)
        def alt():
            return render_alt(context._locals(__M_locals))
        def line():
            return render_line(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alt'):
            context['self'].alt(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'line'):
            context['self'].line(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        event = context.get('event', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>')
        __M_writer(str(event.name))
        __M_writer('</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        def alt():
            return render_alt(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>Areas</h4>\r\n<div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                </tr>\r\n')
        for area in areas:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def line():
            return render_line(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>Expected On-Site Sale Items</h4>\r\n<div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th>Low Price</th>\r\n                    <th>High Price</th>\r\n                </tr>\r\n')
        for product in products:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(product.low_price))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(product.high_price))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/events.details.html", "line_map": {"68": 2, "69": 3, "70": 3, "76": 5, "83": 5, "84": 14, "85": 15, "86": 16, "87": 16, "88": 17, "89": 17, "90": 20, "27": 0, "96": 24, "110": 39, "103": 24, "104": 35, "105": 36, "106": 37, "107": 37, "108": 38, "109": 38, "46": 4, "111": 39, "112": 40, "113": 40, "114": 43, "51": 23, "41": 1, "120": 114, "61": 2}, "uri": "/events.details.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
