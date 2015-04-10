# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428609357.977793
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/users.html'
_template_uri = '/users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'alt']


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
        def title():
            return render_title(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def alt():
            return render_alt(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alt'):
            context['self'].alt(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2>Manage Users</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def alt():
            return render_alt(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>First Name</th>\r\n                    <th>Last Name</th>\r\n                    <th>Username</th>\r\n                    <th>Email</th>\r\n                    <th></th>\r\n                </tr>\r\n')
        for user in users:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n                    <td style="text-align:center"><a href="users.edit/')
            __M_writer(str(user.id))
            __M_writer('">Edit</a><span> | </span><a style="color:#CF000F" href="users.delete/')
            __M_writer(str(user.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n         </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/users.html", "uri": "/users.html", "line_map": {"65": 5, "72": 5, "73": 16, "74": 17, "75": 18, "76": 18, "77": 19, "78": 19, "79": 20, "80": 20, "81": 21, "82": 21, "83": 22, "84": 22, "85": 22, "86": 22, "87": 25, "27": 0, "93": 87, "37": 1, "42": 4, "47": 28, "53": 2, "59": 2}, "source_encoding": "ascii"}
__M_END_METADATA
"""
