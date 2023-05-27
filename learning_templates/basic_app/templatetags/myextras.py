from django import template

register=template.Library()

def cut(value,arg):
    """
    This cuts out all values of "arg" fro the string !
    """
    return value.replace(arg,'')
    
