# Generated by Django 4.0.4 on 2022-04-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_appuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
