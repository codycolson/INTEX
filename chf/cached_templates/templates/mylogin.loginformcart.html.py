# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428609181.767699
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/mylogin.loginformcart.html'
_template_uri = 'mylogin.loginformcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer('\r\n    <div class="table-responsive">\r\n       <form id="loginform" method="post" action="mylogin.loginformcart">\r\n        <table>\r\n            <tr>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n            </tr>\r\n        </table>\r\n        <a href="/password_reset/">Forgot your password?</a></br>\r\n        <a style="float:left;" href="/account.create/">Create an Account!</a>\r\n        <button id="login-button" class="btn btn-success" type="submit">Login</button>\r\n    </form>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/mylogin.loginformcart.html", "uri": "mylogin.loginformcart.html", "line_map": {"35": 1, "53": 2, "54": 7, "55": 7, "40": 15, "27": 0, "61": 55, "46": 2}, "source_encoding": "ascii"}
__M_END_METADATA
"""
