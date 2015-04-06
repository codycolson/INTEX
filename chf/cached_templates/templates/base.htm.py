# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428258177.272603
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'nine', 'line', 'content', 'alt']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def nine():
            return render_nine(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def alt():
            return render_alt(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def line():
            return render_line(context._locals(__M_locals))
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
        __M_writer('chf/media/jquery.loadmodal.js"></script>\r\n  </head>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  <body>\r\n    <header>\r\n        <nav id="top-header" class="navbar navbar-default">\r\n            <div class="container-fluid">\r\n                <div class="navbar-header">\r\n                    <a class="navbar-brand" href="#">Colonial Heritage Foundation</a>\r\n                 </div>\r\n            </div>\r\n        </nav>\r\n    </header>\r\n    <div class="right">\r\n')
        if request.user.is_authenticated():
            __M_writer('            Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('!<div class="logout"><a href="/account">Account</a><span> | </span><a href="/logout">Log out</a></div>\r\n')
        else:
            __M_writer('            <button id="show_login_dialog" class="btn btn-success">Login</button>\r\n            <a href="account.create">Register</a>\r\n')
        __M_writer('    </div>\r\n\r\n    <div id="middle">\r\n        <div class="center-menu">\r\n            <ul class="list-inline">\r\n              <li class="header-links"><a href="/items">Items</a></li>\r\n              <li class="header-links"><a href="/products">Products</a></li>\r\n              <li class="header-links"><a href="/events">Events</a></li>\r\n              <li class="header-links"><a href="/areas">Areas</a></li>\r\n              <li class="header-links"><a href="/users">Users</a></li>\r\n              <li class="header-links"><a href="/batch">Batch</a></li>\r\n              <li class="header-links"><a href="/report">Report</a></li>\r\n')
        if request.user.is_authenticated():
            __M_writer('              <li class="header-links"><a href="/account.checkout">My Cart</a></li>\r\n')
        __M_writer('            </ul>\r\n        </div>\r\n            ')
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
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n    <footer>\r\n        <div id = footer class="row-fluid">\r\n            <div class="spacer"></div>\r\n            <span class="footer-links"><a href="/about">about</a></span>\r\n            <span class="footer-links"><a href="/contact">contact</a></span>\r\n            <span class="footer-links"><a href="/terms">terms</a></span>\r\n\r\n        </div>\r\n    </footer>\r\n\r\n    <div class="copyright"><span>Copyright 2015, Colson Enterprises</span></div>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/base.htm", "line_map": {"132": 66, "138": 66, "16": 4, "18": 0, "150": 72, "156": 150, "36": 2, "37": 4, "38": 5, "42": 5, "43": 17, "44": 20, "45": 20, "46": 21, "47": 21, "48": 22, "49": 22, "50": 26, "51": 26, "52": 26, "53": 39, "54": 40, "55": 40, "56": 40, "57": 41, "58": 42, "59": 45, "60": 57, "61": 58, "62": 60, "67": 63, "72": 67, "77": 73, "82": 79, "87": 85, "88": 103, "89": 103, "90": 103, "96": 62, "144": 72, "102": 62, "108": 78, "114": 78, "120": 84, "126": 84}, "source_encoding": "ascii"}
__M_END_METADATA
"""
