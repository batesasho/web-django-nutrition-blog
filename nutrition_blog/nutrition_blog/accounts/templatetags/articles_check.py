from django import template
from django.contrib.auth import get_user_model

from nutrition_blog.web.models import Articles

register = template.Library()

UserModel = get_user_model()


# @register.simple_tag
# def articles_count():
#
#     return len(Articles.objects.all(user = get_user_model())) > 0


@register.inclusion_tag('base/base.html', takes_context = True)
def count_articles(context):
    variable = UserModel.objects. \
        prefetch_related('articles_set'). \
        all()

    result = {
            'variable': context[variable],
    }
    return result
