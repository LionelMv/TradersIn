from django import template

register = template.Library()


@register.filter(name='truncate_words')
def truncate_words(value, arg):
    """
    Truncates a string after a certain number of words.

    Argument: Number of words to truncate after.
    """
    try:
        limit = int(arg)
    except ValueError:
        return value  # Return original value if limit is not an integer

    words = value.split()
    if len(words) > limit:
        return " ".join(words[:limit]) + "..."
    return value
