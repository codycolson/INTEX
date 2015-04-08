# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428482119.549203
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/items.html'
_template_uri = '/items.html'
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
        categories = context.get('categories', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cat = context.get('cat', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        def side():
            return render_side(context._locals(__M_locals))
        subcategories = context.get('subcategories', UNDEFINED)
        search = context.get('search', UNDEFINED)
        sub = context.get('sub', UNDEFINED)
        items = context.get('items', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for productspecification in items:
            __M_writer('\r\n    <div class="grid-container">\r\n        <div class="item_container">\r\n            <a href="/items.view/')
            __M_writer(str(productspecification.id))
            __M_writer('"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( productspecification.photo ))
            __M_writer('"/></a>\r\n            <div>')
            __M_writer(str(productspecification.name))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str(productspecification.price))
            __M_writer('</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sub = context.get('sub', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context)
        cat = context.get('cat', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n<ol class="breadcrumb">\r\n    <li><a href="/items">Items</a></li>\r\n')
        if cat:
            __M_writer('        <li><a href="/items/')
            __M_writer(str(cat.id))
            __M_writer('">')
            __M_writer(str(cat.name))
            __M_writer('</a></li>\r\n')
        if sub:
            __M_writer('        <li><a href="/items/')
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
        subcategories = context.get('subcategories', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        def side():
            return render_side(context)
        search = context.get('search', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="left-box"></div>\r\n<div class="right-box"></div>\r\n<div class="center-box">\r\n    <div class="category-list">Categories:</div>\r\n')
        for c in categories:
            __M_writer('        <div class="category-link"><a href="/items/')
            __M_writer(str( c.id ))
            __M_writer('">')
            __M_writer(str(c.name))
            __M_writer('</a></div>\r\n')
        if subcategories:
            __M_writer('        <div class="subcategory-list">Filter:</div>\r\n')
            for s in subcategories:
                __M_writer('        <div class="category-link"><a href="/items/3/')
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
{"source_encoding": "ascii", "line_map": {"128": 7, "129": 8, "130": 8, "131": 8, "132": 8, "133": 8, "134": 10, "135": 11, "136": 12, "137": 13, "138": 13, "139": 13, "140": 13, "141": 13, "142": 16, "143": 20, "144": 21, "145": 21, "146": 21, "147": 22, "148": 23, "149": 25, "27": 0, "155": 149, "45": 1, "50": 27, "55": 40, "60": 53, "66": 41, "74": 41, "75": 43, "76": 44, "77": 47, "78": 47, "79": 47, "80": 47, "81": 47, "82": 48, "83": 48, "84": 49, "85": 49, "91": 28, "99": 28, "100": 32, "101": 33, "102": 33, "103": 33, "104": 33, "105": 33, "106": 35, "107": 36, "108": 36, "109": 36, "110": 36, "111": 36, "112": 38, "118": 2, "127": 2}, "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/items.html", "uri": "/items.html"}
__M_END_METADATA
"""
