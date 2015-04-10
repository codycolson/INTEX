# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428564719.71172
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/manage.html'
_template_uri = 'manage.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['alt', 'nine']


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
        prodtrans = context.get('prodtrans', UNDEFINED)
        def alt():
            return render_alt(context._locals(__M_locals))
        def nine():
            return render_nine(context._locals(__M_locals))
        itemtrans = context.get('itemtrans', UNDEFINED)
        __M_writer = context.writer()
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
        __M_writer('\r\n<h2 style="margin-bottom:50px;">Manage Inventory</h2>\r\n<h4>Sale Items<span> </span><a href="items.create">+</a></h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Item Name</th>\r\n                    <th>Description</th>\r\n                    <th>Price</th>\r\n                    <th>Manufacturer</th>\r\n                    <th>Category</th>\r\n                    <th>Subcategory</th>\r\n                    <th>Average Cost</th>\r\n                    <th>SKU</th>\r\n                    <th>Order From Name</th>\r\n                    <th>Production Time</th>\r\n                    <th>Photo</th>\r\n                    <th>Quantity on Hand</th>\r\n                    <th>Shelf Location</th>\r\n                    <th></th>\r\n                </tr>\r\n')
        for t in itemtrans:
            __M_writer('                <tr style="text-align:left">\r\n                    <td>')
            __M_writer(str(t.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.description))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.price))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.manufacturer))
            __M_writer('</td>\r\n')
            if t.category:
                __M_writer('                    <td>')
                __M_writer(str(t.category.name))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                    <td></td>\r\n')
            if t.subcategory:
                __M_writer('                    <td>')
                __M_writer(str(t.subcategory.name))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                    <td></td>\r\n')
            __M_writer('                    <td>')
            __M_writer(str(t.average_cost))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.sku))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.order_form_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.production_time))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.photo))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.quantity_on_hand))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.shelf_location))
            __M_writer('</td>\r\n                    <td><a href="/items.edit/')
            __M_writer(str(t.id))
            __M_writer('">Edit</a><span> | </span><a style="color:red" href="item.delete/')
            __M_writer(str(t.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nine(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nine():
            return render_nine(context)
        prodtrans = context.get('prodtrans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h4>Rental Products<span> </span><a href="items.create">+</a></h4>\r\n    <div class="table-responsive">\r\n        <table class="table table-striped table-bordered">\r\n            <tbody>\r\n                <tr>\r\n                    <th>Item Name</th>\r\n                    <th>Description</th>\r\n                    <th>Price</th>\r\n                    <th>Price per Day</th>\r\n                    <th>Times Rented</th>\r\n                    <th>Cost</th>\r\n                    <th>Manufacturer</th>\r\n                    <th>Category</th>\r\n                    <th>Subcategory</th>\r\n                    <th>Average Cost</th>\r\n                    <th>SKU</th>\r\n                    <th>Order From Name</th>\r\n                    <th>Production Time</th>\r\n                    <th>Photo</th>\r\n                    <th>Quantity on Hand</th>\r\n                    <th>Shelf Location</th>\r\n                    <th></th>\r\n                </tr>\r\n')
        for t in prodtrans:
            __M_writer('                <tr style="text-align:left">\r\n                    <td>')
            __M_writer(str(t.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.description))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.price))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.price_per_day))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.times_rented))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.cost))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.manufacturer))
            __M_writer('</td>\r\n')
            if t.category:
                __M_writer('                    <td>')
                __M_writer(str(t.category.name or ''))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                    <td></td>\r\n')
            if t.subcategory:
                __M_writer('                    <td>')
                __M_writer(str(t.subcategory.name))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                    <td></td>\r\n')
            __M_writer('                    <td>')
            __M_writer(str(t.average_cost))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.sku))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.order_form_name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.production_time))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.photo))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.quantity_on_hand))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str(t.shelf_location))
            __M_writer('</td>\r\n                    <td><a href="/items.edit/')
            __M_writer(str(t.id))
            __M_writer('">Edit</a><span> | </span><a style="color:red" href="item.delete/')
            __M_writer(str(t.id))
            __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "manage.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/manage.html", "line_map": {"27": 0, "38": 1, "43": 53, "48": 110, "54": 2, "61": 2, "62": 24, "63": 25, "64": 26, "65": 26, "66": 27, "67": 27, "68": 28, "69": 28, "70": 29, "71": 29, "72": 30, "73": 31, "74": 31, "75": 31, "76": 32, "77": 33, "78": 35, "79": 36, "80": 36, "81": 36, "82": 37, "83": 38, "84": 40, "85": 40, "86": 40, "87": 41, "88": 41, "89": 42, "90": 42, "91": 43, "92": 43, "93": 44, "94": 44, "95": 45, "96": 45, "97": 46, "98": 46, "99": 47, "100": 47, "101": 47, "102": 47, "103": 50, "109": 54, "116": 54, "117": 78, "118": 79, "119": 80, "120": 80, "121": 81, "122": 81, "123": 82, "124": 82, "125": 83, "126": 83, "127": 84, "128": 84, "129": 85, "130": 85, "131": 86, "132": 86, "133": 87, "134": 88, "135": 88, "136": 88, "137": 89, "138": 90, "139": 92, "140": 93, "141": 93, "142": 93, "143": 94, "144": 95, "145": 97, "146": 97, "147": 97, "148": 98, "149": 98, "150": 99, "151": 99, "152": 100, "153": 100, "154": 101, "155": 101, "156": 102, "157": 102, "158": 103, "159": 103, "160": 104, "161": 104, "162": 104, "163": 104, "164": 107, "170": 164}, "source_encoding": "ascii"}
__M_END_METADATA
"""
