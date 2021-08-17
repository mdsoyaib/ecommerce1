from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    # keys = cart.keys()
    # print(keys)
    print(product, cart)
    return True
