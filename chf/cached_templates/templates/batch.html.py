# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428205724.788636
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/batch.html'
_template_uri = '/batch.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        batch = context.get('batch', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        batch = context.get('batch', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Customer Name</th>\r\n                    <th>Customer Email</th>\r\n                    <th>Product</th>\r\n                    <th>Date Out</th>\r\n                    <th>Date Due</th>\r\n                </tr>\r\n')
        for b in batch:
            __M_writer('                <tr style="text-align:left;>\r\n                    <td>')
            __M_writer(str(b.transaction.customer.first_name))
            __M_writer(' ')
            __M_writer(str(b.transaction.customer.last_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(b.transaction.customer.email))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(b.rental_product.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(b.date_out.strftime('%B %d, %Y')))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(b.date_due.strftime('%B %d, %Y')))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/batch.html", "uri": "/batch.html", "line_map": {"64": 18, "65": 19, "66": 19, "35": 1, "73": 67, "45": 2, "27": 0, "67": 22, "52": 2, "53": 13, "54": 14, "55": 15, "56": 15, "57": 15, "58": 15, "59": 16, "60": 16, "61": 17, "62": 17, "63": 18}}
__M_END_METADATA
"""
