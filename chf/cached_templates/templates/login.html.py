# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423676053.746566
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/mylogin.html'
_template_uri = 'mylogin.html'
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
        form = context.get('form', UNDEFINED)
        next = context.get('next', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        next = context.get('next', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2 class="edit">Login to CHF</h2>\r\n')
        if next:
            __M_writer('    <form action="/login/?next=')
            __M_writer(str( next ))
            __M_writer('" method="post" >\r\n')
        __M_writer('       <div class="table-responsive">\r\n        <table>\r\n            <tr>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n            </tr>\r\n        </table>\r\n       </div>\r\n        <button type="submit" style="margin-right:30px; margin-bottom:30px; float:right;" class="btn btn-primary btn-lg">Login</button>\r\n    </form>\r\n')
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
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/mylogin.html", "source_encoding": "ascii", "uri": "mylogin.html", "line_map": {"64": 5, "65": 5, "66": 7, "67": 10, "68": 10, "38": 1, "74": 17, "43": 16, "80": 17, "53": 2, "86": 80, "27": 0, "61": 2, "62": 4, "63": 5}}
__M_END_METADATA
"""
