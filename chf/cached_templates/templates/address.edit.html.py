# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423301720.120325
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/address.edit.html'
_template_uri = '/address.edit.html'
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
        def line():
            return render_line(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2 class="edit">Edit Address</h2>\r\n    <form method="POST">\r\n       <div class="table-responsive">\r\n        <table>\r\n            <tr>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n            </tr>\r\n        </table>\r\n       </div>\r\n        <button type="submit" style="margin-right:30px; margin-bottom:30px; float:right;" class="btn btn-primary btn-lg">Save Changes</button>\r\n    </form>\r\n')
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
{"uri": "/address.edit.html", "line_map": {"67": 15, "27": 0, "52": 2, "37": 1, "73": 15, "42": 14, "59": 2, "60": 8, "61": 8, "79": 73}, "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/address.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
