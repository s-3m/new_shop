from django import template

from mainapp.utils import top_main_menu

register = template.Library()


@register.simple_tag(name="top_menu")
def top_menu():
    return top_main_menu
