from django import template
from django.template.defaultfilters import stringfilter

from datetime import datetime

#created following https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/
#verified python's datetime.now strftime formatting from documentation here: https://docs.python.org/3/library/datetime.html
#   year will always be 4 digits, month and day will always be padded.

register = template.Library()

@register.filter
@stringfilter
def l2l_dt(value):
    """Converts a datetime string from %Y-%m-%dT%H:%M:%S format to %Y-%m-%d %H:%M:%S"""
    #this is lazy but simple and gets the job done. I haven't filled an hour, so let's find a better solution.
    #return value.replace("T", " ")[:19]
    
    dt_object = None
    try: 
        dt_object = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    except Exception:
        #string filter will turn the datetime object into a string -- this will be in the format %Y-%m-%d %H:%M:%S.%f
        try:
            dt_object = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
        except Exception: #bummer -- we've hit a case that hasn't been handled.
            return value
    return dt_object.strftime("%Y-%m-%d %H:%M:%S")
