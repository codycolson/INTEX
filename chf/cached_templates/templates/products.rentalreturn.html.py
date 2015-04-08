# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428484039.955832
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.rentalreturn.html'
_template_uri = '/products.rentalreturn.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'breadcrumbs', 'side']


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
        search = context.get('search', UNDEFINED)
        def side():
            return render_side(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        sub = context.get('sub', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        cat = context.get('cat', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'side'):
            context['self'].side(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'breadcrumbs'):
            context['self'].breadcrumbs(**pageargs)
        

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
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for product in products:
            __M_writer('\r\n    <div class="grid-container">\r\n        <div class="item_container">\r\n            <a href="products.viewreturn/')
            __M_writer(str(product.id))
            __M_writer('"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( product.rental_product.photo ))
            __M_writer('"/></a>\r\n            <div>')
            __M_writer(str(product.rental_product.name))
            __M_writer('</div>\r\n            <div>')
            __M_writer(str(product.transaction.customer.first_name))
            __M_writer('</div>\r\n            <div>Due: ')
            __M_writer(str(product.date_due.strftime('%B %d, %Y')))
            __M_writer('</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def breadcrumbs():
            return render_breadcrumbs(context)
        cat = context.get('cat', UNDEFINED)
        sub = context.get('sub', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n<ol class="breadcrumb">\r\n    <li><a href="/products.viewreturn">Products Currently Rented</a></li>\r\n')
        if cat:
            __M_writer('        <li><a href="/products.viewreturn/')
            __M_writer(str(cat.id))
            __M_writer('">')
            __M_writer(str(cat.name))
            __M_writer('</a></li>\r\n')
        if sub:
            __M_writer('        <li><a href="/products.viewreturn/')
            __M_writer(str(sub.id))
            __M_writer('">')
            __M_writer(str(sub.name))
            __M_writer('</a></li>\r\n')
        __M_writer('</ol>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        search = context.get('search', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        def side():
            return render_side(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="left-box"></div>\r\n<div class="right-box"></div>\r\n<div class="center-box">\r\n    <div class="category-list">Categories:</div>\r\n')
        for c in categories:
            __M_writer('        <div class="category-link"><a href="/products.viewreturn/')
            __M_writer(str( c.id ))
            __M_writer('">')
            __M_writer(str(c.name if c.name != 'Custom Orders' else ""))
            __M_writer('</a></div>\r\n')
        if subcategories:
            __M_writer('        <div class="subcategory-list">Filter:</div>\r\n')
            for s in subcategories:
                __M_writer('        <div class="category-link"><a href="/products.viewreturn/3/')
                __M_writer(str( s.id ))
                __M_writer('">')
                __M_writer(str(s.name))
                __M_writer('</a></div>\r\n')
        __M_writer('    <div id="input-box" class="input-group input-group-hg input-group-rounded">\r\n      <span class="input-group-btn">\r\n        <a id="searchbox" class="btn"><span class="fui-search"></span></a>\r\n      </span>\r\n')
        if search:
            __M_writer('        <input type="text" class="form-control" value="')
            __M_writer(str(search))
            __M_writer('" placeholder="Search" id="search">\r\n')
        else:
            __M_writer('        <input type="text" class="form-control" placeholder="Search" id="search">\r\n')
        __M_writer('    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "/products.rentalreturn.html", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/products.rentalreturn.html", "line_map": {"129": 2, "130": 7, "131": 8, "132": 8, "133": 8, "134": 8, "135": 8, "136": 10, "137": 11, "138": 12, "139": 13, "140": 13, "141": 13, "142": 13, "143": 13, "144": 16, "145": 20, "146": 21, "147": 21, "148": 21, "149": 22, "150": 23, "151": 25, "27": 0, "157": 151, "45": 1, "50": 27, "55": 40, "60": 54, "66": 41, "74": 41, "75": 43, "76": 44, "77": 47, "78": 47, "79": 47, "80": 47, "81": 47, "82": 48, "83": 48, "84": 49, "85": 49, "86": 50, "87": 50, "93": 28, "101": 28, "102": 32, "103": 33, "104": 33, "105": 33, "106": 33, "107": 33, "108": 35, "109": 36, "110": 36, "111": 36, "112": 36, "113": 36, "114": 38, "120": 2}}
__M_END_METADATA
"""
