# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426723403.086558
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/account.html'
_template_uri = '/account.html'
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
        request = context.get('request', UNDEFINED)
        def line():
            return render_line(context._locals(__M_locals))
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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2 class="edit">Your Account</h2>\r\n       <div class="table-responsive">\r\n        <table>\r\n            <tr>\r\n                <td class="header"><b>First Name: </b></td>\r\n                <td>')
        __M_writer(str( request.user.first_name ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Last Name: </b></td>\r\n                <td>')
        __M_writer(str( request.user.last_name ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Email: </b></td>\r\n                <td>')
        __M_writer(str( request.user.email ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Phone: </b></td>\r\n                <td>')
        __M_writer(str( request.user.phone ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Organization Name: </b></td>\r\n                <td>')
        __M_writer(str( request.user.organization_name ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Organization Type: </b></td>\r\n                <td>')
        __M_writer(str( request.user.organization_type ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Emergency Contact: </b></td>\r\n                <td>')
        __M_writer(str( request.user.emergency_contact ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Emergency Phone: </b></td>\r\n                <td>')
        __M_writer(str( request.user.emergency_phone ))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td class="header"><b>Emergency Relationship: </b></td>\r\n                <td>')
        __M_writer(str( request.user.emergency_relationship ))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n       </div>\r\n    <button id="change_password" style="margin-left:30px; margin-bottom:30px; float:left;" class="btn btn-warning btn-lg">Change Password</button>\r\n    <button id="show_account_edit" style="margin-right:30px; margin-bottom:30px; float:right;" class="btn btn-warning btn-lg">Change Info</button>\r\n')
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
{"line_map": {"64": 16, "65": 16, "66": 20, "67": 20, "68": 24, "69": 24, "70": 28, "71": 28, "72": 32, "73": 32, "74": 36, "75": 36, "76": 40, "77": 40, "83": 47, "89": 47, "27": 0, "95": 89, "37": 1, "42": 46, "52": 2, "59": 2, "60": 8, "61": 8, "62": 12, "63": 12}, "uri": "/account.html", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/account.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
