from django.contrib import admin

from nutrition_blog.web.models import Articles


@admin.register(Articles)
class ArticlesUserAdmin(admin.ModelAdmin):

    list_display = ('user', 'article_title', "article_url_image", 'article_tag_name',)
