# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428478221.564953
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/events.html'
_template_uri = '/events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['alt', 'title', 'line']


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
        def alt():
            return render_alt(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
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


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alt():
            return render_alt(context)
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Manage Events</h2>\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "/events.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/events.html", "source_encoding": "ascii", "line_map": {"66": 5, "67": 16, "68": 17, "69": 18, "70": 18, "71": 18, "72": 18, "73": 19, "74": 19, "75": 20, "76": 20, "77": 21, "78": 21, "79": 22, "80": 22, "81": 25, "87": 2, "27": 0, "93": 2, "99": 29, "39": 1, "105": 29, "44": 4, "111": 105, "49": 28, "59": 5}}
__M_END_METADATA
"""
