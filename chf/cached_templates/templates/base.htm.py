# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428565154.352613
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/base.htm'
_template_uri = '/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['side', 'title', 'line', 'alt', 'breadcrumbs', 'nine', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def line():
            return render_line(context._locals(__M_locals))
        def alt():
            return render_alt(context._locals(__M_locals))
        def nine():
            return render_nine(context._locals(__M_locals))
        def side():
            return render_side(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def breadcrumbs():
            return render_breadcrumbs(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\r\n  <head>\r\n\r\n    <title>Colonial Heritage Foundation</title>\r\n    <meta charset="UTF-8">\r\n    <meta name="description" content="CH Foundation store and informative website">\r\n    <meta name="keywords" content="colonial, heritage, foundation, store, civil war">\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css"/>\r\n    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('bower_components/flat-ui/dist/css/flat-ui.min.css"/>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('chf/media/jquery.form.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('chf/media/jquery.loadmodal.js"></script>\r\n      <script src="http://listjs.com/no-cdn/list.js"></script>\r\n  </head>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  <body>\r\n    <header>\r\n        <nav id="top-header" class="navbar navbar-default">\r\n            <div class="container-fluid">\r\n                <div class="navbar-header">\r\n                    <a class="navbar-brand" href="/">Colonial Heritage Foundation</a>\r\n                 </div>\r\n            </div>\r\n        </nav>\r\n    </header>\r\n    <div class="right">\r\n')
        if request.user.is_authenticated():
            __M_writer('            Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('!<div class="logout"><a href="/account">Account</a><span> | </span><a href="/logout">Log out</a></div>\r\n')
        else:
            __M_writer('            <button id="show_login_dialog" class="btn btn-success">Login</button>\r\n            <a href="account.create">Register</a>\r\n')
        __M_writer('    </div>\r\n            <div class="center-menu">\r\n            <ul class="list-inline">\r\n              <li class="header-links"><a href="/items">Items</a></li>\r\n              <li class="header-links"><a href="/products">Products</a></li>\r\n              <li class="header-links"><a href="/events">Events</a></li>\r\n')
        if request.user.is_staff:
            __M_writer('                <li class="header-links"><a href="/products.returnrental">Return</a></li>\r\n                <li class="header-links"><a href="/report">Overdue</a></li>\r\n')
        if request.user.is_superuser:
            __M_writer('                <li class="header-links"><a href="/manage">Inventory</a></li>\r\n                <li class="header-links"><a href="/report.accounting">Accounting</a></li>\r\n                <li class="header-links"><a href="/users">Users</a></li>\r\n')
        if request.user.is_authenticated():
            __M_writer('                <li class="header-links" style="color:Black;"><a style="color:#D35400;font-weight:bold;" href="/account.checkout">My Cart</a></li>\r\n')
        __M_writer('            </ul>\r\n        </div>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'breadcrumbs'):
            context['self'].breadcrumbs(**pageargs)
        

        __M_writer("\r\n        <div class='side-bar'>")
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'side'):
            context['self'].side(**pageargs)
        

        __M_writer('</div>\r\n\r\n    <div id="middle">\r\n\r\n\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n        <div id = "main" class="container-fluid">\r\n            <div class="row">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n        <div id = "alt" class="container-fluid">\r\n            <div class = "row-fluid">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alt'):
            context['self'].alt(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n        <div id = "nine" class="container-fluid">\r\n            <div class = "row-fluid">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nine'):
            context['self'].nine(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n        <div id = "bottom" class="container-fluid">\r\n            <div class = "row-fluid">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'line'):
            context['self'].line(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n    <footer>\r\n        <div id ="footer" class="row-fluid">\r\n            <div class="spacer"></div>\r\n            <span class="footer-links"><a href="/about">about</a></span>\r\n            <span class="footer-links"><a href="/contact">contact</a></span>\r\n            <span class="footer-links"><a href="/terms">terms</a></span>\r\n\r\n        </div>\r\n    </footer>\r\n\r\n    <div class="copyright"><span>Copyright 2015, Team "Efficiency"</span></div>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def side():
            return render_side(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def line():
            return render_line(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alt(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alt():
            return render_alt(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def breadcrumbs():
            return render_breadcrumbs(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nine(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nine():
            return render_nine(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base.htm", "filename": "C:\\Users\\Cody\\Desktop\\Heritage\\chf\\templates/base.htm", "line_map": {"131": 74, "179": 90, "137": 96, "143": 96, "16": 4, "18": 0, "149": 84, "155": 84, "197": 191, "161": 66, "167": 66, "40": 2, "41": 4, "42": 5, "173": 90, "46": 5, "47": 17, "48": 20, "49": 20, "50": 21, "51": 21, "52": 22, "53": 22, "54": 27, "55": 27, "56": 27, "57": 40, "58": 41, "59": 41, "60": 41, "61": 42, "62": 43, "63": 46, "64": 52, "65": 53, "66": 56, "67": 57, "68": 61, "69": 62, "70": 64, "75": 68, "80": 69, "85": 75, "185": 78, "90": 79, "95": 85, "100": 91, "105": 97, "106": 115, "107": 115, "108": 115, "114": 69, "191": 78, "125": 74}, "source_encoding": "ascii"}
__M_END_METADATA
"""
