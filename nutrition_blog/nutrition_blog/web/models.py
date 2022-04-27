from django.contrib.auth import get_user_model
from django.db import models

from nutrition_blog.accounts.models import Profile, AppUser

UserModel = get_user_model()


class Articles(models.Model):
    ARTICLE_NAME_MAX_LEN = 15
    ARTICLE_TAG_NAME_MAX_LEN = 15

    article_url_image = models.URLField(
            default = "https://cfpen.org/wp-content/uploads/2019/05/Eat_Healthy_Blog_15May19.jpg",
    )
    article_tag_name = models.CharField(
            max_length = ARTICLE_TAG_NAME_MAX_LEN,
            default = "Tips",
    )

    article_title = models.CharField(
            max_length = ARTICLE_NAME_MAX_LEN,
            default = "Healthy Advice",
    )

    description = models.TextField(
            default = 'Write down the information about current article',
    )

    user = models.ForeignKey(
            UserModel,
            on_delete = models.CASCADE,
            # primary_key = True,
    )

    def __str__(self):
        return self.article_title

# class UserInformationModel(models.Model):
#     information_text_food_program = models.TextField(
#             blank = True,
#             null = True,
#     )
#     information_text_food_advices = models.TextField(
#             blank = True,
#             null = True,
#     )
#     information_text_tips = models.TextField(
#             blank = True,
#             null = True,
#     )
#
#     user = models.OneToOneField(
#             UserModel,
#             on_delete = models.CASCADE,
#             primary_key = True,
#
#
#     )
