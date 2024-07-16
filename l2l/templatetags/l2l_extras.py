from django import template
from django.template.defaultfilters import stringfilter

#created following https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/
#verified python's datetime.now strftime formatting from documentation here: https://docs.python.org/3/library/datetime.html
#   year will always be 4 digits, month and day will always be padded.

register = template.Library()

@register.filter
@stringfilter
def l2l_dt(value):
    """Converts a datetime string from %Y-%m-%dT%H:%M:%S format to %Y-%m-%d %H:%M:%S"""
    return value.replace("T", " ")[:19]