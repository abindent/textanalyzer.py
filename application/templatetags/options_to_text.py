from django import template
register = template.Library()

@register.filter(name="options_to_text")
def options_to_text(option: str) -> str:
    list ={
    "AD": "admin post",
    "ST": "staff post",
    "BW": "access to wrtie a blog."
  }
    return list[option]