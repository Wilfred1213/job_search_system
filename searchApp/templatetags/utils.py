from django import template
register = template.Library()


import re

@register.filter(name='split')
def split(value, sep):
    return re.split(sep, value)


# @register.filter(name='split')
# def split(value, arg):
#     return value.split(arg)


