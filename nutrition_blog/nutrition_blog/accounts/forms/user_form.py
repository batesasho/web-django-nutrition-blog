import os
from os.path import join

from django import forms
from django.conf import settings
from django.contrib.auth import forms as auth_forms, get_user_model

from nutrition_blog.accounts.models import Profile

# from nutrition_blog.web.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    # adding first_name field&last_name in the form
    FIRST_NAME_MAX_LEN = 20
    # LAST_NAME_MAX_LEN = 20
    first_name = forms.CharField(
            max_length = FIRST_NAME_MAX_LEN,
    )

    # last_name = forms.CharField(
    #         max_length = LAST_NAME_MAX_LEN,
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
                attrs = {'class': 'user_info email', 'placeholder': 'Enter Your Email', })
        self.fields['password1'].widget = forms.PasswordInput(
                attrs = {'class': 'user_info password', 'placeholder': 'New password', }, )
        self.fields['password2'].widget = forms.PasswordInput(
                attrs = {'class': 'user_info password', 'placeholder': 'Repeat password', })
        self.fields['first_name'].widget = forms.TextInput(
                attrs = {'class': 'user_info name', 'placeholder': 'Enter Your Name', })
        # self.fields['last_name'].widget = forms.TextInput(attrs = {'class': 'user_info name'})
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean_first_name(self):
        return self.cleaned_data['first_name']  # , self.cleaned_data['last_name']

    # save first_name in database during POST
    #
    def save(self, commit = True):
        user_created = super().save(commit = commit)
        profile = Profile(
                first_name = self.cleaned_data['first_name'],
                user = user_created,
        )
        if commit:
            profile.save()
        return user_created

    class Meta:
        model = UserModel
        fields = ('first_name', 'email',)


class LoginUserForm(auth_forms.AuthenticationForm):
    error_messages = {
            "invalid_login": (
                    "Please enter a correct %(username)s and password."
            ),
            "inactive": ("This account is inactive."),
    }


class EditUserProfileBasicInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['gender'] = Profile.DO_NOT_SHOW
        # self.initial['profile_image'].widget.attrs['placeholder'] = "Your profile image"
        # self.initial['profile_image'].widget.attrs['class'] = "user_info profile_image"
        # self.fields['first_name'].label_class = 'user_info first_name'
        # self.fields['last_name'].label_class = 'user_info last_name'
        # self.fields['age'].label_class = 'user_info age'

    # delete user profile old photo in the media file system
    def save(self, commit = True):
        db_profile = Profile.objects.get(pk = self.instance.pk)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_profile.profile_image))
            try:
                os.remove(image_path)
            except:
                pass
        return super().save(commit)

    class Meta:
        model = Profile
        fields = ('first_name', "last_name", "age", 'gender', 'profile_image')
        widgets = {

                'first_name': forms.TextInput(
                        attrs = {
                                'placeholder': 'Enter your first name',
                                'class': 'user_info first_name',

                        }, ),

                'last_name': forms.TextInput(
                        # max_length = LAST_NAME_MAX_LENGTH,
                        attrs = {
                                'placeholder': 'Enter your last name',
                                'class': 'user_info last_name',
                        }, ),

                'age': forms.NumberInput(
                        attrs = {
                                'placeholder': 'Enter your age',
                                'class': 'user_info age',
                        }, ),

                'profile_image': forms.FileInput(),

                'gender': forms.Select(

                        attrs = {
                                'class': 'user_info gender',
                        }, ),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['first_name'].widget = forms.TextInput(
    #             attrs = {'class': 'user_info first_name', 'placeholder': 'Enter Your First Name', })
    #     self.fields['last_name'].widget = forms.TextInput(
    #             attrs = {'class': 'user_info last_name', 'placeholder': 'Enter Your Last Name', })
    #     self.fields['age'].widget = forms.IntegerField(
    #             attrs = {'class': 'user_info age', 'placeholder': 'Enter Your age', },
    #     )
    #     self.fields['password1'].widget = forms.PasswordInput(
    #             attrs = {'class': 'user_info password', 'placeholder': 'New password', }, )
    #     self.fields['password2'].widget = forms.PasswordInput(
    #             attrs = {'class': 'user_info password', 'placeholder': 'Repeat password', })


class DeleteUserProfileBasicInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit = True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('user',)


class UserPasswordResetForm(auth_forms.PasswordResetForm):
    '''
     checking for existing email address in the database before reset the password
    '''

    def clean_email(self):
        email = self.cleaned_data['email']
        if not UserModel.objects.filter(email__iexact = email, is_active = True).exists():
            msg = ("There is no user registered with the specified e-mail address, please enter a registered email.")
            self.add_error('email', msg)
        return email


# !!!! Django Ratelimit - security check i.e if a user sends more than certain times reset's request he will be rejected


class UserPasswordResetConfirmForm(auth_forms.SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
