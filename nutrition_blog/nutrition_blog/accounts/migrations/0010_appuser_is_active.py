# Generated by Django 4.0.4 on 2022-04-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_appuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
