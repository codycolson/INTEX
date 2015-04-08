# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428478156.02334
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/itemdetails.html'
_template_uri = 'itemdetails.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['alt', 'title']


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
        prod = context.get('prod', UNDEFINED)
        def alt():
            return render_alt(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
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


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        prod = context.get('prod', UNDEFINED)
        def alt():
            return render_alt(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if item:
            __M_writer('<div class="item-details table-responsive">\r\n    <table class="table table-striped table-bordered">\r\n        <tbody>\r\n        <tr style="text-align:left">\r\n            <td>Product Name</td>\r\n            <td>')
            __M_writer(str(item.product.name))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Price</td>\r\n            <td>')
            __M_writer(str(item.product.price))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Quantity</td>\r\n            <td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Description</td>\r\n            <td>')
            __M_writer(str(item.product.description))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Manufacturer</td>\r\n            <td>')
            __M_writer(str(item.product.manufacturer))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Average Cost</td>\r\n            <td>')
            __M_writer(str(item.product.average_cost))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>SKU</td>\r\n            <td>')
            __M_writer(str(item.product.sku))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Order Form Name</td>\r\n            <td>')
            __M_writer(str(item.product.order_form_name or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Production Time</td>\r\n            <td>')
            __M_writer(str(item.product.production_time or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Category</td>\r\n            <td>')
            __M_writer(str(item.product.category))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Owner</td>\r\n            <td>')
            __M_writer(str(item.product.owner or "CHF"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Photo File Name</td>\r\n            <td>')
            __M_writer(str(item.product.photo))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Quantity on Hand</td>\r\n            <td>')
            __M_writer(str(item.product.quantity_on_hand))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Shelf Location</td>\r\n            <td>')
            __M_writer(str(item.product.shelf_location or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Product Order File</td>\r\n            <td>')
            __M_writer(str(item.product.product_order_file or "-" ))
            __M_writer('</td>\r\n        </tr>\r\n        </tbody>\r\n    </table>\r\n</div>\r\n')
        else:
            __M_writer('    <div class="item-details table-responsive">\r\n    <table class="table table-striped table-bordered">\r\n        <tbody>\r\n        <tr style="text-align:left">\r\n            <td>Product Name</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.name))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Price</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.price))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Quantity</td>\r\n            <td>')
            __M_writer(str(prod.quantity))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Description</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.description))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Manufacturer</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.manufacturer))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Average Cost</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.average_cost))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>SKU</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.sku))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Order Form Name</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.order_form_name or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Production Time</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.production_time or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Category</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.category))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Owner</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.owner or "CHF"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Photo File Name</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.photo))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Quantity on Hand</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.quantity_on_hand))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Shelf Location</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.shelf_location or "-"))
            __M_writer('</td>\r\n        </tr><tr style="text-align:left">\r\n            <td>Product Order File</td>\r\n            <td>')
            __M_writer(str(prod.rental_product.product_order_file or "-" ))
            __M_writer('</td>\r\n        </tbody>\r\n    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n<p class="back"><a href="/report.accounting">< Back</a></p>\r\n<h2>Line Item Details</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "itemdetails.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/itemdetails.html", "source_encoding": "ascii", "line_map": {"131": 2, "137": 2, "143": 137, "27": 0, "38": 1, "43": 5, "53": 6, "61": 6, "62": 7, "63": 8, "64": 13, "65": 13, "66": 16, "67": 16, "68": 19, "69": 19, "70": 22, "71": 22, "72": 25, "73": 25, "74": 28, "75": 28, "76": 31, "77": 31, "78": 34, "79": 34, "80": 37, "81": 37, "82": 40, "83": 40, "84": 43, "85": 43, "86": 46, "87": 46, "88": 49, "89": 49, "90": 52, "91": 52, "92": 55, "93": 55, "94": 60, "95": 61, "96": 66, "97": 66, "98": 69, "99": 69, "100": 72, "101": 72, "102": 75, "103": 75, "104": 78, "105": 78, "106": 81, "107": 81, "108": 84, "109": 84, "110": 87, "111": 87, "112": 90, "113": 90, "114": 93, "115": 93, "116": 96, "117": 96, "118": 99, "119": 99, "120": 102, "121": 102, "122": 105, "123": 105, "124": 108, "125": 108}}
__M_END_METADATA
"""
