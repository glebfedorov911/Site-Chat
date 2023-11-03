from django import template

register = template.Library()

@register.simple_tag()
def new_cost(amount, discount):
    amount = int(amount)
    discount = int(discount)
    return str(int(amount*(1.0-discount/100)))