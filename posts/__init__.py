from urllib import quote_plus
from django import template

'''
In html templates must add
{% load urlify %}
to header
'''


register = template.Library()

@register.filter
def urlify(value):
	return quote_plus(value)