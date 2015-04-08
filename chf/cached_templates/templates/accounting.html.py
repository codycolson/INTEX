# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428388090.870834
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/accounting.html'
_template_uri = 'accounting.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['alt', 'title', 'nine']


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
        def alt():
            return render_alt(context._locals(__M_locals))
        itemtrans = context.get('itemtrans', UNDEFINED)
        prodtrans = context.get('prodtrans', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def nine():
            return render_nine(context._locals(__M_locals))
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alt():
            return render_alt(context)
        itemtrans = context.get('itemtrans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>30 day Sale History</h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Item Name</th>\r\n                    <th>Price</th>\r\n                    <th>Quantity</th>\r\n                    <th>Total</th>\r\n                    <th>Purchase Date</th>\r\n                    <th>Customer Name</th>\r\n                </tr>\r\n')
        for t in itemtrans:
            __M_writer('                <tr style="text-align:left">\r\n                    <td><a href="report.itemdetails/')
            __M_writer(str(t.id))
            __M_writer('">')
            __M_writer(str(t.product.name))
            __M_writer('</a></td>\r\n                    <td>$')
            __M_writer(str(t.product.price))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.quantity))
            __M_writer('</td>\r\n                    <td>$')
            __M_writer(str(t.quantity * t.product.price))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.transaction.order_date.strftime('%B %d, %Y')))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.transaction.customer.first_name))
            __M_writer(' ')
            __M_writer(str(t.transaction.customer.last_name))
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
        __M_writer('\r\n<h2>Transactional Accounting</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nine(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        prodtrans = context.get('prodtrans', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def nine():
            return render_nine(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>30 day Rental History</h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Rental Item Name</th>\r\n                    <th>Price per Day</th>\r\n                    <th>Total</th>\r\n                    <th>Date In</th>\r\n                    <th>Date Due</th>\r\n                    <th>Date In</th>\r\n                    <th>Customer Name</th>\r\n                </tr>\r\n')
        for t in prodtrans:
            __M_writer('                <tr style="text-align:left">\r\n                    <td><a href="report.itemdetails/')
            __M_writer(str(t.id))
            __M_writer('">')
            __M_writer(str(t.rental_product.name))
            __M_writer('</a></td>\r\n                    <td>$')
            __M_writer(str(t.rental_product.price_per_day))
            __M_writer('</td>\r\n                    <td>$')
            __M_writer(str(t.rental_product.price_per_day * (int(t.date_due.strftime('%d')) - int(t.date_out.strftime('%d')))))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.date_out.strftime('%B %d, %Y')))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.date_due.strftime('%B %d, %Y')))
            __M_writer('</td>\r\n')
            if t.date_in:
                __M_writer('                    <td>')
                __M_writer(str(t.date_in.strftime('%B %d, %Y')))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                    <td>-</td>\r\n')
            __M_writer('                    <td>')
            __M_writer(str(t.transaction.customer.first_name))
            __M_writer(' ')
            __M_writer(str(t.transaction.customer.last_name))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/accounting.html", "line_map": {"128": 52, "129": 53, "130": 54, "131": 54, "132": 54, "133": 55, "134": 56, "135": 58, "136": 58, "137": 58, "138": 58, "139": 58, "140": 61, "146": 140, "27": 0, "41": 1, "46": 4, "51": 31, "56": 64, "62": 5, "69": 5, "70": 18, "71": 19, "72": 20, "73": 20, "74": 20, "75": 20, "76": 21, "77": 21, "78": 22, "79": 22, "80": 23, "81": 23, "82": 24, "83": 24, "84": 25, "85": 25, "86": 25, "87": 25, "88": 28, "94": 2, "100": 2, "106": 32, "114": 32, "115": 46, "116": 47, "117": 48, "118": 48, "119": 48, "120": 48, "121": 49, "122": 49, "123": 50, "124": 50, "125": 51, "126": 51, "127": 52}, "source_encoding": "ascii", "uri": "accounting.html"}
__M_END_METADATA
"""
