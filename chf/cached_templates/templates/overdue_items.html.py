# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428211853.262892
_enable_loop = True
_template_filename = 'C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/overdue_items.html'
_template_uri = 'overdue_items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h4>Uh oh!</h4>\r\n</br>\r\n</br>\r\nLooks like you have an overdue item:\r\n</br>\r\n\r\n<div class="grid-container">\r\n    <div class="item_container">\r\n        <div>')
        __M_writer(str(items.rental_product.name))
        __M_writer('</div>\r\n    </div>\r\n</div>\r\n\r\n<p>If you have any questions or concerns about your items, please contact our support team at support@colonialheritagefoundation.com</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "overdue_items.html", "filename": "C:\\Users\\Cody\\Desktop\\chf\\chf\\templates/overdue_items.html", "line_map": {"16": 0, "24": 9, "30": 24, "22": 1, "23": 9}, "source_encoding": "ascii"}
__M_END_METADATA
"""
