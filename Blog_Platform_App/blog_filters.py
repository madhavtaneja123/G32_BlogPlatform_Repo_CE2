from django import template
import math

register = template.Library()  # This is required

@register.filter(name='reading_time')
def reading_time(text):
    """Calculate reading time based on word count (200 words per minute)"""
    if not text:
        return "0 min read"
    word_count = len(text.split())
    minutes = math.ceil(word_count / 200)  # Round up to nearest minute
    return f"{minutes} min read"