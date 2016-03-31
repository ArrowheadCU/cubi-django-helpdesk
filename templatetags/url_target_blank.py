"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

templatetags/url_target_blank.py
    Very simple template tag to allow us to target new tab on
    link selection

Assuming 'food' = 'pizza' and 'best_foods' = ['pizza', 'pie', 'cake]:

{% if food|in_list:best_foods %}
 You've selected one of our favourite foods!
{% else %}
 Your food isn't one of our favourites.
{% endif %}
"""


from django import template
import re


#@register.filter(name = 'url_target_blank')
def url_target_blank(value):
    return re.sub("<a([^>]+)(?<!target=)>",'<a target="_blank"\\1>',value)

register = template.Library()
register.filter('url_target_blank',url_target_blank, is_safe = True)
