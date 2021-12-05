from django import template

register = template.Library()


@register.simple_tag()
def is_select(re_fun, re_select: str):
	"""

	"""
	if re_fun == re_select:
		res = 'selected="selected"'
	else:
		res = ''
	return res
