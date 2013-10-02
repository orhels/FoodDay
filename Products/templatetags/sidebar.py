from Products.views import get_sidebar_widget_rendered
from django import template

register = template.Library()


def sidebar():
    return get_sidebar_widget_rendered()

register.simple_tag(sidebar)