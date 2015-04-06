# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428210930.313241
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/report.html'
_template_uri = '/report.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'nine', 'line', 'alt', '']


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
        batch2 = context.get('batch2', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def nine():
            return render_nine(context._locals(__M_locals))
        def __M_anon_81():
            return render___M_anon_81(context._locals(__M_locals))
        def alt():
            return render_alt(context._locals(__M_locals))
        batch3 = context.get('batch3', UNDEFINED)
        batch1 = context.get('batch1', UNDEFINED)
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nine'):
            context['self'].nine(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'line'):
            context['self'].line(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], '__M_anon_81'):
            context['self'].__M_anon_81(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Overdue Rental Report</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nine(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        batch2 = context.get('batch2', UNDEFINED)
        def nine():
            return render_nine(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>60 days overdue</h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Customer Name</th>\r\n                    <th>Customer Email</th>\r\n                    <th>Product</th>\r\n                    <th>Date Out</th>\r\n                    <th>Date Due</th>\r\n                </tr>\r\n')
        for b in batch2:
            __M_writer('                <tr style="text-align:left">\r\n                    <td>')
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


def render_line(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        batch3 = context.get('batch3', UNDEFINED)
        def line():
            return render_line(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>90+ days overdue</h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Customer Name</th>\r\n                    <th>Customer Email</th>\r\n                    <th>Product</th>\r\n                    <th>Date Out</th>\r\n                    <th>Date Due</th>\r\n                </tr>\r\n')
        for b in batch3:
            __M_writer('                <tr style="text-align:left">\r\n                    <td>')
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
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n<div style="text-align:right;margin-top:30px;"><a href="report.send" class="btn btn-warning">Send Email</a></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        batch1 = context.get('batch1', UNDEFINED)
        def alt():
            return render_alt(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>30 days overdue</h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Customer Name</th>\r\n                    <th>Customer Email</th>\r\n                    <th>Product</th>\r\n                    <th>Date Out</th>\r\n                    <th>Date Due</th>\r\n                </tr>\r\n')
        for b in batch1:
            __M_writer('                <tr style="text-align:left">\r\n                    <td>')
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


def render___M_anon_81(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def __M_anon_81():
            return render___M_anon_81(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/report.html", "source_encoding": "ascii", "line_map": {"128": 69, "129": 70, "130": 70, "131": 71, "132": 71, "133": 72, "134": 72, "135": 73, "136": 73, "137": 76, "143": 5, "150": 5, "151": 17, "152": 18, "153": 19, "154": 19, "27": 0, "156": 19, "157": 20, "158": 20, "159": 21, "160": 21, "161": 22, "162": 22, "155": 19, "164": 23, "165": 26, "171": 81, "45": 1, "177": 81, "50": 4, "55": 29, "60": 54, "65": 80, "75": 2, "81": 2, "163": 23, "87": 30, "94": 30, "95": 42, "96": 43, "97": 44, "98": 44, "99": 44, "100": 44, "101": 45, "102": 45, "103": 46, "104": 46, "105": 47, "106": 47, "107": 48, "108": 48, "109": 51, "183": 177, "115": 55, "122": 55, "123": 67, "124": 68, "125": 69, "126": 69, "127": 69}, "uri": "/report.html"}
__M_END_METADATA
"""
