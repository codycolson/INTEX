# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428517625.278169
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/users.edit.html'
_template_uri = '/users.edit.html'
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
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def alt():
            return render_alt(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alt'):
            context['self'].alt(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<p class="back"><a href="/report.accounting">< Back</a></p>\r\n<h2>Edit User</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def alt():
            return render_alt(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="item-details table-responsive">\r\n       <form method="post">\r\n        <table class="table table-striped table-bordered">\r\n            <tr style="text-align:left">\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n            </tr>\r\n        </table>\r\n\r\n        <button class="btn btn-success" type="submit">Save Changes</button>\r\n    </form>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/users.edit.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/users.edit.html", "source_encoding": "ascii", "line_map": {"64": 6, "52": 2, "37": 1, "71": 6, "72": 11, "73": 11, "58": 2, "27": 0, "42": 5, "79": 73}}
__M_END_METADATA
"""
