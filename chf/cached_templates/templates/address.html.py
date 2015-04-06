# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428204683.880858
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/address.html'
_template_uri = '/address.html'
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
        addresses = context.get('addresses', UNDEFINED)
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
        __M_writer('\r\n    <a class="btn btn-success" href="/address.create" style="float:right">Create New</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        addresses = context.get('addresses', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Address 1</th>\r\n                    <th>Address 2</th>\r\n                    <th>City</th>\r\n                    <th>State</th>\r\n                    <th>Zip</th>\r\n                    <th></th>\r\n                </tr>\r\n')
        for address in addresses:
            __M_writer('                <tr style="text-align:left;">\r\n                    <td>')
            __M_writer(str(address.street1))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(address.street2))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(address.city))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(address.state))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(address.zip_code))
            __M_writer('</td>\r\n                    <td><a href="address.edit/')
            __M_writer(str(address.id))
            __M_writer('">Edit</a><span> | </span><a style="color:#CF000F" href="address.delete/')
            __M_writer(str(address.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/address.html", "line_map": {"64": 2, "71": 2, "72": 14, "73": 15, "74": 16, "75": 16, "76": 17, "77": 17, "78": 18, "79": 18, "80": 19, "81": 19, "82": 20, "83": 20, "84": 21, "85": 21, "86": 21, "87": 21, "88": 24, "27": 0, "94": 88, "37": 1, "42": 27, "52": 28, "58": 28}, "source_encoding": "ascii", "uri": "/address.html"}
__M_END_METADATA
"""
