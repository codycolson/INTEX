# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428477035.381733
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.html'
_template_uri = '/account.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        def alt():
            return render_alt(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def line():
            return render_line(context._locals(__M_locals))
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
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Account Details</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alt():
            return render_alt(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="account-details table-responsive">\r\n    <table class="table table-striped table-bordered">\r\n        <tbody>\r\n        <tr class="text-left">\r\n            <td>First Name</td>\r\n            <td>')
        __M_writer(str(request.user.first_name))
        __M_writer('</td>\r\n        </tr><tr class="text-left">\r\n            <td>Last Name</td>\r\n            <td>')
        __M_writer(str(request.user.last_name))
        __M_writer('</td>\r\n        </tr><tr class="text-left">\r\n            <td>Email</td>\r\n            <td>')
        __M_writer(str(request.user.email))
        __M_writer('</td>\r\n        </tr><tr class="text-left">\r\n            <td>Phone</td>\r\n            <td>')
        __M_writer(str(request.user.phone))
        __M_writer('</td>\r\n        </tr><tr class="text-left">\r\n            <td>Organization Name</td>\r\n            <td>')
        __M_writer(str(request.user.organization_name))
        __M_writer('</td>\r\n        </tr>\r\n        <tr class="text-left">\r\n            <td>Organization Type</td>\r\n            <td>')
        __M_writer(str(request.user.organization_type))
        __M_writer('</td>\r\n        </tr>\r\n        <tr class="text-left">\r\n            <td>Emergency Contact</td>\r\n            <td>')
        __M_writer(str(request.user.emergency_contact))
        __M_writer('</td>\r\n        </tr>\r\n        <tr class="text-left">\r\n            <td>Emergency Phone</td>\r\n            <td>')
        __M_writer(str(request.user.emergency_phone))
        __M_writer('</td>\r\n        </tr>\r\n        <tr class="text-left">\r\n            <td>Emergency Relationship</td>\r\n            <td>')
        __M_writer(str(request.user.emergency_relationship))
        __M_writer('</td>\r\n        </tr>\r\n        </tbody>\r\n        </table>    <button id="change_password" style="margin-left:30px; margin-bottom:30px; float:left;" class="btn btn-warning btn-lg">Change Password</button>\r\n    <button id="show_account_edit" style="margin-right:30px; margin-bottom:30px; float:right;" class="btn btn-warning btn-lg">Change Info</button>\r\n\r\n       </div>\r\n')
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
{"source_encoding": "ascii", "line_map": {"65": 2, "71": 5, "108": 47, "78": 5, "79": 11, "80": 11, "81": 14, "82": 14, "83": 17, "84": 17, "85": 20, "86": 20, "87": 23, "88": 23, "89": 27, "90": 27, "27": 0, "92": 31, "93": 35, "94": 35, "95": 39, "96": 39, "91": 31, "102": 47, "39": 1, "44": 4, "49": 46, "114": 108, "59": 2}, "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/account.html", "uri": "/account.html"}
__M_END_METADATA
"""
