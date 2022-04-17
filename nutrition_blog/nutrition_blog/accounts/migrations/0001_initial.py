# Generated by Django 4.0.4 on 2022-04-15 09:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import nutrition_blog.accounts.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), nutrition_blog.accounts.validators.validate_only_letters])),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), nutrition_blog.accounts.validators.validate_only_letters])),
                ('age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('profile_image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_photo/', validators=[nutrition_blog.accounts.validators.ValidateMaxSizeMB])),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Do not show', max_length=11, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
