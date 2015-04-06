# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425455861.95391
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/users.html'
_template_uri = '/users.html'
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
        users = context.get('users', UNDEFINED)
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
        __M_writer('\r\n    <a class="btn btn-success" href="/users.create" style="float:right">Create New</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>First Name</th>\r\n                    <th>Last Name</th>\r\n                    <th>Username</th>\r\n                    <th>Email</th>\r\n                </tr>\r\n')
        for user in users:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n                    <td><a href="users.edit/')
            __M_writer(str(user.id))
            __M_writer('">Edit</a><span> | </span><a style="color:#CF000F" href="users.delete/')
            __M_writer(str(user.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/users.html", "line_map": {"64": 2, "71": 2, "72": 12, "73": 13, "74": 14, "75": 14, "76": 15, "77": 15, "78": 16, "79": 16, "80": 17, "81": 17, "82": 18, "83": 18, "84": 18, "85": 18, "86": 21, "27": 0, "92": 86, "37": 1, "42": 24, "52": 25, "58": 25}, "source_encoding": "ascii", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/users.html"}
__M_END_METADATA
"""
