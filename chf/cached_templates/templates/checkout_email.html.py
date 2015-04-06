# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428104651.853847
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/checkout_email.html'
_template_uri = 'checkout_email.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h4>Thank you for your purchase!</h4>\r\n</br>\r\n</br>\r\n')
        for productspecification in items:
            __M_writer('\r\n<div class="grid-container">\r\n    <div class="item_container">\r\n        <div>')
            __M_writer(str(productspecification.name))
            __M_writer('</div>\r\n        <div>$')
            __M_writer(str(productspecification.price))
            __M_writer('</div>\r\n    </div>\r\n</div>\r\n')
        __M_writer('\r\n<p>If you have any questions or concerns about your items, please contact our support team at support@colonialheritagefoundation.com</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "35": 29, "22": 1, "23": 4, "24": 5, "25": 8, "26": 8, "27": 9, "28": 9, "29": 13}, "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/checkout_email.html", "source_encoding": "ascii", "uri": "checkout_email.html"}
__M_END_METADATA
"""
