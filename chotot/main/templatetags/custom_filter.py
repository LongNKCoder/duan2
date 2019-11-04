from django import template
import locale
register = template.Library()

@register.filter(name = 'currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'vi_VN.utf8')
    except:
        locale.setlocale(locale.LC_ALL,'vi_VN.UTF-8')
    loc = locale.localeconv()
    return locale.currency(value, grouping=True)