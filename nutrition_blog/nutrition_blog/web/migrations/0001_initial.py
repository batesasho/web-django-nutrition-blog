# Generated by Django 4.0.4 on 2022-04-15 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_url_image', models.URLField(default='https://cfpen.org/wp-content/uploads/2019/05/Eat_Healthy_Blog_15May19.jpg')),
                ('article_tag_name', models.CharField(default='Tips', max_length=15)),
                ('article_title', models.CharField(default='Healthy Advice', max_length=15)),
                ('description', models.TextField(default='Write down the information about current article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
