# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428560022.452081
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/items.html'
_template_uri = '/items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'side', 'breadcrumbs']


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
        cat = context.get('cat', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        search = context.get('search', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def side():
            return render_side(context._locals(__M_locals))
        sub = context.get('sub', UNDEFINED)
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


def render_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        subcategories = context.get('subcategories', UNDEFINED)
        search = context.get('search', UNDEFINED)
        def side():
            return render_side(context)
        categories = context.get('categories', UNDEFINED)
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


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat = context.get('cat', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context)
        sub = context.get('sub', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        if request.user.is_superuser:
            __M_writer('        <p style="float:right"><a href="/items.create">Create New</a></p>\r\n')
        __M_writer('</ol>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"129": 28, "138": 28, "139": 32, "140": 33, "141": 33, "142": 33, "143": 33, "144": 33, "145": 35, "146": 36, "147": 36, "148": 36, "149": 36, "150": 36, "151": 38, "152": 39, "153": 41, "27": 0, "159": 153, "46": 1, "51": 27, "56": 43, "61": 56, "67": 44, "75": 44, "76": 46, "77": 47, "78": 50, "79": 50, "80": 50, "81": 50, "82": 50, "83": 51, "84": 51, "85": 52, "86": 52, "92": 2, "101": 2, "102": 7, "103": 8, "104": 8, "105": 8, "106": 8, "107": 8, "108": 10, "109": 11, "110": 12, "111": 13, "112": 13, "113": 13, "114": 13, "115": 13, "116": 16, "117": 20, "118": 21, "119": 21, "120": 21, "121": 22, "122": 23, "123": 25}, "source_encoding": "ascii", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/items.html", "uri": "/items.html"}
__M_END_METADATA
"""
