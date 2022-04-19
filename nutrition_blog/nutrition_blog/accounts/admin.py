from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from nutrition_blog.accounts.models import Profile

UserModel = get_user_model()


@admin.register(Profile)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'age', 'user_email_address',)

    list_filter = ('first_name',)
    ordering = ('first_name',)

    # def get_form(self, request, obj = None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #
    #     if not is_superuser:
    #         form.base_fields['user'].disabled = True
    #
    #     return form

    @staticmethod
    def user_email_address(obj):
        return obj.user.email


# preventing non-superuser to grant superuser rights i.e even changing in the User model
@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_superuser',  # 'article_name', 'article_tag', 'user_first_name',
                    # 'user_last_name', 'user_age', 'user_gender',
                    )
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)

    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Permissions', {
                    'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }),
            ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
            (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2'),
            }),
    )

    @staticmethod
    def article_name(obj):
        return [x.article_title for x in obj.articles_set.all()]

    @staticmethod
    def article_tag(obj):
        return [x.article_tag_name for x in obj.articles_set.all()]

    @staticmethod
    def user_first_name(obj):
        return obj.profile.first_name

    @staticmethod
    def user_last_name(obj):
        return obj.profile.last_name

    @staticmethod
    def user_age(obj):
        return obj.profile.age

    @staticmethod
    def user_gender(obj):
        return obj.profile.gender

    def get_form(self, request, obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        # fix - any user with a change permission on the User model can make any user a superuser
        # |= update between two sets - set2 add to set1 any elements in set2 that set1 does not already have
        # if a user is superuser we add email and is_superuser fields i.e preventing other users to become superusers
        # if not is_superuser:
        #     disabled_fields |= {
        #             'email',
        #             'is_superuser',
        #
        #     }

        # Prevent non-superusers from editing their own permissions
        # - When obj is None, the form is used to create a new user.
        # - When obj is not None, the form is used to edit an existing user.
        # - To check if the user making the request is operating on themselves, compare request.user with obj.
        #   Because this is the user admin, obj is either an instance of User, or None.
        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
            }

        # marking all fields disabled
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
