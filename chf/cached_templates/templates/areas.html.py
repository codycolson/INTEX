# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423203841.354626
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/areas.html'
_template_uri = '/areas.html'
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
        def line():
            return render_line(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
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
        __M_writer('\r\n    <a class="btn btn-success" href="/areas.create" style="float:right">Create New</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th></th>\r\n                </tr>\r\n')
        for area in areas:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\r\n                    <td style="text-align:center"><a href="areas.edit/')
            __M_writer(str(area.id))
            __M_writer('">Edit</a><span> | </span><a style="color:#CF000F" href="areas.delete/')
            __M_writer(str(area.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/areas.html", "source_encoding": "ascii", "line_map": {"64": 2, "37": 1, "71": 2, "72": 11, "73": 12, "74": 13, "75": 13, "76": 14, "77": 14, "78": 15, "79": 15, "80": 15, "81": 15, "82": 18, "52": 22, "88": 82, "58": 22, "27": 0, "42": 21}, "uri": "/areas.html"}
__M_END_METADATA
"""
