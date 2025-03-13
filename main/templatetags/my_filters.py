from django import template

register = template.Library()


@register.filter
def dot_separator(value):
    """Форматирует число с точкой как разделителем тысяч"""
    if isinstance(value, (int, float)):
        return f"{value:,}".replace(",", ".")  # Заменяем запятую на точку
    return value
