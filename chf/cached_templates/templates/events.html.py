# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428187888.216899
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/events.html'
_template_uri = '/events.html'
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
        events = context.get('events', UNDEFINED)
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
        __M_writer('\r\n    <a class="btn btn-success" href="/events.create" style="float:right">Create New</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Event Name</th>\r\n                    <th>Description</th>\r\n                    <th>Start Date</th>\r\n                    <th>End Date</th>\r\n                    <th>Map File Name</th>\r\n                </tr>\r\n')
        for event in events:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td><a href="events.details/')
            __M_writer(str(event.id))
            __M_writer('">')
            __M_writer(str(event.name))
            __M_writer('</a></td>\r\n                    <td>')
            __M_writer(str(event.description))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(event.map_file_name))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 2, "71": 2, "72": 13, "73": 14, "74": 15, "75": 15, "76": 15, "77": 15, "78": 16, "79": 16, "80": 17, "81": 17, "82": 18, "83": 18, "84": 19, "85": 19, "86": 22, "27": 0, "92": 86, "37": 1, "42": 25, "52": 26, "58": 26}, "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/events.html", "uri": "/events.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
