from django import template

register = template.Library()

WORDS = ['лесом', 'дали', 'нафнаф', 'big', 'sometitle']

@register.filter(name='Censor')
def Censor(value):
    for word in WORDS:
        value = value.replace(word[1:], '*' * (len(word) - 1))
    return value