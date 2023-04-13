from django import template
from django.utils.safestring import mark_safe
from menu.models import Menu
from typing import List
register = template.Library()
from django.urls import reverse

@register.simple_tag()
def draw_menu() -> str:
    menu_items = Menu.objects.all().values()
    return mark_safe(get_menu(menu_items))


def get_menu(menu_items: List, menu: str = '', parent_id: int = None, repeat: List = None) -> str:
    if repeat is None:
        repeat = []
    menu += '<ul>'
    for item in menu_items:
        if item not in repeat and item['parent_id'] == parent_id:
            menu += '<li><a href="{url}">{title}</a></li>'.format(
                url=reverse('menu', kwargs={'slug': item['url']}),
                title=item['title'],
            )
            child = [children for children in menu_items if children['parent_id'] == item['id']]
            if child:
                res = get_menu(menu_items, '', item['id'], repeat)
                menu += res
                repeat.extend(child)
            menu += '</li>'
    menu += '</ul>'
    print(menu)
    return menu