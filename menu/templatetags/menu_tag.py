from django import template
from menu.models import Menu
register = template.Library()

@register.simple_tag
def get_menu():
    menu = Menu.objects.all()
    return menu
