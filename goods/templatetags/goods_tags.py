from django import template

from goods.models import Products

register = template.Library()

@register.simple_tag()
def goods():
    return Products.objects.all()