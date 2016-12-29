"""
Utility module used in template_minifier.
"""
import re

from django.conf import settings


def strip_spaces_in_template(template_source):
    """
    Default function used to preprocess templates.
    
    Use settings.TEMPLATE_MINIFIER_HTML_TAGS or 
    settings.TEMPLATE_MINIFIER_TEMPLATE_TAGS to change
    its behaviour.
    
    To use Your own stripping function do not change this function, use
    **settings.TEMPLATE_MINIFIER_STRIP_FUNCTION property**!
    """
    if getattr(settings, 'TEMPLATE_MINIFIER_HTML_TAGS', True):
        template_source = re.sub(r'>\s+<', '><', template_source)

    if getattr(settings, 'TEMPLATE_MINIFIER_TEMPLATE_TAGS', True):
        template_source = re.sub(r'\s+{ ?%', ' {%', template_source)
        template_source = re.sub(r'% ?}\s+', '%} ', template_source)

    return template_source


def get_function_from_string(string):
    """
    Return function from given dotted string. It imports correct module
    and than gets needed functon.
    """
    (modulename, function_name) = string.rsplit('.', 1)
    m = __import__(modulename, globals(), locals(), [function_name])
    return getattr(m, function_name)


def get_template_minifier_strip_function():
    """
    Getting proper template strip function, taking into consideration
    TEMPLATE_MINIFER_STRIP_FUNCTION setting.
    """
    if getattr(settings, 'TEMPLATE_MINIFER_STRIP_FUNCTION', False):
        return get_function_from_string(settings.TEMPLATE_MINIFER_STRIP_FUNCTION)
    else:
        return strip_spaces_in_template
